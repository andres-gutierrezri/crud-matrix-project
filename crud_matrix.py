#!/usr/bin/env python3
"""Generador automático de matriz CRUD con salidas CSV, Markdown y Excel."""

import argparse
import sys
from pathlib import Path

import mysql.connector
import pandas as pd


def build_matrix(cursor, database):
    cursor.execute(
        """SELECT table_name
           FROM information_schema.tables
           WHERE table_schema = %s
           ORDER BY table_name;""",
        (database,),
    )
    tables = [row[0] for row in cursor.fetchall()]
    data = {
        "Tabla": tables,
        "Create": ["X"] * len(tables),
        "Read": ["X"] * len(tables),
        "Update": ["X"] * len(tables),
        "Delete": ["X"] * len(tables),
    }
    return pd.DataFrame(data)


def main():
    parser = argparse.ArgumentParser(
        description="Genera una matriz CRUD y la exporta en CSV, Markdown y Excel."
    )
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=3306)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True) # NOTA ACLARATORIA: Si la Base de Datos NO tiene contraseña cambiar required=True por default="" | parser.add_argument("--password", default="")
    parser.add_argument("--database", required=True)
    parser.add_argument(
        "--output",
        default="matriz_crud.csv",
        help="Ruta del archivo CSV de salida (por defecto matriz_crud.csv)",
    )
    args = parser.parse_args()

    try:
        cnx = mysql.connector.connect(
            host=args.host,
            port=args.port,
            user=args.user,
            password=args.password,
            database=args.database,
        )
    except mysql.connector.Error as err:
        print(f"[ERROR] Conexión fallida: {err}")
        sys.exit(1)

    cursor = cnx.cursor()
    df = build_matrix(cursor, args.database)

    # Rutas de salida
    csv_path = Path(args.output)
    md_path = csv_path.with_suffix(".md")
    xlsx_path = csv_path.with_suffix(".xlsx")

    # Exportaciones
    df.to_csv(csv_path, index=False)
    df.to_markdown(md_path, index=False)
    df.to_excel(xlsx_path, index=False, engine="openpyxl")

    print(f"Matriz CRUD generada: {csv_path} {md_path} {xlsx_path}")

    cnx.close()


if __name__ == "__main__":
    main()
