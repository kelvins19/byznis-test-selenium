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
#driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
driver.find_element_by_xpath("//th[2]//div[1]//div[1]//*[local-name()='svg']").click()
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

"""
-----------------------------------------------------------------------------------------------------------
"""

# SORT FILTER
# Kampanye
driver.find_element_by_xpath("//h1[contains(text(),'Kampanye')]").click()
print("Kampanye")
driver.implicitly_wait(10)

# Kampanye di Proses
driver.find_element_by_xpath("//h3[contains(text(),'Kampanye Diproses')]").click()
print("Kampanye diProses")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Nama Badan Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Nama Badan Usaha")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Nama Badan Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Nama Badan Usaha")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Merk
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Merk")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Merk
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Merk")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Industri
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Industri")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Industri
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Industri")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Dana Dibutuhkan
# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""
# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Diproses
driver.find_element_by_xpath("//h4[contains(text(),'Diproses')]").click()
print("Diproses")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Revisi
driver.find_element_by_xpath("//h4[contains(text(),'Revisi')]").click()
print("Revisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Ditolak
driver.find_element_by_xpath("//h4[contains(text(),'Ditolak')]").click()
print("Ditolak")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Sisa Waktu
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[8]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Sisa Waktu")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Sisa Waktu
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[8]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Sisa Waktu")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Sisa Waktu
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[8]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Sisa Waktu")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Pendaftaran
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Pendaftaran")
driver.implicitly_wait(10)
# Tanggal 1
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
print("Pop up Tanggal")
driver.implicitly_wait(10)
# Pilih Tanggal
driver.find_element_by_xpath("//body//div[@id='__next']//div//div//div//div//div//div//div//div//div//div//div//div//div[2]//div[1]").click()
print("Tanggal 1 DiPilih")
# Tanggal 2
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
print("Pop up Tanggal")
driver.implicitly_wait(10)
# Pilih Tanggal
driver.find_element_by_xpath("//div[contains(text(),'19')]").click()
print("Tanggal 2 DiPilih")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Sisa Waktu
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Pendaftaran")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# SORT FILTER
# Kampanye
driver.find_element_by_xpath("//h1[contains(text(),'Kampanye')]").click()
print("Kampanye")
driver.implicitly_wait(10)

# Kampanye Berjalan
driver.find_element_by_xpath("//h3[contains(text(),'Kampanye Berjalan')]").click()
print("Kampanye Berjalan")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# ID
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter ID")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("47")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# ID
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter ID")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# PT Penerbit
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter PT Penerbit")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# PT Penerbit
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter PT Penerbit")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Merk
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Merk")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("47")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Merk
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Merk")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""
# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Sedang Berjalan
driver.find_element_by_xpath("//h4[contains(text(),'Sedang Berjalan')]").click()
print("Sedang Berjalan")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Tidak Berhasil
driver.find_element_by_xpath("//h4[contains(text(),'Tidak Berhasil')]").click()
print("Tidak Berhasil")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Berhasil
driver.find_element_by_xpath("//body//div[@id='__next']//div//div//div//div//div[1]//h4[1]").click()
print("Berhasil")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Status
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Status")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Dana Dibutuhkan
# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[7]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Dana Terkumpul
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Terkumpul")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Dana Terkumpul
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Terkumpul")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Dana Terkumpul
# Dana Terkumpul
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Terkumpul")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# SORT FILTER
# Kampanye
driver.find_element_by_xpath("//h1[contains(text(),'Kampanye')]").click()
print("Kampanye")
driver.implicitly_wait(10)

# Kampanye Berjalan
driver.find_element_by_xpath("//h3[contains(text(),'Kampanye Diajukan')]").click()
print("Kampanye Diajukan")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Pendaftaran
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Pendaftaran")
driver.implicitly_wait(10)
# Tanggal 1
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
print("Pop up Tanggal")
driver.implicitly_wait(10)
# Pilih Tanggal
driver.find_element_by_xpath("//body//div[@id='__next']//div//div//div//div//div//div//div//div//div//div//div//div//div[2]//div[1]").click()
print("Tanggal 1 DiPilih")
# Tanggal 2
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
print("Pop up Tanggal")
driver.implicitly_wait(10)
# Pilih Tanggal
driver.find_element_by_xpath("//div[contains(text(),'19')]").click()
print("Tanggal 2 DiPilih")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Pendaftaran
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Pendaftaran")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Nama Badan Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Nama Badan Usaha")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Nama Badan Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Nama Badan Usaha")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Merk
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Merk")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Merk
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[4]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Merk")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Industri
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Industri")
driver.implicitly_wait(10)
# Kata Kunci
driver.find_element_by_xpath("//input[@placeholder='Cari kata kunci disini']").send_keys("A")
print("Kata Kunci diisi")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Filter
# Industri
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Industri")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Descending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]").click()
print("Descending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Ascending
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Ascending")
# Submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
print("Submit")
driver.implicitly_wait(10)

# Clear Dana Dibutuhkan
# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[6]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Filter Dana Dibutuhkan")
driver.implicitly_wait(10)
# Clear
driver.find_element_by_xpath("//div[contains(text(),'Clear Filter')]").click()
print("Clear Filter")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Blog
driver.find_element_by_xpath("//h5[contains(text(),'Blog')]").click()
print("Blog")
driver.implicitly_wait(10)
