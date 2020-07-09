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

"""
NEED
TO 
BE
FIXED
"""
# Banner
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[2]/h5[1]").click()
print("Banner")
driver.implicitly_wait(10)


# Banner Website
file_banner = driver.find_element_by_id('upload-banner')
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_banner)
file_banner.send_keys(path_to_image)
print("Banner Uploaded")
driver.implicitly_wait(10)
# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
print("Simpan")
driver.implicitly_wait(10)

# Hapus Banner Website
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[1]/*[local-name()='svg'][1]").click()
print("Hapus")
driver.implicitly_wait(10)
# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
print("Simpan")
driver.implicitly_wait(10)

# Banner Aplikasi
file_banner_aplikasi = driver.find_element_by_id("upload-banner-mobile")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_banner_aplikasi)
file_banner_aplikasi.send_keys(path_to_image)
print("Banner Aplikasi Uploaded")
driver.implicitly_wait(10)
# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]").click()
print("Simpan")
driver.implicitly_wait(10)

# Hapus Banner Aplikasi
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/*[local-name()='svg'][1]").click()
print("Banner App Di Hapus")
driver.implicitly_wait(10)
# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]").click()
print("SImpan")
driver.implicitly_wait(10)


"""
-----------------------------------------------------------------------------------------------------------
"""

# Blog
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[3]/h5[1]").click()
print("Blog")
driver.implicitly_wait(10)

# Cover Artikel
file_cover_artikel = driver.find_element_by_xpath("//input[@id='upload-cover-artikel']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_cover_artikel)
file_cover_artikel.send_keys(path_to_file)
print("Cover Artikel Uploaded")
# Judul
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/input[1]").send_keys("Judul Test")
print("Judul")
# SUb Judul
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/input[2]").send_keys("Sub Judul Test")
print("SUb Judul")
# Content
# Hashtag
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/input[1]").send_keys("#HashtagTest")
print("Hashtag")
# Terbitkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]").click()
print("Terbitkan")
driver.implicitly_wait(10)

# Editor Artikel
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/h2[2]").click()
print("Editor Artikel")
driver.implicitly_wait(10)
# Hapus Artikel
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/*[local-name()='svg'][1]").click()
print("Hapus Artikel")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# FAQ
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[4]/h5[1]").click()
print("FAQ")
driver.implicitly_wait(10)
# Tambah
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]").click()
print("Tambah")
driver.implicitly_wait(10)
# Pertanyaan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/input[1]").send_keys("Apa pertanyaannya")
print("Pertanyaan")
# Jawaban
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/textarea[1]").send_keys("Ini Jawbannya lalalallalal")
print("Jawaban")
# Urutan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/*[local-name()='svg'][1]").click()
print("Urutan")
driver.implicitly_wait(10)
# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]").click()
print("SImpan")
driver.implicitly_wait(10)

# Hapus
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/*[local-name()='svg'][1]").click()
print("Hapus")
driver.implicitly_wait(10)
# Yakin
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]").click()
print("Yakin")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Pengguna
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/h1[1]").click()
print("Pengguna")
driver.implicitly_wait(10)
# Pilih Pengguna
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[1]").click()
print("Pilih Pengguna")
driver.implicitly_wait(10)
# Jumlah Transaksi
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]").click()
print("Tab Jumlah Transaksi")
# Jumlah Kampanye DiDanai
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]").click()
print("Tab Jumlah Kampanye DiDanai")
# Dokumen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[3]").click()
print("Tab Dokumen")
# Dividen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[4]").click()
print("Tab Dividen")

# Verifikasi
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
#waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]')))
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]").click()
print("Sudah Di Verikasi Di Pilih")

# Simpan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]").click()
print("Simpan")
driver.implicitly_wait(10)

# Pengguna
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/h1[1]").click()
print("Pengguna")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Dashboard
# Tab Pengguna
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/h1[1]").click()
print("Dahsboard")
driver.implicitly_wait(10)
# Tab Kampanye
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]").click()
print("Tab Kampanye")
driver.implicitly_wait(10)
# Popularitas
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
print("Popularitas")
driver.implicitly_wait(10)
# Pendanaan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]").click()
print("Pendanaan")
driver.implicitly_wait(10)
# Sort Tinggi Ke Rendah
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/div[1]/div[1]/*[local-name()='svg'][1]/*[name()='path'][1]").click()
print("Sorted")

"""
-----------------------------------------------------------------------------------------------------------
"""

# Kampanye
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/h1[1]").click()
print("Kampanye")
driver.implicitly_wait(10)

# Atur Industri & Jenis Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/h3[1]").click()
print("Atur Industri & Jenis Usaha")
driver.implicitly_wait(10)
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

# Kampanye di Proses
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]").click()
print("Kampanye Di Proses")
driver.implicitly_wait(10)

"""
-----------------------------------------------------------------------------------------------------------
"""

# Kampanye Jalan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]").click()
print("Kampanye Jalan")
driver.implicitly_wait(10)

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
#driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]/button[2]").click()
print("Transaksi Selesai")