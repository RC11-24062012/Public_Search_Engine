import os
import json

def merge_all_tags(data_dir="data", output_file="data/tags.json"):
    merged = {}
    total_count = 0

    for subdir in os.listdir(data_dir):
        subpath = os.path.join(data_dir, subdir)
        if os.path.isdir(subpath):
            for file in os.listdir(subpath):
                if file.endswith(".json"):
                    filepath = os.path.join(subpath, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            data = json.load(f)

                            if isinstance(data, dict) and "files" in data:
                                for relative_path, info in data["files"].items():
                                    # Add source field
                                    info["source"] = subdir

                                    # Normalize image path (preserve subpath)
                                    if info.get("type") == "image":
                                        normalized_path = relative_path.replace("\\", "/")
                                        info["image"] = f"data/{subdir}/{normalized_path}"
                                    else:
                                        normalized_path = relative_path.replace("\\", "/")

                                    # Build a unique key to avoid conflicts
                                    full_key = f"{subdir}/{normalized_path}"
                                    merged[full_key] = info
                                    total_count += 1

                                print(f"Combined: {filepath}")
                            else:
                                print(f"Skipped: {filepath} (missing 'files' field)")
                    except Exception as e:
                        print(f"Error: {filepath} - {e}")

    # Write merged result
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump({"files": merged}, out, indent=2, ensure_ascii=False)

    print(f"\nAll tags have been merged into {output_file}")
    print(f"Total merged entries: {total_count}")

if __name__ == "__main__":
    merge_all_tags()
