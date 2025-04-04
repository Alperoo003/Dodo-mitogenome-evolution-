# Dodo-mitogenome-evolution-
Mitochondrial gene evolution analysis of the dodo (Raphus cucullatus) and related species.
# 🧬 Dodo Mitochondrial Gene Evolution Project

## 📌 Overview

This project investigates the evolutionary patterns of mitochondrial genes in the extinct *Raphus cucullatus* (dodo) and compares them to a selected set of extant avian species. The goal was to test whether dodo-specific molecular changes, particularly in mitochondrial energy-related genes, reveal adaptations or relaxed constraints associated with flightlessness.

Our analysis focused on:
- Diversifying selection in protein-coding mitochondrial genes
- Structural and functional predictions for key amino acid substitutions
- Comparative phylogenetic patterns across flightless and volant birds

---

## 🔍 Objectives

- Extract protein-coding mitochondrial genes from GenBank files using Biopython.
- Align sequences (codon-based) and construct phylogenetic trees with MEGA X.
- Identify sites under positive selection using FEL, MEME, and other models via DataMonkey.
- Assess structural impact of amino acid substitutions with AlphaFold, PyMOL, SIFT, and PROVEAN.
- Explore implications of mitochondrial sequence variation for energy metabolism and flight adaptation.

---

## 🐦 Species Included

- **Raphus cucullatus** (Dodo)
- *Caloenas nicobarica* (Nicobar pigeon)
- *Columba livia* (Rock pigeon)
- *Streptopelia decaocto* (Eurasian collared dove)
- *Gallus gallus* (Chicken)
- *Apteryx owenii* (Little spotted kiwi)
- *Dromaius novaehollandiae* (Emu)
- *Struthio camelus* (Ostrich)

---

## 🧪 Genes Analyzed

| Gene   | Selection Sites Found | Notes |
|--------|------------------------|-------|
| ATP8   | Yes (codon 42, dodo-specific) | Found a Proline substitution unique to dodo |
| CYTB   | Yes (334, 354, 361, 305) | Various substitutions in Nicobar pigeon and global tree |
| ATP6   | No | Highly conserved |
| ND2    | No | No positive selection |
| ND3    | No | Dodo clusters separately in phylogeny |
| ND5    | — | Excluded due to alignment issues |
| COI    | No | Analyzed for structural divergence |
| COIII   | No | (Optional inclusion) |

---

## 📊 Tools Used

- **Python / Biopython**: GenBank parsing and gene extraction scripts
- **MEGA X**: MUSCLE codon alignment and NJ phylogenetic trees (bootstrap 500)
- **DataMonkey**: Selection analysis (FEL, MEME,)
- **AlphaFold + PyMOL**: Protein modeling and visualization
- **SIFT / PROVEAN**: Mutation impact prediction

---

## 🧬 Key Results

- **ATP8 codon 42**: Dodo has Proline; others mostly have Threonine or Leucine  
  → SIFT: Tolerated (score: 0.17)  
  → PROVEAN: Neutral  
  → AlphaFold: Located in flexible/disordered region (plDDT < 70)

- **CYTB codons 334, 354, 361**: Multiple substitutions observed in *Caloenas nicobarica*  
  → May indicate mild divergence within Columbidae

- No strong evidence of mitochondrial adaptation was found, but the patterns suggest:
  - Either a relaxed selection in dodo
  - Or adaptation signatures elsewhere, such as nuclear-mitochondrial interactions
