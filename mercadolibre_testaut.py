#Importanto libreriass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Configura el navegador con el Service correcto
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Esperas 
wait = WebDriverWait(driver, 10)

# Abrir la página de MercadoLibre
driver.get("https://www.mercadolibre.com")

# 4. Esperar que el botón de México esté disponible y hacer clic
mexico_link = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "México"))
)
mexico_link.click()


#	Search for the term “playstation 5”   - Buscar termino “playstation 5”

search_box = wait.until(
    EC.presence_of_element_located((By.NAME,"as_word")))

search_box.send_keys("Playstation 5")
search_box.send_keys(Keys.ENTER)

# Buscar el primer enlace "Nuevo"
nuevo_elemento = driver.find_element(By.PARTIAL_LINK_TEXT, "Nuevo")

# Hacer scroll hacia él 
driver.execute_script("arguments[0].scrollIntoView(true);", nuevo_elemento)

# Forzar clic con JavaScript
driver.execute_script("arguments[0].click();", nuevo_elemento)

# Select location
cdmx_location = driver.find_element(By.PARTIAL_LINK_TEXT, "Estado De México")

# Hacer scroll hacia él (opcional pero recomendado)
driver.execute_script("arguments[0].scrollIntoView(true);", cdmx_location)

# Forzar clic con JavaScript
driver.execute_script("arguments[0].click();", cdmx_location)
#  Pausar para que veas el resultado

# Espera y clic en el botón de "Más relevantes"

orden_menu = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "andes-dropdown__trigger"))
)
orden_menu.click()

time.sleep(1)  # Darle tiempo a que aparezca el menú

opciones = driver.find_elements(By.XPATH, "//li[@role='option']//span")
for o in opciones:
    print("🔹", o.text)

opcion_mayor_precio = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Mayor precio')]"))
)
driver.execute_script("arguments[0].click();", opcion_mayor_precio)


# Esperar que los productos estén presentes
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.poly-card--CORE")))

# Obtener los productos
productos = driver.find_elements(By.CSS_SELECTOR, "div.poly-card--CORE")[:5]

# Iterar y extraer nombre y precio
for i, producto in enumerate(productos, 1):
    try:
        nombre = producto.find_element(By.CLASS_NAME, "poly-component__title").text
        precio = producto.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
        print(f"{i}. {nombre} - ${precio}")
    except Exception as e:
        print(f"{i}. ⚠️ Error al obtener producto: {e}")


input("✅ Elemento encontrado . Presiona Enter para cerrar...")
driver.quit()