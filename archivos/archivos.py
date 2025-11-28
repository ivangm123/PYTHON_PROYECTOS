from pathlib import Path
from time import ctime


archivo = Path("archivos/prueba")
"""archivos.exists()
archivos.rename()
archivos.unlink()

print(archivo.stat())
"""

print("acceso", ctime(archivo.stat().st_atime))
print("modificacion", ctime(archivo.stat().st_mtime))
print("creacion", ctime(archivo.stat().st_ctime))
