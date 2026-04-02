from PIL import Image

def decode_image(stego_path, output_path):
    stego = Image.open(stego_path).convert("RGB")
    pixels = stego.load()

    width, height = stego.size
    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r_new = (r & 1) * 255
            g_new = (g & 1) * 255
            b_new = (b & 1) * 255

            new_pixels[x, y] = (r_new, g_new, b_new)

    new_image.save(output_path)
    print("Gambar berhasil diambil!")

decode_image("output secret.png", "recovered secret.png")