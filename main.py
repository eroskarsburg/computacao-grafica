import os
from PIL import Image, ImageEnhance, ImageFilter

# Função para embelezar a imagem
def beautify_image(image_path, output_folder, upscale_factor=4, sharpness_factor=2, blur_radius=1):
    # Abrir a imagem
    img = Image.open(image_path)

    # Redimensionar a imagem
    width, height = img.size
    new_width = int(width * upscale_factor)
    new_height = int(height * upscale_factor)
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)

    # Melhorar a nitidez
    enhancer = ImageEnhance.Sharpness(img_resized)
    img_sharpened = enhancer.enhance(sharpness_factor)

    # Aplicar suavização (filtro gaussiano)
    img_smooth = img_sharpened.filter(ImageFilter.GaussianBlur(blur_radius))

    # Verificar se a pasta de saída existe, se não, criar
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Criar o caminho de saída
    output_path = os.path.join(output_folder, "beautified_image_smoothed.jpg")

    # Salvar a imagem aprimorada
    img_smooth.save(output_path)
    print(f"Imagem suavizada e salva em: {output_path}")

# Bloco principal para obter entrada do usuário e processar a imagem
if __name__ == "__main__":
    # Caminho da imagem original
    image_path = "C:/Users/Eros/repos/computacao-grafica/PetImages/Cat/40.jpg"

    # Verificar se o arquivo existe
    if not os.path.exists(image_path):
        print("O caminho especificado da imagem não existe. Verifique e tente novamente.")
    else:
        # Caminho da pasta de saída onde a imagem será salva
        output_folder = "C:/Users/Eros/repos/computacao-grafica/PetImagesBeautified/Cats"

        # Embelezar a imagem e criar a versão suavizada
        beautify_image(image_path, output_folder)

        # Opcional: Exibir a imagem para confirmar
        img = Image.open(os.path.join(output_folder, "beautified_image_smoothed.jpg"))
        img.show()
