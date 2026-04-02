from PIL import Image

def encode_image(cover_path, secret_path, output_path):
    cover = Image.open(cover_path).convert("RGB")
    secret = Image.open(secret_path).convert("RGB")

    cover_pixels = cover.load()
    secret_pixels = secret.load()

    width, height = cover.size
    secret = secret.resize((width, height))
    secret_pixels = secret.load()

    for x in range(width):
        for y in range(height):
            r1, g1, b1 = cover_pixels[x, y]
            r2, g2, b2 = secret_pixels[x, y]

            # ambil 4 bit dari masing-masing
            r = (r1 & 0xF0) | (r2 >> 4)
            g = (g1 & 0xF0) | (g2 >> 4)
            b = (b1 & 0xF0) | (b2 >> 4)

            cover_pixels[x, y] = (r, g, b)

    cover.save(output_path)
    print("Gambar berhasil disembunyikan!")
    
encode_image("wadah.png", "secret.png", "output.png")