"""
File Organizer

Description:
Organizes files in a selected folder into categorized subfolders
based on file extension.

Author: Nixon Bone
Version: 1.0
"""

from pathlib import Path
import shutil


FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Documents": {".doc", ".docx", ".txt", ".rtf"},
    "PDFs": {".pdf"},
    "Spreadsheets": {".csv", ".xls", ".xlsx"},
    "Presentations": {".ppt", ".pptx"},
    "Archives": {".zip", ".rar", ".7z"},
}


def get_category(file_extension: str) -> str:
    """Return the category name for a file extension."""

    extension = file_extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def organize_files(folder_path: Path) -> tuple[int, int]:
    """
    Move files into categorized folders.

    Returns:
        A tuple containing the number of files moved and skipped.
    """

    moved_count = 0
    skipped_count = 0

    for item in folder_path.iterdir():
        if not item.is_file():
            continue

        category = get_category(item.suffix)
        destination_folder = folder_path / category
        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / item.name

        if destination_file.exists():
            print(f"Skipped: {item.name} already exists in {category}.")
            skipped_count += 1
            continue

        try:
            shutil.move(str(item), str(destination_file))
            print(f"Moved: {item.name} -> {category}")
            moved_count += 1
        except OSError as error:
            print(f"Error moving {item.name}: {error}")
            skipped_count += 1

    return moved_count, skipped_count


def main() -> None:
    """Run the file organizer."""

    print("=" * 45)
    print(" File Organizer")
    print("=" * 45)

    folder_input = input(
        "Enter the full path of the folder to organize: "
    ).strip().strip('"')

    folder_path = Path(folder_input).expanduser()

    if not folder_path.exists():
        print("\nError: The folder does not exist.")
        return

    if not folder_path.is_dir():
        print("\nError: The path is not a folder.")
        return

    moved_count, skipped_count = organize_files(folder_path)

    print("\nOrganization Complete")
    print("-" * 45)
    print(f"Files moved   : {moved_count}")
    print(f"Files skipped : {skipped_count}")


if __name__ == "__main__":
    main()
