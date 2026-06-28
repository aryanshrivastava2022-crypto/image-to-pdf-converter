from PIL import Image

print("🖼️➡️📄 Image to PDF Converter")

image_files = input("Enter image filenames separated by commas: ").split(",")

try:
    images = []

    for file in image_files:
        img = Image.open(file.strip()).convert("RGB")
        images.append(img)

    output_file = "output.pdf"

    images[0].save(
        output_file,
        save_all=True,
        append_images=images[1:]
    )

    print(f"✅ PDF created successfully!")
    print(f"Saved as: {output_file}")

except FileNotFoundError:
    print("❌ One or more image files were not found.")
except Exception as e:
    print("Error:", e)
