import subprocess
import os
 
BASE_INPUT_PATH = r"C:\Repositories\computacao-grafica\PetImages"
BASE_OUTPUT_PATH = r"C:\Repositories\computacao-grafica\PetImagesBeautified"
ANIMAL_DIRS = {1: "Dog", 2: "Cat"}

def beautify_image(input_image, output_image, exe_path="./realesrgan-ncnn-vulkan/realesrgan-ncnn-vulkan.exe", model_name="realesrgan-x4plus"):
    command = [
        exe_path,
        "-i", input_image,
        "-o", output_image,
        "-n", model_name
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Imagem gerada com sucesso!")

        if os.path.exists(output_image):
            os.startfile(output_image)

    except subprocess.CalledProcessError as e:
        print("Erro ao gerar imagem.")
        print("Erro:", e.stderr)

def get_animal_option():
    print("Digite a opção do animal:")
    print("1. Cachorro")
    print("2. Gato")
    try:
        option = int(input(": "))
        if option not in ANIMAL_DIRS:
            print("Opção inválida.")
            return None
        return option
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None

def build_image_paths(animal_type, image_name):
    input_dir = os.path.join(BASE_INPUT_PATH, ANIMAL_DIRS[animal_type])
    output_dir = os.path.join(BASE_OUTPUT_PATH, ANIMAL_DIRS[animal_type] + "s")

    input_path = os.path.join(input_dir, f"{image_name}.jpg")
    output_path = os.path.join(output_dir, f"{image_name}_updated.jpg")
    return input_path, output_path

def main():
    option = get_animal_option()
    if option is None:
        return

    image_name = input("Digite o nome da imagem a ser remodelada:\n").strip()
    input_path, output_path = build_image_paths(option, image_name)

    beautify_image(input_path, output_path)

if __name__ == "__main__":
    main()