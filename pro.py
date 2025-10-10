import os
import shutil

def rename_and_organize_modules(
    source_dir,
    target_dir,
    prefix="mod",
    file_types=(".mp4", ".mov", ".mkv"),
    dry_run=True
):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

    os.makedirs(target_dir, exist_ok=True)

    files = [f for f in os.listdir(source_dir) if f.endswith(file_types)]
    files.sort()

    print(f"Found {len(files)} module(s) to process.\n")

    for index, filename in enumerate(files, start=1):
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}{index:03}{name.strip().replace(' ', '')}{ext}"
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(target_dir, new_name)

        if dry_run:
            print(f"[DRY RUN] Would rename '{filename}' -> '{new_name}'")
        else:
            shutil.copy2(src_path, dst_path)
            print(f"Renamed and moved: '{filename}' -> '{new_name}'")

    if dry_run:
        print("\nDry run complete. Set dry_run=False to apply changes.")

# Example usage
if __name__ == "_main_":
    rename_and_organize_modules(
        source_dir="your_video_modules",
        target_dir="standard_modules",
        prefix="mod",
        file_types=(".mp4", ".mov"),
        dry_run=True  # Change to False to actually rename and move
    )