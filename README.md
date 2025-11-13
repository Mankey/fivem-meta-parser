# 🧩 FiveM Vehicle Model Extractor

I got tired of searching through all the `vehicles.meta` files just to find spawn codes — so I made this tool.  
This script automatically scans all your FiveM resources, finds every `<modelName>` tag, and saves them to a clean text file.

---

## 🚀 What It Does
- Recursively searches through all folders for `vehicles.meta` files  
- Extracts every `<modelName>` (spawn code)  
- Outputs all codes into `vehicle_models.txt`  
- Removes duplicates and trims any extra spaces  
