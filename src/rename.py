import os

def main():
    directory = str(input("Digite o diretório: "))
    
    for filename in os.listdir(directory):
        old_file = os.path.join(directory, filename)

        new_filename = filename.replace(" ROUBO DE VEICULOS", "")

        new_file = os.path.join(directory, new_filename)
        
        os.rename(old_file, new_file)

if __name__ == "__main__":
    main()
