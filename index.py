from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()

bot.get("https://www.viajesexito.com/")
time.sleep(8)

try:
    iframe = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[contains(@class, "bhr-iframe-holder--custom")]'))
    )
    bot.switch_to.frame(iframe)

    close_button = WebDriverWait(bot, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]')) 
    )
    close_button.click()

    bot.switch_to.default_content()
except Exception as e:
    print("No se pudo encontrar el iframe o el botón de cierre:", e)

paquetes = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]')
time.sleep(2)
paquetes.click()
time.sleep(2)

origen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]')
origen.click()
time.sleep(1)

inputOrigen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
time.sleep(1)
inputOrigen.send_keys('bogota')

dorado = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li[2]')
time.sleep(1)
dorado.click()
time.sleep(1)

destino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]')
time.sleep(1)
destino.click()
time.sleep(1)

inputDestino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
time.sleep(1)
inputDestino.send_keys('punta cana')

puntaCana = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li')
time.sleep(1)
puntaCana.click()
time.sleep(1)

fecha = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div')
time.sleep(1)
fecha.click()
time.sleep(1)

diaSalida = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[4]/div[2]')
time.sleep(1)
diaSalida.click()
time.sleep(1)

diaRegreso = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]')
time.sleep(1)
diaRegreso.click()
time.sleep(1)

botonAceptar = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[2]/button[2]')
time.sleep(1)
botonAceptar.click()
time.sleep(1)

habitaciones = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div')
time.sleep(1)
habitaciones.click()
time.sleep(1)

agregarHabitacion = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
time.sleep(1)
agregarHabitacion.click()
time.sleep(1)

aceptarHabitaciones = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
time.sleep(1)
aceptarHabitaciones.click()
time.sleep(1)

buscar = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]')
time.sleep(1)
buscar.click()
time.sleep(20)

original_window = bot.current_window_handle

all_windows = bot.window_handles

for window in all_windows:
    if window != original_window:
        bot.switch_to.window(window)
        break


precio1 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 1: ' + precio1)

precio2 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 2: ' + precio2)

precio3 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 3: ' + precio3)

precio4 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 4: ' + precio4)

precio5 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 5: ' + precio5)

precio6 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 6: ' + precio6)

precio7 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 7: ' + precio7)

precio8 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 8: ' + precio8)

precio9 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 9: ' + precio9)

precio10 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
print('precio paquete 10: ' + precio10)

opcionesAvanzadas = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
time.sleep(1)
opcionesAvanzadas.click()
time.sleep(1)

aerolinia = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
time.sleep(1)
aerolinia.click()
aerolinia.send_keys('avian')
time.sleep(1)

inputAereolinia = bot.find_element(By.XPATH, '/html/body/ul[3]/li[1]')
time.sleep(1)
inputAereolinia.click()
time.sleep(1)

buscarAvanzadas = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
time.sleep(1)
buscarAvanzadas.click()
time.sleep(20)

precio = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text

fecha = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]/div').text

horaSalida = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]').text

espaciosLibres = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[2]').text

horaSalida2 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[4]/div/div[1]/div[2]/div[1]/div[1]/div[2]').text

espaciosLibres2 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[4]/div/div[2]').text

duracion = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div[3]').text

fechaRegreso = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div').text

horaSalidaRegreso = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]').text

duracionRegreso = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[3]').text

texto_a_guardar = f""" 
        *** Mejor Oferta ***

        Precio: {precio}
        Aereolinia: Avianca

        IDA Bogota - Punta Cana: {fecha}
        Opcion 1: salida {horaSalida} - tiempo de vuelo {duracion}
                  {espaciosLibres}
        Opcion 2: salida {horaSalida2} - tiempo de vuelo {duracion}
                  {espaciosLibres2}
                 
        REGRESO Punta Cana - Bogota: {fechaRegreso}
        Opcion 1: salida {horaSalidaRegreso} - tiempo de vuelo {duracionRegreso}

"""

nombre_archivo = "mejor_oferta.txt"

with open(nombre_archivo, 'w') as archivo:
    archivo.write(texto_a_guardar)

print(f"archivo {nombre_archivo} guardado.")

bot.save_screenshot('capturaPantalla.png')

print(f"captura de pantalla guardada.")

time.sleep(3)
bot.quit()
