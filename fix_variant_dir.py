import click
import json
from pathlib import Path

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

@click.command()
@click.argument('input_json_path', type=click.Path(exists=True))
@click.argument('output_json_path', type=click.Path())
def process_files(input_json_path, output_json_path):
    # Load input JSON
    data = load_json(input_json_path)
    
    # Prepare the output structure
    output_data = {
        "files": [],
        "gcovr/format_version": data["gcovr/format_version"]
    }
    
    # Dictionary to store file paths and their combined lines
    combined_files = {}

    # Iterate through the files in the input
    for file_entry in data["files"]:
        file_path = file_entry["file"]
        lines = file_entry["lines"]
        
        # Find the directory of the current file
        file_dir = Path(file_path).parent
        
        # Check for "variant_dir.json" in the directory
        variant_file_path = file_dir / "variant_dir.txt"
        
        if variant_file_path.exists():
            # Load the variant_dir.json to get the mapping
            variant_data = load_json(variant_file_path)
            original_path = variant_data["src"]
            
            # Adjust the file path to reflect the original path
            new_file_path = str(Path(original_path) / Path(file_path).relative_to(file_dir))
            
            # If this original path already exists in the dictionary, combine lines
            if original_path in combined_files:
                combined_files[original_path]["lines"].extend(lines)
            else:
                combined_files[original_path] = {
                    "file": new_file_path,
                    "lines": lines
                }
        else:
            # If no variant_dir.json, retain the original path
            if file_path not in combined_files:
                combined_files[file_path] = file_entry

    # Save combined files to the output JSON
    output_data["files"] = list(combined_files.values())
    save_json(output_json_path, output_data)

    click.echo(f"Processed files have been saved to {output_json_path}")

if __name__ == "__main__":
    process_files()
