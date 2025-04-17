import subprocess
import os
 
def beautify_image(input_image, output_image, exe_path="./realesrgan-ncnn-vulkan/realesrgan-ncnn-vulkan.exe", model_name="realesrgan-x4plus"):
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
 
def main():
    option = int(input("Digite a opção do animal.\n1. Cachorro\n2. Gato\n: "))
    if option != 1 and option != 2:
        return print("Opção inválida.")
 
    animal_name = input("Digite a o nome da imagem a ser remodelada:\n")
    outputname = animal_name + "_updated"
 
    input_path = f"C:\Repositories\computacao-grafica\PetImages\Cat\{animal_name}.jpg"
    output_path = f"C:\Repositories\computacao-grafica\PetImagesBeautified\Cats\{outputname}.jpg"
    if option == 1:
        input_path = f"C:\Repositories\computacao-grafica\PetImages\Dog\{animal_name}.jpg"
        output_path = f"C:\Repositories\computacao-grafica\PetImagesBeautified\Dogs\{outputname}.jpg"
 
    beautify_image(input_path, output_path)
 
if __name__ == "__main__":
    main()