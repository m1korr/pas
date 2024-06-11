import shutil

def copy_image_file():
    source_file = input("Podaj nazwę pliku graficznego: ")
    destination_file = "lab1zad1.png"
    try:
        shutil.copy(source_file, destination_file)
        print(f"Plik skopiowany do {destination_file}")
    except FileNotFoundError:
        print("Plik nie został znaleziony.")

if __name__ == "__main__":
    copy_image_file()
