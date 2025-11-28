from pathlib import Path

path = Path("hola-mundo/mi-archivo.txt")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()

)

p = path.with_name("chanchito.txt")
print(p)
p = path.with_suffix(".md")
print(p)
p = path.with_stem("feliz")
print(p)
