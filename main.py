import subprocess
import os
 
BASE_INPUT_PATH = rf".\PetImages"
BASE_OUTPUT_PATH = rf".\PetImagesBeautified"
ANIMAL_DIRS = {1: "Dog", 2: "Cat"}

def beautify_image(input_image, output_image, exe_path="./realesrgan-ncnn-vulkan/realesrgan-ncnn-vulkan.exe", model_name="realesrgan-x4plus"):
    """
    Aplica melhoria de qualidade à imagem usando Real-ESRGAN.

    Args:
        input_image (str): Caminho para a imagem de entrada.
        output_image (str): Caminho para salvar a imagem de saída.
        exe_path (str): Caminho para o executável do Real-ESRGAN.
        model_name (str): Nome do modelo a ser utilizado na melhoria.

    Returns:
        None
    """
    command = [
        exe_path,
        "-i", input_image,
        "-o", output_image,
        "-n", model_name
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("Imagem gerada com sucesso!")

        if os.path.exists(output_image):
            os.startfile(output_image)

    except subprocess.CalledProcessError as e:
        print("Erro ao gerar imagem.")
        print("Erro:", e.stderr)

def get_animal_option():
    """
    Solicita ao usuário que selecione um tipo de animal (cachorro ou gato).

    Returns:
        int or None: Código do animal (1 para cachorro, 2 para gato), ou None se a entrada for inválida.
    """
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
    """
    Constrói os caminhos para a imagem de entrada e a imagem de saída com base no tipo de animal e nome da imagem.

    Args:
        animal_type (int): Código do animal (1 para cachorro, 2 para gato).
        image_name (str): Nome da imagem (sem extensão).

    Returns:
        tuple: Caminhos completos para a imagem de entrada e de saída.
    """    
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