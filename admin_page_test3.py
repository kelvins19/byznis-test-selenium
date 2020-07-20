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
driver.find_element_by_class_name("password-input").send_keys("TestUser001!")
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

# SORT FILTER
# Pengguna
driver.find_element_by_xpath("//h1[contains(text(),'Pengguna')]").click()
print("Pengguna")
driver.implicitly_wait(10)
# Nama
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Nama")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Nama
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Nama")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Belum Terverifikasi
driver.find_element_by_xpath("//h4[contains(text(),'Belum Terverifikasi')]").click()
print("Belum Terverifikasi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Terverifikasi
driver.find_element_by_xpath("//h4[contains(text(),'Terverifikasi')]").click()
print("Terverifikasi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Transaksi
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Transaksi")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Transaksi
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Transaksi")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Limit
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Limit")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Limit
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Limit")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Limit
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Limit")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Dividen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dividen")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Dividen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dividen")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Dividen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dividen")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)