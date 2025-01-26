import os

folders_to_filter = ["37_rosamaria_right"]

import os

def rename_images_in_folders(directory):
    """
    Renombra las imágenes en cada carpeta dentro de un directorio principal,
    concatenando el nombre de la carpeta y un correlativo.

    Args:
        directory (str): Ruta del directorio principal donde están las carpetas.
    """
    # Verifica si el directorio existe
    if not os.path.exists(directory):
        print(f"El directorio {directory} no existe.")
        return

    # Itera sobre las carpetas en el directorio principal
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)

        # Verifica que sea un directorio
        if os.path.isdir(folder_path):
            # Lista de archivos en la carpeta
            files = os.listdir(folder_path)
            
            # Filtrar solo archivos de imagen
            image_files = [file for file in files if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]

            # Renombrar los archivos a nombres temporales para evitar conflictos
            temp_files = []
            for index, file in enumerate(sorted(image_files), start=1):
                old_file_path = os.path.join(folder_path, file)
                extension = os.path.splitext(file)[1]
                temp_file_name = f"temp_{index}{extension}"
                temp_file_path = os.path.join(folder_path, temp_file_name)

                os.rename(old_file_path, temp_file_path)
                temp_files.append(temp_file_path)

            # Renombrar los archivos temporales al nombre final
            for index, temp_file_path in enumerate(temp_files, start=1):
                extension = os.path.splitext(temp_file_path)[1]
                new_file_name = f"{folder}_{index}{extension}"
                new_file_path = os.path.join(folder_path, new_file_name)

                os.rename(temp_file_path, new_file_path)
                print(f"Renombrado temp: {temp_file_path} -> {new_file_path}")

            print(f"\n{folder} -> {len(temp_files)} imágenes renombradas\n\n")

# Ejemplo de uso
ruta_principal = "/Users/gipo/Downloads/new_feet_images"
rename_images_in_folders(ruta_principal)