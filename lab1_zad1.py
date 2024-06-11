import shutil

def copy_text_file():
    source_file = input("Podaj nazwę pliku tekstowego: ")
    destination_file = "lab1zad1.txt"
    try:
        shutil.copy(source_file, destination_file)
        print(f"Plik skopiowany do {destination_file}")
    except FileNotFoundError:
        print("Plik nie został znaleziony.")

if __name__ == "__main__":
    copy_text_file()
