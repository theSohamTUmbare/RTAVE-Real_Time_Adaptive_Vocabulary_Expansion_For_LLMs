# Step 1: few lines of the raw file to understand the format
input_file = "data\gene_data\gene_alias_description.txt"

with open(input_file, "r", encoding="utf-8") as f:
    for i in range(5):  # first 5 lines
        line = f.readline().strip()
        print(f"Line {i+1}:", line)


# Step 2: Checking if all lines have exactly 3 parts (ID, alias, description)
bad_lines = []
with open(input_file, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        parts = line.strip().split("\t")
        if len(parts) != 3:
            bad_lines.append((idx, line.strip()))

print(f"Total malformed lines: {len(bad_lines)}")
if bad_lines:
    print("Sample malformed lines:")
    for idx, l in bad_lines[:3]:  # first 3 bad lines
        print(f"Line {idx}: {l}")


# Step 3: Writing the clean version to output file
output_file = "gene_input_text.tsv"

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        parts = line.strip().split("\t")
        if len(parts) != 3:
            continue  # Skip malformed lines

        gene_id, alias, description = parts
        combined_text = f"{alias}. {description}"
        fout.write(f"{gene_id}\t{combined_text}\n")

print(f"✅ Processed gene descriptions written to {output_file}")


with open(output_file, "r", encoding="utf-8") as f:
    for i in range(5):
        print(f.readline().strip())


## finally function to get the description and alias of the gene from the processed  file 
def get_gene_text(tsv_path: str, gene_id: str) -> str:
    with open(tsv_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) != 2:
                continue  # skip 
            current_gene_id, gene_text = parts
            if current_gene_id == gene_id:
                return gene_text
    return None  # Gene ID not found
