import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

def copy_file(file_path, dest_dir):
    """Копирует файл в целевую директорию, создавая поддиректорию по расширению."""
    if not os.path.isfile(file_path):
        return

    ext = os.path.splitext(file_path)[1][1:].lower()  # Получаем расширение без точки
    if not ext:  # Пропускаем файлы без расширения
        ext = "unknown"

    target_folder = os.path.join(dest_dir, ext)
    os.makedirs(target_folder, exist_ok=True)

    try:
        shutil.copy(file_path, target_folder)
        print(f"✔ Копирован: {file_path} → {target_folder}")
    except Exception as e:
        print(f"❌ Ошибка копирования {file_path}: {e}")

def process_directory(source_dir, dest_dir):
    """Рекурсивно проходит по всем файлам в папке и копирует их."""
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(copy_file, file_path, dest_dir)

def main():
    parser = argparse.ArgumentParser(description="Сортировка файлов по расширениям.")
    parser.add_argument("source", help="Путь к исходной директории")
    parser.add_argument("destination", nargs="?", default="dist", help="Путь к целевой директории (по умолчанию: dist)")

    args = parser.parse_args()

    source_dir = os.path.abspath(args.source)
    dest_dir = os.path.abspath(args.destination)

    if not os.path.exists(source_dir):
        print(f"❌ Ошибка: директория {source_dir} не найдена!")
        return

    os.makedirs(dest_dir, exist_ok=True)
    process_directory(source_dir, dest_dir)
    print(f"✅ Файлы успешно отсортированы в {dest_dir}")

if __name__ == "__main__":
    main()

