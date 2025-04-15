import subprocess

def beautify_image(input_image, output_image, exe_path="./realesrgan-ncnn-vulkan/realesrgan-ncnn-vulkan.exe", model_name="realesrgan-x4plus"):
    command = [
        exe_path,
        "-i", input_image,
        "-o", output_image,
        "-n", model_name
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)

    except subprocess.CalledProcessError as e:
        print("Erro ao gerar imagem.")
        print("Erro:", e.stderr)

def main():
    nome = "124"
    input_path = f"C:\Repositories\computacao-grafica\PetImages\Dog\{nome}.jpg"
    output_path = f"C:\Repositories\computacao-grafica\PetImagesBeautified\Dogs\{nome}_novo.jpg"
    beautify_image(input_path, output_path)

if __name__ == "__main__":
    main()