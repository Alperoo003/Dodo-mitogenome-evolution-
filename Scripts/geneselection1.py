import os
from Bio import SeqIO

# Input folder: the folder containing all .gb files
input_folder = r"C:\Users\ASUS\Downloads\Dodo project\data"
output_folder = os.path.join(input_folder, "extracted_genes")
os.makedirs(output_folder, exist_ok=True)

# Target genes
target_genes = {
    "atp6": "ATP6",
    "atp8": "ATP8",
    "cytb": "CYTB",
    "cytochrome b": "CYTB",
    "cytochrome_b": "CYTB",
    "atp synthase f0 subunit 8": "ATP8",  # 💡 Added
    "atp synthase f0 subunit 6": "ATP6"   # 💡 Can be added
}

# Merge all species for each gene into the same file
output_files = {
    "ATP6": open(os.path.join(output_folder, "ATP6_all_species.fasta"), "w"),
    "ATP8": open(os.path.join(output_folder, "ATP8_all_species.fasta"), "w"),
    "CYTB": open(os.path.join(output_folder, "CYTB_all_species.fasta"), "w")
}

for filename in os.listdir(input_folder):
    if filename.endswith(".gb"):
        filepath = os.path.join(input_folder, filename)
        try:
            record = SeqIO.read(filepath, "genbank")
        except Exception as e:
            print(f"❌ Failed to read {filename}: {e}")
            continue

        species = record.annotations.get("organism", filename.replace(".gb", "")).replace(" ", "_")

        for feature in record.features:
            if feature.type == "CDS":
                gene = feature.qualifiers.get("gene", [""])[0].lower()
                product = feature.qualifiers.get("product", [""])[0].lower()

                for key in target_genes:
                    if key in gene or key in product:
                        gene_name = target_genes[key]
                        try:
                            seq = feature.extract(record.seq)
                            fasta_entry = f">{species}_{gene_name}\n{seq}\n"
                            output_files[gene_name].write(fasta_entry)
                            print(f"✅ Extracted {gene_name}: {species}")
                        except Exception as e:
                            print(f"⚠️ Failed to extract {gene_name} ({species}): {e}")
                        break

# Close output files
for f in output_files.values():
    f.close()

print("\n🎉 Gene extraction completed for all species! FASTA files are saved at:")
print(output_folder)


