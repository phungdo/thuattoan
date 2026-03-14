#!/usr/bin/env python3
"""
LaTeX → Audio Lecture Pipeline
===============================
Extracts sections from a LaTeX .tex file, converts math notation
to spoken Vietnamese, and generates .mp3 audio for each section
using Edge TTS.

Usage:
    python3 tex_to_audio.py                          # all sections
    python3 tex_to_audio.py --sections 1 3 5         # specific sections
    python3 tex_to_audio.py --list                   # list available sections
    python3 tex_to_audio.py --voice vi-VN-NamMinhNeural  # male voice
"""

import re
import os
import sys
import asyncio
import argparse
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("❌ edge-tts not installed. Run: pip3 install edge-tts")
    sys.exit(1)

# ============================================================
# CONFIG
# ============================================================
DEFAULT_TEX_FILE = "LECTURE_NOTES_ALGORITHMS.tex"
OUTPUT_DIR = "audio_lectures"
DEFAULT_VOICE = "vi-VN-HoaiMyNeural"  # Female Vietnamese
DEFAULT_RATE = "-5%"  # Slightly slower for lecture style

# ============================================================
# MATH → SPEECH CONVERSION
# ============================================================
MATH_RULES = [
    # Big-O notation
    (r'O\s*\(\s*n\s*\\lg\s*n\s*\)', 'Ô lớn của n nhân lốc n'),
    (r'O\s*\(\s*n\^2\s*\)', 'Ô lớn của n bình phương'),
    (r'O\s*\(\s*n\^3\s*\)', 'Ô lớn của n lập phương'),
    (r'O\s*\(\s*n\^(\w+)\s*\)', r'Ô lớn của n mũ \1'),
    (r'O\s*\(\s*2\^n\s*\)', 'Ô lớn của 2 mũ n'),
    (r'O\s*\(\s*n!\s*\)', 'Ô lớn của n giai thừa'),
    (r'O\s*\(\s*(\w+)\s*\)', r'Ô lớn của \1'),
    (r'O\s*\(\s*1\s*\)', 'Ô lớn của 1, tức hằng số'),
    (r'O\s*\(\s*\\lg\s*n\s*\)', 'Ô lớn của lốc n'),
    (r'O\s*\(\s*\\log\s*n\s*\)', 'Ô lớn của lốc n'),

    # Theta notation
    (r'\\Theta\s*\(\s*n\s*\\lg\s*n\s*\)', 'Theta của n nhân lốc n'),
    (r'\\Theta\s*\(\s*n\^2\s*\)', 'Theta của n bình phương'),
    (r'\\Theta\s*\(\s*(\w+)\s*\)', r'Theta của \1'),

    # Omega notation
    (r'\\Omega\s*\(\s*(\w+)\s*\)', r'Omega của \1'),

    # Logarithms
    (r'\\lg\s*n', 'lốc n'),
    (r'\\lg\s*(\w)', r'lốc \1'),
    (r'\\log_2\s*n', 'lốc cơ số 2 của n'),
    (r'\\log_2\s*(\w)', r'lốc cơ số 2 của \1'),
    (r'\\log\s*n', 'lốc n'),

    # Powers
    (r'(\w)\^{\s*2\s*}', r'\1 bình phương'),
    (r'(\w)\^2', r'\1 bình phương'),
    (r'(\w)\^{\s*3\s*}', r'\1 lập phương'),
    (r'(\w)\^3', r'\1 lập phương'),
    (r'(\w)\^{\s*(\w+)\s*}', r'\1 mũ \2'),
    (r'(\w)\^(\w)', r'\1 mũ \2'),
    (r'2\^k', '2 mũ k'),
    (r'2\^n', '2 mũ n'),

    # Subscripts
    (r'(\w)_{\s*(\w+)\s*}', r'\1 \2'),
    (r'(\w)_(\w)', r'\1 \2'),

    # Greek letters
    (r'\\alpha', 'alpha'),
    (r'\\beta', 'beta'),
    (r'\\gamma', 'gamma'),
    (r'\\delta', 'delta'),
    (r'\\epsilon', 'epsilon'),
    (r'\\lambda', 'lambda'),
    (r'\\sigma', 'sigma'),
    (r'\\pi', 'pi'),
    (r'\\phi', 'phi'),
    (r'\\theta', 'theta'),

    # Relations and operators
    (r'\\infty', 'vô cùng'),
    (r'\\to', ' đến '),
    (r'\\rightarrow', ' đến '),
    (r'\\leftarrow', ' từ '),
    (r'\\Rightarrow', ' suy ra '),
    (r'\\Leftarrow', ' được suy ra từ '),
    (r'\\leq', ' nhỏ hơn hoặc bằng '),
    (r'\\geq', ' lớn hơn hoặc bằng '),
    (r'\\neq', ' khác '),
    (r'\\approx', ' xấp xỉ '),
    (r'\\equiv', ' tương đương '),
    (r'\\times', ' nhân '),
    (r'\\cdot', ' nhân '),
    (r'\\div', ' chia '),
    (r'\\pm', ' cộng trừ '),
    (r'\\mp', ' trừ cộng '),
    (r'\\cap', ' giao '),
    (r'\\cup', ' hợp '),
    (r'\\subset', ' tập con của '),
    (r'\\in', ' thuộc '),
    (r'\\notin', ' không thuộc '),
    (r'\\forall', ' với mọi '),
    (r'\\exists', ' tồn tại '),

    # Functions
    (r'\\min', 'min'),
    (r'\\max', 'max'),
    (r'\\sum', 'tổng'),
    (r'\\prod', 'tích'),
    (r'\\lim', 'giới hạn'),
    (r'\\sqrt\{([^}]+)\}', r'căn bậc hai của \1'),
    (r'\\sqrt', 'căn bậc hai'),
    (r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 trên \2'),

    # Matrices & arrays
    (r'\\begin\{pmatrix\}', ''),
    (r'\\end\{pmatrix\}', ''),
    (r'\\begin\{bmatrix\}', ''),
    (r'\\end\{bmatrix\}', ''),

    # Common algorithm terms
    (r'\\textbf\{([^}]+)\}', r'\1'),
    (r'\\textit\{([^}]+)\}', r'\1'),
    (r'\\emph\{([^}]+)\}', r'\1'),
    (r'\\text\{([^}]+)\}', r'\1'),
    (r'\\mathbf\{([^}]+)\}', r'\1'),
    (r'\\mathrm\{([^}]+)\}', r'\1'),
]


def math_to_speech(text: str) -> str:
    """Convert LaTeX math notation to spoken Vietnamese."""
    for pattern, replacement in MATH_RULES:
        text = re.sub(pattern, replacement, text)
    return text


# ============================================================
# LATEX STRIPPING
# ============================================================
def strip_latex(text: str) -> str:
    """Remove LaTeX markup, keeping readable text."""
    # Remove comments
    text = re.sub(r'(?<!\\)%.*$', '', text, flags=re.MULTILINE)

    # Handle custom environments
    text = re.sub(r'\\intuition\{', '', text)  # custom \intuition{...} command

    # Convert math to speech BEFORE stripping delimiters
    text = math_to_speech(text)

    # Remove display math delimiters
    text = re.sub(r'\$\$(.+?)\$\$', r' \1 ', text, flags=re.DOTALL)
    text = re.sub(r'\\\[(.+?)\\\]', r' \1 ', text, flags=re.DOTALL)
    text = re.sub(r'\\\((.+?)\\\)', r' \1 ', text, flags=re.DOTALL)

    # Remove inline math delimiters
    text = re.sub(r'\$([^$]+?)\$', r' \1 ', text)

    # Convert \item to bullet points (spoken)
    text = re.sub(r'\\item\b', '\n• ', text)

    # Remove environments (but keep content inside intuition/tcolorbox)
    text = re.sub(r'\\begin\{(?:enumerate|itemize|description)\}(?:\[.*?\])?', '', text)
    text = re.sub(r'\\end\{(?:enumerate|itemize|description)\}', '', text)
    text = re.sub(r'\\begin\{(?:center|quote|minipage|figure|table)\}(?:\[.*?\])?', '', text)
    text = re.sub(r'\\end\{(?:center|quote|minipage|figure|table)\}', '', text)

    # Remove TikZ pictures entirely (can't read diagrams)
    text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', 
                  '\n[Xem hình vẽ minh họa trong tài liệu PDF]\n', text, flags=re.DOTALL)

    # Remove verbatim/lstlisting (pseudocode) but note it
    text = re.sub(r'\\begin\{(?:verbatim|lstlisting)\}(?:\[.*?\])?(.+?)\\end\{(?:verbatim|lstlisting)\}',
                  r'\n[Pseudocode - xem chi tiết trong tài liệu PDF]\n', text, flags=re.DOTALL)

    # Remove tcolorbox but keep inner text  
    text = re.sub(r'\\begin\{tcolorbox\}\[.*?\]', '', text)
    text = re.sub(r'\\end\{tcolorbox\}', '', text)

    # Remove tabular/longtable
    text = re.sub(r'\\begin\{(?:tabular|longtable|tabularx)\}.*?\\end\{(?:tabular|longtable|tabularx)\}',
                  '\n[Xem bảng trong tài liệu PDF]\n', text, flags=re.DOTALL)

    # Handle section commands (for structure)
    text = re.sub(r'\\(?:sub)*section\*?\{(.+?)\}', r'\n\n\1.\n\n', text)
    text = re.sub(r'\\paragraph\{(.+?)\}', r'\n\1: ', text)

    # Remove remaining LaTeX commands
    text = re.sub(r'\\(?:label|ref|cite|eqref|pageref|hyperref)\{[^}]*\}', '', text)
    text = re.sub(r'\\(?:caption|captionof)\{[^}]*\}\{[^}]*\}', '', text)
    text = re.sub(r'\\(?:caption|captionof)\{[^}]*\}', '', text)
    text = re.sub(r'\\(?:includegraphics|usepackage|newcommand|renewcommand|definecolor)(?:\[.*?\])?\{[^}]*\}', '', text)
    text = re.sub(r'\\(?:hfill|vfill|noindent|newpage|clearpage|pagebreak|bigskip|medskip|smallskip)', ' ', text)
    text = re.sub(r'\\(?:hspace|vspace)\*?\{[^}]*\}', ' ', text)
    text = re.sub(r'\\(?:textbf|textit|emph|underline|texttt|textsf|textsc)\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\(?:small|footnotesize|scriptsize|tiny|large|Large|LARGE|huge|Huge|normalsize|bfseries|itshape)\b', '', text)
    text = re.sub(r'\\(?:centering|raggedright|raggedleft)\b', '', text)
    text = re.sub(r'\\(?:rule)\{[^}]*\}\{[^}]*\}', '', text)

    # Remove \href but keep text
    text = re.sub(r'\\href\{[^}]*\}\{([^}]*)\}', r'\1', text)

    # Remove boxed
    text = re.sub(r'\\boxed\{([^}]*)\}', r'\1', text)

    # Remove remaining braces-only commands
    text = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{([^}]*)\}', r'\1', text)

    # Remove stray LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+\*?', '', text)

    # Clean up special chars
    text = text.replace('&', ' và ')
    text = text.replace('~', ' ')
    text = text.replace('\\\\', ' ')
    text = text.replace('\\', '')
    text = re.sub(r'[{}]', '', text)
    text = re.sub(r'\[.*?\]', '', text)  # remove optional args

    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    text = re.sub(r'^\s+$', '', text, flags=re.MULTILINE)

    return text.strip()


# ============================================================
# SECTION EXTRACTION
# ============================================================
def extract_sections(tex_content: str) -> list[dict]:
    """Extract sections from LaTeX content."""
    # Match \section, \subsection, \subsubsection
    section_pattern = re.compile(
        r'\\(section|subsection|subsubsection)\*?\{(.+?)\}',
        re.DOTALL
    )

    matches = list(section_pattern.finditer(tex_content))
    sections = []

    for i, match in enumerate(matches):
        level = match.group(1)
        title = match.group(2)
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(tex_content)

        # Clean title
        title_clean = re.sub(r'\\texorpdfstring\{[^}]*\}\{([^}]*)\}', r'\1', title)
        title_clean = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', title_clean)
        title_clean = re.sub(r'[$\\{}]', '', title_clean)
        title_clean = title_clean.strip()

        # Only include sections and subsections (not subsubsections unless short)
        if level in ('section', 'subsection'):
            content = tex_content[start:end]
            sections.append({
                'index': len(sections),
                'level': level,
                'title': title_clean,
                'content': content,
                'char_count': len(content)
            })

    return sections


# ============================================================
# AUDIO GENERATION
# ============================================================
async def generate_audio(text: str, output_path: str, voice: str, rate: str):
    """Generate audio from text using Edge TTS."""
    tts = edge_tts.Communicate(text, voice, rate=rate)
    await tts.save(output_path)


async def process_section(section: dict, output_dir: str, voice: str, rate: str) -> dict:
    """Process a single section: strip LaTeX → TTS → mp3."""
    # Strip LaTeX and convert math
    speech_text = strip_latex(section['content'])

    # Skip if too short (< 50 chars of actual content)
    if len(speech_text.strip()) < 50:
        return {**section, 'status': 'skipped', 'reason': 'too short'}

    # Add intro
    speech_text = f"{section['title']}.\n\n{speech_text}"

    # Generate filename
    safe_title = re.sub(r'[^\w\s-]', '', section['title'])
    safe_title = re.sub(r'\s+', '_', safe_title).strip('_')[:50]
    filename = f"{section['index']:02d}_{safe_title}.mp3"
    output_path = os.path.join(output_dir, filename)

    # Generate audio
    try:
        await generate_audio(speech_text, output_path, voice, rate)
        file_size = os.path.getsize(output_path)
        return {
            **section,
            'status': 'done',
            'filename': filename,
            'file_size': file_size,
            'speech_length': len(speech_text)
        }
    except Exception as e:
        return {**section, 'status': 'error', 'reason': str(e)}


# ============================================================
# MAIN
# ============================================================
async def main():
    parser = argparse.ArgumentParser(description='LaTeX → Audio Lecture Pipeline')
    parser.add_argument('--tex', default=DEFAULT_TEX_FILE, help='Input .tex file')
    parser.add_argument('--output', default=OUTPUT_DIR, help='Output directory for audio files')
    parser.add_argument('--voice', default=DEFAULT_VOICE, 
                        help='TTS voice (vi-VN-HoaiMyNeural or vi-VN-NamMinhNeural)')
    parser.add_argument('--rate', default=DEFAULT_RATE, help='Speech rate (e.g. -10%%)')
    parser.add_argument('--sections', nargs='+', type=int, help='Specific section indices to generate')
    parser.add_argument('--list', action='store_true', help='List available sections')
    parser.add_argument('--preview', type=int, help='Preview speech text for a section (by index)')

    args = parser.parse_args()

    # Read tex file
    tex_path = Path(args.tex)
    if not tex_path.exists():
        print(f"❌ File not found: {tex_path}")
        sys.exit(1)

    print(f"📖 Reading: {tex_path}")
    tex_content = tex_path.read_text(encoding='utf-8')

    # Extract sections
    sections = extract_sections(tex_content)
    print(f"📋 Found {len(sections)} sections\n")

    # List mode
    if args.list:
        print(f"{'#':>3}  {'Level':<12}  {'Title':<60}  {'Chars':>6}")
        print("─" * 90)
        for s in sections:
            level_icon = "📗" if s['level'] == 'section' else "  📘"
            print(f"{s['index']:3d}  {level_icon} {s['level']:<8}  {s['title']:<60}  {s['char_count']:6d}")
        return

    # Preview mode
    if args.preview is not None:
        idx = args.preview
        matching = [s for s in sections if s['index'] == idx]
        if not matching:
            print(f"❌ Section {idx} not found")
            return
        speech = strip_latex(matching[0]['content'])
        print(f"🔍 Preview of section {idx}: {matching[0]['title']}")
        print("═" * 60)
        print(speech[:2000])
        if len(speech) > 2000:
            print(f"\n... ({len(speech) - 2000} more characters)")
        return

    # Filter sections if specified
    if args.sections:
        sections = [s for s in sections if s['index'] in args.sections]
        print(f"🎯 Generating {len(sections)} selected sections")

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    # Process sections
    print(f"🎙️  Voice: {args.voice}")
    print(f"⏱️  Rate: {args.rate}")
    print(f"📁 Output: {args.output}/")
    print("═" * 60)

    results = []
    for i, section in enumerate(sections):
        status_char = "⏳"
        print(f"{status_char} [{i+1}/{len(sections)}] {section['title'][:50]}...", end='', flush=True)

        result = await process_section(section, args.output, args.voice, args.rate)
        results.append(result)

        if result['status'] == 'done':
            size_kb = result['file_size'] / 1024
            print(f"\r✅ [{i+1}/{len(sections)}] {section['title'][:50]} → {result['filename']} ({size_kb:.0f} KB)")
        elif result['status'] == 'skipped':
            print(f"\r⏭️  [{i+1}/{len(sections)}] {section['title'][:50]} (skipped: {result['reason']})")
        else:
            print(f"\r❌ [{i+1}/{len(sections)}] {section['title'][:50]} (error: {result['reason']})")

    # Summary
    done = [r for r in results if r['status'] == 'done']
    skipped = [r for r in results if r['status'] == 'skipped']
    errors = [r for r in results if r['status'] == 'error']
    total_size = sum(r.get('file_size', 0) for r in done)

    print("\n" + "═" * 60)
    print(f"📊 Summary:")
    print(f"   ✅ Generated: {len(done)} files ({total_size/1024/1024:.1f} MB)")
    print(f"   ⏭️  Skipped:   {len(skipped)}")
    print(f"   ❌ Errors:    {len(errors)}")
    print(f"   📁 Output:    {os.path.abspath(args.output)}/")

    if done:
        print(f"\n🎧 Play all:  open {args.output}/")
        print(f"   Play one:  open {args.output}/{done[0]['filename']}")


if __name__ == '__main__':
    asyncio.run(main())
