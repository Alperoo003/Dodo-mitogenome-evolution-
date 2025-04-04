import os
from Bio import SeqIO

# 📁 Giriş ve çıkış klasörleri
input_folder = r"C:\Users\ASUS\Downloads\Dodo project\data.gb"
output_folder = os.path.join(input_folder, "extracted_flight_genes")
os.makedirs(output_folder, exist_ok=True)

# 🎯 Hedef genler
target_genes = {
    "coi": "COI",
    "cox1": "COI",
    "co1": "COI",
    "cytochrome c oxidase subunit i": "COI",

    "nd2": "ND2",
    "nad2": "ND2",
    "nad dehydrogenase subunit 2": "ND2",

    "nd4": "ND4",
    "nad4": "ND4",
    "nad dehydrogenase subunit 4": "ND4",

    "nd3": "ND3",
    "nad3": "ND3",
    "nad dehydrogenase subunit 3": "ND3",

    "coiii": "COIII",
    "cox3": "COIII",
    "cytochrome c oxidase subunit iii": "COIII"
    
}

# 🧬 Çıktı dosyaları oluştur
output_files = {
    "COI": open(os.path.join(output_folder, "COI_all_species.fasta"), "w"),
    "ND2": open(os.path.join(output_folder, "ND2_all_species.fasta"), "w"),
    "ND4": open(os.path.join(output_folder, "ND4_all_species.fasta"), "w"),
    "ND3": open(os.path.join(output_folder, "ND3_all_species.fasta"), "w"),
    "COIII": open(os.path.join(output_folder, "COIII_all_species.fasta"), "w")
}

# 🔁 GenBank dosyalarını gez
for filename in os.listdir(input_folder):
    if filename.endswith(".gb"):
        filepath = os.path.join(input_folder, filename)
        try:
            record = SeqIO.read(filepath, "genbank")
        except Exception as e:
            print(f"❌ {filename} okunamadı: {e}")
            continue

        species = record.annotations.get("organism", filename.replace(".gb", "")).replace(" ", "_")
        found_genes = set()

        for feature in record.features:
            if feature.type == "CDS":
                gene = feature.qualifiers.get("gene", [""])[0]
                product = feature.qualifiers.get("product", [""])[0]
                combined_info = f"{gene} {product}".lower()

                for key in target_genes:
                    gene_name = target_genes[key]
                    if key in combined_info and gene_name not in found_genes:
                        try:
                            seq = feature.extract(record.seq)
                            fasta_entry = f">{species}_{gene_name}\n{seq}\n"
                            output_files[gene_name].write(fasta_entry)
                            found_genes.add(gene_name)
                            print(f"✅ {gene_name} çıkarıldı: {species}")
                        except Exception as e:
                            print(f"⚠️ {gene_name} çıkarılamadı ({species}): {e}")
                        break

# 🔒 Dosyaları kapat
for f in output_files.values():
    f.close()

print("\n🎉 5 hedef gen (COI, ND2, ND4, ND3, COIII) başarıyla çıkarıldı!")
print("📂 Klasör: " + output_folder)






