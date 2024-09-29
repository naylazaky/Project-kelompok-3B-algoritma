from PIL import Image, ImageOps
import os

def flip_image(image_path, output_path, direction='horizontal'):
    """
    Memantulkan gambar baik secara horizontal atau vertikal.

    :param image_path: Path ke file gambar yang ingin dipantulkan.
    :param output_path: Path untuk menyimpan gambar yang dipantulkan.
    :param direction: Arah pemantulan ('horizontal' atau 'vertical').
    """
    # Buka gambar
    image = Image.open(image_path)

    # Pemantulan gambar sesuai arah
    if direction == 'horizontal':
        flipped_image = ImageOps.mirror(image)
    elif direction == 'vertical':
        flipped_image = ImageOps.flip(image)
    else:
        raise ValueError("Direction must be 'horizontal' or 'vertical'.")

    # Simpan gambar yang dipantulkan
    flipped_image.save(output_path)
    print(f"Gambar berhasil dipantulkan dan disimpan di: {output_path}")

def main():
    # Input manual dari pengguna
    input_image_path = input("Masukkan Gambar (Contoh: C:/Users/LENOVO/Downloads/jpg): ")
    output_image_path_horizontal = input("Masukkan nama output horizontal (Contoh: C:/Users/LENOVO/Downloads/jpg): ")
    output_image_path_vertical = input("Masukkan nama output vertikal (Contoh: C:/Users/LENOVO/Downloads/jpg): ")
    
    # Memanggil fungsi untuk memantulkan gambar secara horizontal  
    flip_image(input_image_path, output_image_path_horizontal, direction='horizontal')

    # Memanggil fungsi untuk memantulkan gambar secara vertikal
    flip_image(input_image_path, output_image_path_vertical, direction='vertical')

if __name__ == "__main__":
    main()
