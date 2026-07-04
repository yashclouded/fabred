from fetcher import clone_repo
from extractor import get_readme, get_all_files, read_file


repo = input("GitHub URL: ").strip()

repo_path = clone_repo(repo)

print("Repository cloned successfully.\n")

readme = get_readme(repo_path)

if readme:
    print("=" * 50)
    print("README")
    print("=" * 50)
    print(readme[:1000])
else:
    print("No README found.")

print("\n")


files = get_all_files(repo_path)

print(f"Found {len(files)} files.\n")

for file in files:
    print(file)

print("\n")


print("=" * 50)
print("Python Files")
print("=" * 50)

for file in files:

    if file.endswith(".py"):
        print("\n", file)

        code = read_file(file)

        print(code[:500])