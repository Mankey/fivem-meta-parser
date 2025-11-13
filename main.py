import os
import re

def find_vehicle_models(base_path):
    model_pattern = re.compile(r'<modelName>\s*(.*?)\s*</modelName>', re.IGNORECASE)
    model_names = set()  # use a set to avoid duplicates

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.lower() == 'vehicles.meta':
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                models = model_pattern.findall(content)
                for model in models:
                    model_names.add(model.strip())

    return sorted(model_names)


if __name__ == "__main__":
    base_directory = input("Enter the path to search for vehicles.meta: ").strip()
    results = find_vehicle_models(base_directory)

    output_file = "vehicle_models.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for model in results:
            f.write(f"{model}\n")

    print(f"\n✅ {len(results)} model names saved to {output_file}")
