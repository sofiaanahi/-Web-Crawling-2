import os
import requests 
from bs4 import BeautifulSoup


# Crear la carpeta "imagenes" si no existe  
image_folder = "imagenes"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# URL del sitio web a  scraper
url = "https://www.nationalgeographic.com.es/animales/perros/"

# Hacer la solicitud GET a la URL
response = requests.get(url)

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas las etiquetas <img> y descargar las imagenes
for img in soup.find_all('img'):
    img_src = img.get('src')
    if img_src:
        try:
            # Verificar el formato de la imagen
            if any(img_src.endswith(ext) for ext in ['.png', '.jpg', '.webp']):
                # Descargar la imagen
                img_response = requests.get(img_src)
                img_filename =os.path.join(image_folder, os.path.basename(img_src))
                with open(img_filename, 'wb') as f:
                    f.write(img_response.content)
                print(f"imagen descargada: {img_filename}")
        except (requests.exceptions.RequestException, IOError) as e:
            print(f"Error al descargar la imagen: {img_src} - {e}")
            continue