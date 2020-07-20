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
# Kampanye Diajukan
# Pilih Kampanye
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]").click()
print("Kampanye DiPilih")
driver.implicitly_wait(10)
# Detail Perhitungan
driver.find_element_by_xpath("//h4[contains(text(),'Detail Perhitungan')]").click()
print("Detail Perhitungan")
driver.implicitly_wait(10)
# Reject Perhitungan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Reject Dana Dibutuhkan")
driver.implicitly_wait(10)
# Comment
driver.find_element_by_xpath("//div[@id='__next']//div//div//div//div//div//div//div//div//div//textarea").send_keys("Ganti Dana Dibutuhkan")
print("Comment")

# Simpan Data Sementara
driver.find_element_by_xpath("//div[contains(text(),'Simpan Revisi Sementara')]").click()
print("Simpan Data Sementara")
driver.implicitly_wait(10)
# Mengerti
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[24]/div[1]/div[1]").click()
print("Mengerti")

# Proses Dokumen
driver.find_element_by_xpath("//div[contains(text(),'Proses Dokumen')]").click()
print("Proses Dokumen")
driver.implicitly_wait(10)

# Kirim Data
driver.find_element_by_xpath("//div[contains(text(),'Kirim Data')]").click()
print("Kirim Data")
driver.implicitly_wait(10)
# Mengerti
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[22]/div[1]/div[1]").click()
print("Mengerti")

"""
-----------------------------------------------------------------------------------------------------------
"""
# Kampanye
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/h1[1]").click()
print("Kampanye")
driver.implicitly_wait(10)

# Tab Kampanye di Proses
driver.find_element_by_xpath("//h3[contains(text(),'Kampanye Diproses')]").click()
print("Kampanye di Proses")
driver.implicitly_wait(10)

# Pilih Kampanye
# XPATH CAN BE CHANGED TO SUIT WHICH CAMPAIGN WANT TO BE USED ON THE TEST
driver.find_element_by_xpath("//td[contains(text(),'PT BDO')]").click()
print("kampanye dipilih")
driver.implicitly_wait(10)

# Detail Perhitungan
driver.find_element_by_xpath("//h4[contains(text(),'Detail Perhitungan')]").click()
print("Detail Perhitungan")
driver.implicitly_wait(10)

# Terima Revisi
driver.find_element_by_xpath("//body//div[@id='__next']//div//div//div//div//div//div//div//div//div//div//div[2]//*[local-name()='svg']").click()
print("Terima Revisi")

# Ganti Status Kampanye
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-21-option-0')))
driver.find_element_by_id("react-select-21-option-0").click()
print("Verifikasi Dokumen Di Pilih")

# Simpan
driver.find_element_by_xpath("//div[contains(text(),'Simpan')]").click()
print("Simpan")
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Mengubah Status ke Pembayaran Deposit
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0')))
driver.find_element_by_id("react-select-2-option-0").click()
print("Pembayaran Deposit Di Pilih")

# Simpan
driver.find_element_by_xpath("//div[contains(text(),'Simpan')]").click()
print("Simpan")
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""
# Tolak Pembayaran
driver.find_element_by_xpath("//h5[contains(text(),'Tolak Pembayaran')]").click()
print("Tolak Pembayaran")
# Verifikasi Pembayaran
driver.find_element_by_xpath("//h5[contains(text(),'Verifikasi Pembayaran')]").click()
print("Verifikasi Pembayaran")
# Status Fee Berhaisl DiUpdate
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[20]/div[1]/div[1]").click()
print("Berhasil diupdate")

"""
-----------------------------------------------------------------------------------------------------------
"""
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
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""
# Mengubah Status ke Evaluasi Pengajuan Pendanaan
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
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""
# Mengubah Status ke Penandatanganan Surat Perjanjian
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0')))
driver.find_element_by_id("react-select-2-option-0").click()
print("Tanda Tangan Surat Perjanjian Di Pilih")

# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]").click()
print('Simpan')
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Mengubah Status ke Pembayaran Deposit
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0')))
driver.find_element_by_id("react-select-2-option-0").click()
print("Pembayaran Deposit Di Pilih")

# Simpan
driver.find_element_by_xpath("//div[contains(text(),'Simpan')]").click()
print("Simpan")
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------------------------------------------
"""

# Mengubah Status ke Publish Kampanye
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0')))
driver.find_element_by_id("react-select-2-option-0").click()
print("Publish Kampanye Di Pilih")

# Simpan
driver.find_element_by_xpath("//div[contains(text(),'Simpan')]").click()
print("Simpan")
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[28]/div[1]/div[1]").click()
print("Yakin")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

