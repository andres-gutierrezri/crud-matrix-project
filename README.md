
# Proyecto: Generador de Matriz CRUD (CSV, Markdown y Excel) para MySQL Workbench 8.0 CE

Este proyecto en Python genera automáticamente la matriz **CRUD** a partir del *schema* indicado y produce **tres** salidas:
* `matriz_crud.csv`
* `matriz_crud.md`
* `matriz_crud.xlsx`

El script se conecta a MySQL utilizando `mysql-connector-python`, construye la tabla con **pandas** y la exporta empleando `DataFrame.to_csv`, `DataFrame.to_markdown` y `DataFrame.to_excel` (motor *openpyxl*).

## Requisitos
| Software | Versión recomendada |
|----------|--------------------|
| Python   | 3.10 o superior |
| MySQL Server | 8.0 |
| MySQL Workbench | 8.0 CE |
| Dependencias de Python | Ver `requirements.txt` |

## Instalación

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso básico

```bash
python crud_matrix.py --host localhost --port 3306 --user root --password 'clave' --database 'database_name' --output matriz_crud.csv
```

> Si omite `--output`, el nombre por defecto es **matriz_crud.csv**.  
> El script generará automáticamente los archivos `.md` y `.xlsx` con el mismo nombre base.

## Estructura interna del script
1. Se conecta a MySQL mediante `mysql.connector.connect`.
2. Consulta `information_schema.tables` para obtener las tablas del esquema.
3. Crea un `pandas.DataFrame` con columnas **Create, Read, Update, Delete** inicializadas en “X”.
4. Exporta a CSV, Markdown y Excel (`openpyxl`).

## Control de versiones

```bash
git init
git add .
git commit -m "Versión inicial con salida Excel"
git remote add origin https://github.com/USUARIO/crud_matrix_excel.git
git push -u origin main
```

Para GitLab sustituya la URL de *remote*.

---

© 2025 · Licencia MIT
