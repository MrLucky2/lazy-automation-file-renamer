import argparse
from pathlib import Path


def rename_files(folder: Path, prefix: str, start: int, dry_run: bool) -> None:
    """Rename all files in a folder to prefix001.ext, prefix002.ext, etc."""
    if not folder.exists() or not folder.is_dir():
        print(f"Error: {folder} is not a valid folder.")
        return

    files = sorted([p for p in folder.iterdir() if p.is_file()])

    if not files:
        print("No files found in the folder.")
        return

    print(f"{'DRY RUN – ' if dry_run else ''}Renaming files in: {folder}")
    counter = start

    for file_path in files:
        new_name = f"{prefix}{counter:03d}{file_path.suffix.lower()}"
        new_path = file_path.with_name(new_name)

        print(f"{file_path.name}  →  {new_name}")

        if not dry_run:
            file_path.rename(new_path)

        counter += 1

    print("Done!")


def main():
    parser = argparse.ArgumentParser(
        description="Batch rename files in a folder with a given prefix."
    )
    parser.add_argument(
        "folder",
        type=str,
        help="Path to the folder containing the files to rename",
    )
    parser.add_argument(
        "--prefix",
        "-p",
        type=str,
        default="file_",
        help="Prefix for new file names (default: file_)",
    )
    parser.add_argument(
        "--start",
        "-s",
        type=int,
        default=1,
        help="Starting number for the sequence (default: 1)",
    )
    parser.add_argument(
        "--dry-run",
        "-d",
        action="store_true",
        help="Show what would be renamed without actually renaming",
    )

    args = parser.parse_args()

    folder_path = Path(args.folder).expanduser().resolve()
    rename_files(folder_path, args.prefix, args.start, args.dry_run)


if __name__ == "__main__":
    main()
