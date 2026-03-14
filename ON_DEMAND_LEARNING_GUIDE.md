# On-Demand Learning: A Comprehensive Skills Guide

> **Author:** Do Minh Phung  
> **Date:** March 2026  
> **Context:** Built while creating *Lecture Notes -- Thuật Toán (Algorithms)*

---

## 1. What is On-Demand Learning?

**On-Demand Learning** (also called *Just-in-Time Learning*) is a self-directed approach where you learn exactly what you need, when you need it, at the depth required — rather than following a rigid, pre-defined curriculum.

### Core Philosophy

```
Traditional Learning:  Read everything → Hope to remember → Apply later
On-Demand Learning:    Identify need → Learn precisely → Apply immediately → Reinforce
```

### Why It Works

| Principle | Science Behind It |
|---|---|
| **Immediate application** | Encoding is stronger when knowledge is used right away (Transfer-Appropriate Processing) |
| **Active construction** | Building your own materials forces deeper processing (Generation Effect) |
| **Multi-modal encoding** | Combining text + visuals + code + video creates richer memory traces |
| **Self-testing** | Retrieval practice is the #1 evidence-based study technique (Roediger & Karpicke, 2006) |
| **Spaced encounters** | Revisiting material across sessions strengthens long-term retention |

---

## 2. The On-Demand Learning Workflow

### Phase 1: Identify & Scope
```
1. What specific problem am I solving? (e.g., "Understand Kruskal's algorithm for exam")
2. What do I already know? (e.g., "I know graphs, but not MST")
3. What's the minimum I need? (e.g., "Pseudocode + trace + proof sketch")
4. What's my deadline? (constrains depth)
```

### Phase 2: Source & Cross-Verify
```
1. Find 2-3 complementary sources:
   - Textbook (CLRS) → formal correctness
   - Video (YouTube) → visual intuition
   - Code (GitHub) → implementation details
2. Cross-verify between sources → catch errors & build confidence
3. Note any discrepancies → they reveal deep understanding
```

**Example from our project:**
- CLRS textbook → formal definitions and proofs
- YouTube videos (Michael Sambol) → visual step-by-step traces
- GitHub code (`kruskals.py`, `prims.py`) → runnable verification
- **Discovery:** The Kruskal and Prim videos use slightly different graphs! (10 vs 11 edges)

### Phase 3: Construct & Encode
```
1. Write it in YOUR words (not copy-paste)
2. Create visual representations (diagrams, tables, trace tables)
3. Add self-check questions ("Why does this step work?")
4. Build navigation aids (hyperlinks, table of contents, cross-references)
```

### Phase 4: Verify & Iterate
```
1. Run/compile your materials → catch errors early
2. Cross-check with original sources → ensure accuracy
3. Ask "Can I explain this without looking?" → Feynman Technique
4. Iterate on weak points → fill gaps
```

---

## 3. Skills Developed

### 3.1 Technical Skills

#### LaTeX Document Engineering
- **Structured documents** with sections, cross-references, and hyperlinks
- **TikZ diagrams** for graph visualization (nodes, edges, weights, colors)
- **Custom environments** using `tcolorbox` for pedagogical elements
- **PDF metadata** via `hypersetup` (hidden author, keywords for searchability)
- **Professional typesetting** with `listings` for pseudocode, `amsmath` for formulas

#### Algorithm Analysis
- **Trace tables** — manually stepping through an algorithm to verify correctness
- **Complexity analysis** — Big-O, Theta, Omega notation
- **Proof techniques** — Loop invariants, cut property, induction
- **Graph algorithms** — Kruskal, Prim, Dijkstra, Floyd-Warshall
- **Dynamic Programming** — Optimal substructure, overlapping subproblems

#### Source Verification
- Cross-referencing **textbook ↔ video ↔ code** to catch inconsistencies
- Running Python scripts mentally or physically to validate trace tables
- Identifying when sources use different inputs (the Kruskal/Prim graph discrepancy)

### 3.2 Meta-Learning Skills

#### Elaborative Interrogation
> "Why does Kruskal sort edges first?"  
> "Why does Dijkstra fail with negative weights?"

Asking "Why?" at every step forces you to understand causation, not just procedure.

#### The Feynman Technique
1. Pick a concept (e.g., "Cut Property of MST")
2. Explain it to an imaginary 12-year-old
3. Identify where you stumble → **that's where you don't understand**
4. Go back to source, re-learn, simplify

#### Active Recall vs. Passive Review
| ❌ Passive (Low retention) | ✅ Active (High retention) |
|---|---|
| Re-reading lecture notes | Closing the book, writing from memory |
| Watching a video again | Tracing the algorithm by hand |
| Highlighting text | Explaining to a friend |
| Copying pseudocode | Writing pseudocode from scratch |

#### Interleaving
Don't study one algorithm for 3 hours. Instead:
- 30 min Kruskal → 30 min Dijkstra → 30 min Kruskal again
- This forces your brain to **discriminate** between similar concepts

---

## 4. Document Architecture Patterns

### Pattern: Bilingual Headers
```
Section Title: Vietnamese Name -- English Name (Reference)
Example:      Chương 5: Thuật toán Tham lam -- Greedy Algorithms (CLRS Ch.16)
```
**Why:** Forces you to know both names. Exam might use either language.

### Pattern: Intuition → Formal → Example → Self-Check
```
1. 💡 Intuition box    → "Think of it like building the cheapest road network..."
2. 📐 Formal definition → "Given G=(V,E), find T⊆E such that..."
3. 📊 Worked example    → Step-by-step trace table with visual diagram
4. ❓ Self-check        → "Why can't Kruskal pick BE(3)?"
```

### Pattern: Side-by-Side Comparison
```
┌──────────────────┬──────────────────┐
│  Original Graph  │   MST Result     │
│  (all edges)     │  (selected edges)│
└──────────────────┴──────────────────┘
```
**Why:** Seeing before/after side-by-side makes the algorithm's effect immediately clear.

### Pattern: Numbered & Styled Code Blocks
```
┌─ Pseudocode 13: Kruskal's Algorithm ─┐
│ (grey background for visual contrast) │
│ Kruskal(G, w):                        │
│     sort edges by weight              │
│     for each edge (u,v):              │
│         if Find(u) ≠ Find(v):         │
│             Union(u, v)               │
└───────────────────────────────────────┘
```
**Why:** Numbered pseudocode blocks are easy to reference ("see Pseudocode 13") and grey backgrounds separate code from prose.

### Pattern: Clickable Navigation
```
Quick Reference Table:
  Sorting    → Ch.2 (click to jump)
  MST        → Ch.5 (click to jump)
  Dijkstra   → Ch.6 (click to jump)
```
**Why:** In a 35-page document, jumping directly to what you need saves precious exam time.

---

## 5. Tools & Technology Stack

| Tool | Purpose |
|---|---|
| **LaTeX (XeLaTeX)** | Document typesetting with Unicode support |
| **TikZ** | Graph and diagram visualization |
| **tcolorbox** | Styled boxes for intuition, pitfalls, pseudocode |
| **hyperref** | Internal links + PDF metadata |
| **listings** | Code/pseudocode formatting |
| **YouTube** | Visual walkthroughs of algorithms |
| **GitHub** | Reference implementations for verification |
| **AI Assistant** | Pair-programming partner for document construction |

---

## 6. Applying This to Other Subjects

### Step-by-Step Template

1. **Define scope** — What's on the exam? What chapters? What depth?
2. **Gather sources** — Textbook + video + code/examples (minimum 2 sources)
3. **Build skeleton** — Create section headers matching exam topics
4. **Fill with understanding, not text** — Every line should help you *understand*, not just *record*
5. **Add self-tests** — If you can't test yourself, you can't learn
6. **Cross-verify** — Run the code. Check the math. Compare sources.
7. **Navigate** — Add hyperlinks, table of contents, quick reference
8. **Iterate** — Each pass makes it better. Don't aim for perfect on first try.

### Subjects This Works Well For

| Subject | Source Types |
|---|---|
| **Algorithms/CS** | Textbook + YouTube + GitHub code |
| **Mathematics** | Textbook + worked examples + Wolfram Alpha verification |
| **Statistics** | Textbook + R/Python notebooks + real datasets |
| **Physics** | Textbook + PhET simulations + problem sets |
| **Languages** | Grammar rules + Anki flashcards + conversation practice |

---

## 7. Key Takeaways

> **The #1 mistake:** Thinking that *reading* = *learning*.  
> **The #1 fix:** Build something. Trace by hand. Explain out loud. Test yourself.

### The 3 Questions Test
After studying any topic, ask yourself:
1. **Can I explain it to someone who doesn't know it?** (Feynman)
2. **Can I trace through an example by hand?** (Procedural knowledge)
3. **Can I solve a NEW problem using this concept?** (Transfer)

If yes to all 3 → you've learned it.  
If no to any → go back to that specific gap.

---

## 8. Resources

### Evidence-Based Learning
- Roediger & Karpicke (2006) — *Test-Enhanced Learning*
- Dunlosky et al. (2013) — *Improving Students' Learning with Effective Techniques*
- Brown, Roediger & McDaniel (2014) — *Make It Stick*

### Algorithm-Specific
- Cormen et al. — *Introduction to Algorithms* (CLRS), 4th Edition
- Michael Sambol's YouTube Channel — Visual algorithm walkthroughs
- [github.com/msambol/dsa](https://github.com/msambol/dsa) — Python implementations

---

*This guide was developed through the process of building comprehensive algorithm lecture notes — a living proof that the best way to learn is to build.*
