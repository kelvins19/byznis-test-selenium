from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import UselessFileDetector
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/kelvin/Documents/Framework/chromedriver")
#link_to_web = "https://admin.byznis.id/login"
link_to_web = "http://127.0.0.1:3000/login"
driver.get(link_to_web)
driver.maximize_window()

driver.file_detector = UselessFileDetector()
path_to_file = "/Users/kelvin/Desktop/test_file.pdf"
path_to_image = "/Users/kelvin/Desktop/test_file.jpeg"

"""
-----------------------------------------------------------------------------------------------------------
"""
# Login
driver.implicitly_wait(10)
driver.find_element_by_class_name("email-input").send_keys("kelvin@byznis.id")
driver.find_element_by_class_name("password-input").send_keys("g9t2cD7WyR0xT1FUdiRfPnlYx")
driver.find_element_by_xpath("//button[contains(text(),'Masuk')]").click()
print("Login Successful")

"""
-----------------------------------------------------------------------------------------------------------
"""
# Assert
waits = WebDriverWait(driver, 60)
waits.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Manajemen Kampanye')]")))
print("Kampanye")

"""
-----------------------------------------------------------------------------------------------------------
"""

# Kamoanye Berjalan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]").click()
print("Kampanye Berjalan")

# Memilih Kampanye
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").click()
print("Memilih Kampanye")

# Bisnis
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]").click()
print("Bisnis")

# Dividen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[10]/div[2]/div[2]/div[2]/input[1]").send_keys("1000000")
print("Dviden")
# Konfirmasi
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[10]/div[3]/button[1]").click()
print("Konfirmasi Dividen")

# Laporan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[13]/div[1]/label[1]")
file_laporan = driver.find_element_by_xpath("//input[@id='upload-laporan']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_laporan)
file_laporan.send_keys(path_to_file)
print("Laporan Usaha UPLOADED")
# Menghapus Laporan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[13]/div[1]/div[1]/div[2]/*[local-name()='svg'][1]").click()
print("Menghapus Laporan")

# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]").click()
print("Simpan")

# Ganti Status Kampanye
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0')))
driver.find_element_by_id("react-select-2-option-0").click()
print("Publish Kampanye Di Pilih")

# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]").click()
print("Simpan")

# Klik Bisnis
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]").click()
print("Bisnis")
# Riwayat Transaksi
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[9]/div[1]/table[1]/tbody[1]/tr[1]/td[3]").click()
driver.implicitly_wait(10)
print("Riwayat Transaksi")
# Transaksi Selesai
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]/button[2]").click()
print("Transaksi Selesai")