from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyautogui as pa
import re

def por_los_jajas(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element("xpath","//button[contains(text(), 'Siguiente')]").click()

    driver.find_element("xpath","//*[@id='answer699531X61X3569other']").send_keys("a") # 1
    driver.find_element("xpath",'//*[@id="answer699531X61X3570other"]').send_keys("a") # 2
    driver.find_element("xpath",'//*[@id="answer699531X61X3606other"]').send_keys("a") # 3

    paths_first_screen = [
        '//*[@id="javatbd699531X61X35714"]/td[6]/label',
        '//*[@id="javatbd699531X61X35715"]/td[6]/label',
        '//*[@id="javatbd699531X61X35716"]/td[6]/label',
        '//*[@id="javatbd699531X61X35717"]/td[6]/label',
        '//*[@id="javatbd699531X61X35718"]/td[6]/label',
        '//*[@id="javatbd699531X61X35719"]/td[6]/label',
        '//*[@id="javatbd699531X61X357110"]/td[6]/label',
        '//*[@id="javatbd699531X61X357111"]/td[6]/label',

        '//*[@id="javatbd699531X61X36071"]/td[1]/label',
        '//*[@id="javatbd699531X61X36072"]/td[2]/label',
        '//*[@id="javatbd699531X61X36073"]/td[3]/label',
        '//*[@id="javatbd699531X61X36074"]/td[4]/label',
        '//*[@id="javatbd699531X61X36075"]/td[5]/label',
        '//*[@id="javatbd699531X61X36076"]/td[6]/label',
        '//*[@id="javatbd699531X61X36077"]/td[7]/label',
        '//*[@id="javatbd699531X61X36078"]/td[8]/label',
    ]
    for path in paths_first_screen:
        driver.find_element("xpath",path).click()
    driver.find_element("xpath","//button[contains(text(), 'Siguiente')]").click()

    paths_second_screen = [
        '//*[@id="javatbd699531X62X35723"]/label',
        '//*[@id="javatbd699531X62X35731"]/label',
        '//*[@id="javatbd699531X62X35741"]/label',
        '//*[@id="javatbd699531X62X35755"]/label',
        '//*[@id="javatbd699531X62X35762"]/label',
        '//*[@id="javatbd699531X62X35773"]/label',
        '//*[@id="answer699531X62X35781"]',
        '//*[@id="javatbd699531X62X35797"]/label'
    ]
    for path in paths_second_screen:
        driver.find_element("xpath",path).click()
    driver.find_element("xpath","//button[contains(text(), 'Siguiente')]").click()



    driver.find_element("xpath",'//*[@id="javatbd699531X63X35801"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35802"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35803"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35804"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35805"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35806"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35807"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35808"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35809"]/td[5]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35811"]/td[1]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35812"]/td[1]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35813"]/td[1]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35814"]/td[1]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35815"]/td[1]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35816"]/td[1]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X63X35817"]/td[1]/label').click()
    sleep(5)
    driver.find_element("xpath","//button[contains(text(), 'Siguiente')]").click()



    driver.find_element("xpath",'//*[@id="answer699531X64X3582AO03"]').click()
    driver.find_element("xpath",'//*[@id="answer699531X64X3584other"]').send_keys("me hacen llenar encuestas a la fuerza")
    driver.find_element("xpath",'//*[@id="answer699531X64X3585SQ003"]').click()
    driver.find_element("xpath",'//*[@id="answer699531X64X3611othertext"]').send_keys('no estoy considerando cambiarme, pero esto de "suspender NEO por 2 dias a quienes no llenen la encuesta" tiene que parar.')
    driver.find_element("xpath",'//*[@id="answer699531X64X3587SQ001"]').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X64X3588AO03"]/label').click()
    driver.find_element("xpath",'//*[@id="answer699531X64X3589AO03"]').click()
    driver.find_element("xpath",'//*[@id="answer699531X64X3590"]').send_keys("Talvez me obliguen a llenar encuestas de nuevo")
    driver.find_element("xpath",'//*[@id="javatbd699531X64X3591SQ002"]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X64X3591SQ003"]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X64X3591SQ006"]/label').click()
    driver.find_element("xpath","//button[contains(text(), 'Siguiente')]").click()


    driver.find_element("xpath",'//*[@id="answer699531X65X3592other"]').send_keys('Cualquier lugar, pero no en las "encuestas obligatorias"')
    driver.find_element("xpath",'//*[@id="javatbd699531X65X3593SQ001"]/td[2]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X65X3593SQ002"]/td[2]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X65X3593SQ003"]/td[2]/label').click()
    driver.find_element("xpath",'//*[@id="javatbd699531X65X3593SQ004"]/td[2]/label').click()
    driver.find_element("xpath",'//*[@id="answer699531X65X3594AO02"]').click()
    driver.find_element("xpath","//button[contains(text(), 'Siguiente')]").click()


    driver.find_element("xpath",'//*[@id="javatbd699531X66X3597AO01"]/label').click()
    age = Select(driver.find_element("xpath",'//*[@id="answer699531X66X3598"]'))
    age.select_by_visible_text("15 años")
    driver.find_element("xpath",'//*[@id="answer699531X66X3599AO02"]').click()
    driver.find_element("xpath",'//*[@id="answer699531X66X36002"]').click()
    driver.find_element("xpath",'//*[@id="answer699531X66X3601othertext"]').send_keys('Donde no obligan a hacer encuestas')
    carreer = Select(driver.find_element("xpath",'//*[@id="answer699531X66X3602"]'))
    carreer.select_by_visible_text("INGENIERÍA AMBIENTAL")
    driver.find_element("xpath",'//*[@id="javatbd699531X66X36042"]/label').click()
    driver.find_element("xpath",'//*[@id="answer699531X66X36052"]').click()

    driver.find_element("xpath","//button[contains(text(), 'Enviar')]").click()






url = pa.prompt('', 'introduce el URL de la encuesta:')

#regex for url with token query and token value
regex =  r'^(?:https://ucbx.edu.bo/encuestas/index.php/699531\?token=)(\d+)'

url_regex = re.compile(regex)
if(not url_regex.match(url)):
    pa.alert("URL invalida, vuelve a intentarlo.")
    exit()
else:
    action = pa.confirm('URL Valido. ¿Deseas continuar?', 'Confirmacion', ['Si', 'No'])
    if(action == 'Si'):
        por_los_jajas(url)
        pa.alert("Listo!")
        exit()
    else:
        exit()