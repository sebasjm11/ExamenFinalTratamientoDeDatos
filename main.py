from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.camisetasfutboleses.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search > input")
search_box.send_keys("Real Madrid Retro")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#search > span > button > span > i")
search_button.click()

select_element = driver.find_element(By.CSS_SELECTOR, "#input-limit")
select = Select(select_element)
select.select_by_index(1)

camiseta = driver.find_elements(By.CSS_SELECTOR, "#content > div:nth-child(9) > div ")


for card in camiseta:
    try:
        nombre = card.find_element(By.CSS_SELECTOR, "div > div > div.product-details > div.caption > h4").text
        precio = card.find_element(By.CSS_SELECTOR, "div > div > div.product-details > div.caption > p.price > span.price-new").text
        descuento = card.find_element(By.CSS_SELECTOR, "div > div > div.product-details > div.caption > p.price > span.percentsaving").text
        # Tu código para procesar otros elementos aquí

        print(nombre)
        print(precio)
        print(descuento)
        # Imprime otros datos aquí

        Total = {
            "Nombre": nombre,
            "Precio": precio,
            "Descuento": descuento,
            # Agrega otros datos aquí
        }

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()

