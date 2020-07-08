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
# Atur Industri & Jenis Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/h3[1]").click()
print("Atur Industri & Jenis Usaha")
# Klik +
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]").click()
print("+")
# Nama Industri
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[3]/input[1]").send_keys("Industri Test")
print("Nama Industi")
# Nama Jenis Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/input[1]").send_keys("Jenis Usaha Test")
print("Jenis Usaha")
# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]").click()
print("Simpan")

# Pilih Industri
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]").click()
print("Pilih Industri")
# Hapus Industri
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]").click()
print("Hapus Industri")

# Klik Batal
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]").click()
print("Batal")

"""
-----------------------------------------------------------------------------------------------------------
"""
# Tab Kampanye di Proses
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/h3[1]").click()
print("Kampanye di Proses")

# Pilih Kampanye
# XPATH CAN BE CHANGED TO SUIT WHICH CAMPAIGN WANT TO BE USED ON THE TEST
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]").click()
print("kampanye dipilih")

# Detail Bisnis
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]").click()
print("Detail Bisnis")

# Ganti Status Kampanye
"""
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-21-option-0')))
driver.find_element_by_id("react-select-21-option-0").click()
print("Verifikasi Dokumen Di Pilih")
"""

# Menyetujui Revisi
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[2]/div[1]/div[8]/div[1]/div[1]/div[2]/*[local-name()='svg'][1]").click()
print("Roadmap Usaha")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[2]/div[1]/div[12]/div[1]/div[2]/*[local-name()='svg'][1]").click()
print("Riwayat Pendapatan")

# Valuasi Perusahaan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("2000000000")
print("Valuasi Perusahaan")

# Simpan Data Sementara
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
print("Simpan Data Sementara")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[24]/div[1]/div[1]").click()
print("Mengerti")

# Kirim
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
print("Kirim")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[24]/div[1]/div[1]").click()
print("Mengerti")

"""
MERUBAH STATUS KAMPANYE
"""

# Kampanye
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/h1[1]").click()
print("Kampanye")
# Kampanye d Proses
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]").click()
print('Kampanye di Proses')
# Memilih Kampanye
# XPATH CAN BE CHANGED TO SUIT WHICH CAMPAIGN WANT TO BE USED ON THE TEST
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").click()
print("Kampanye Di Pilih")

# Mengubah Status ke Pembayaran Deposit
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0')))
driver.find_element_by_id("react-select-2-option-0").click()
print("Verifikasi Dokumen Di Pilih")

# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
print('Simpan')
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")

# Tolak Pembayaran
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[5]/div[2]").click()
print("Tolak Pembayaran")
# Verifikasi Pembayaran
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[5]/div[1]").click()
print("Verifikasi Pembayaran")
# Status Fee Berhaisl DiUpdate
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[20]/div[1]/div[1]").click()
print("Berhasil diupdate")

# Mengubah Status ke Site Visit
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0')))
driver.find_element_by_id("react-select-2-option-0").click()
print("Disetujui Untuk Site Visit di Pilih")

# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
print("Simpan")
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")
