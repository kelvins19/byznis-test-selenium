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
#link_to_web = "https://penerbit.byznis.id/login"
link_to_web = "http://127.0.0.1:3000/login"
driver.get(link_to_web)
driver.maximize_window()

driver.file_detector = UselessFileDetector()
path_to_file = "/Users/kelvin/Desktop/test_file.pdf"
path_to_image = "/Users/kelvin/Desktop/test_file.jpeg"

# Login
driver.implicitly_wait(10)
driver.find_element_by_class_name("email-input").send_keys("developer@byznis.id")
driver.find_element_by_class_name("password-input").send_keys("Byznis2019?")
driver.find_element_by_xpath("//button[contains(text(),'Masuk')]").click()
print("Login Successful")

#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)

driver.implicitly_wait(10)
# User click "Tambah Kampanye"
#driver.find_element_by_link_text("Tambah Kampanye").click()
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
print("Tambah Kampanye Clicked")

driver.implicitly_wait(10)

# User memasukkan nama PT
driver.find_element_by_id("nama_perseroan").send_keys("PT. Automate Test")
print("Nama PT Input")

# Modal Dasar
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("2000000000")
print("Modal Dasar")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/input[1]").send_keys("20000")
print("Terbagi Atas")

# Modal Disetor
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/input[1]").send_keys("500000000")
print("Modal disetor")

# User memasukkan email pemegang saham (akun belum terdaftar)
"""
driver.find_element_by_id("email_pemegang_saham").send_keys("madzarmr@byznis.id")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/button[1]").click()
print("Email Pemegang Saham Salah")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/img[1]").click()
print("Email Pemegang Saham di hapus")
"""
"""
# User memasukkan email pemegang saham
driver.find_element_by_id("email_pemegang_saham").send_keys("madzar@byznis.id")
driver.find_element_by_xpath("//button[contains(text(),'Enter')]").click()
print("Email Pemegang Saham Benar")
# Jumlah lembar saham anggota
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div[4]/div[1]/div[2]/div[1]/input[1]").send_keys("20")
driver.implicitly_wait(10)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div[4]/div[1]/div[2]/div[1]/input[1]").send_keys("0")
driver.implicitly_wait(10)
print("Jumlah lembar saham anggota")
"""
# Jumlah lembar saham Pendaftar
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/input[1]").send_keys("5000")
print("Jumlah lembar saham pendaftar")


# User memasukkan nomor legalitas dokumen perusahaan
# Akta Pendirian
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_akta_pendirian = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='Akta_Pendirian']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_akta_pendirian)
file_akta_pendirian.send_keys(path_to_file)
print("FILE 1 UPLOADED")

# SK Kemenkumham Akta Pendirian
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_sk_kemenkumham_1 = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='SK_Kemenkumham_Akta_Pendirian']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_sk_kemenkumham_1)
file_sk_kemenkumham_1.send_keys(path_to_file)
print("FILE 2 UPLOADED")

# Anggaran Dasar Terakhir
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_anggaran_dasar = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='Anggaran_Dasar_Terakhir']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_anggaran_dasar)
file_anggaran_dasar.send_keys(path_to_file)
print("FILE 3 UPLOADED")

# SK Kemenkumham Anggaran Dasar Terakhir
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_sk_kemenkumham_2 = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='SK_Kemenkumham_Anggaran_Dasar']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_sk_kemenkumham_2)
file_sk_kemenkumham_2.send_keys(path_to_file)
print("FILE 4 UPLOADED")

# NIB TDP
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[5]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_nib_tdp = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='NIB_TDP']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_nib_tdp)
file_nib_tdp.send_keys(path_to_file)
print("FILE 5 UPLOADED")

# Surat Izin Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[6]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_surat_izin = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='Surat_Izin_Usaha']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_surat_izin)
file_surat_izin.send_keys(path_to_file)
print("FILE 6 UPLOADED")

# SKDP
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[7]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_skdp = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='SKDP']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_skdp)
file_skdp.send_keys(path_to_file)
print("FILE 7 UPLOADED")

# NPWP Perusahaan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[8]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_npwp = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='NPWP_Perusahaan']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_npwp)
file_npwp.send_keys(path_to_file)
print("FILE 8 UPLOADED")

# Lapor Pajak
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[9]/div[2]/div[1]/input[1]").send_keys("1234567891234567")
file_lapor_pajak = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='Lapor_Pajak']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_lapor_pajak)
file_lapor_pajak.send_keys(path_to_file)
print("FILE 9 UPLOADED")

# User memilih status hutang
# Ada hutang
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[10]/div[1]/div[1]").click()
driver.implicitly_wait(10)
# Tidak Ada Hutang
driver.find_element_by_xpath("//html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[10]/div[1]/div[2]/p[1]").click()
print("Status Hutang di pilih")

# Simpan dan Lanjutkan ke Detail Bisnis
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]").click()
print("Simpan dan Lanjutkan ke Detail Bisnis")
"""
# User menklik Simpan Data
driver.implicitly_wait(10)
driver.find_element_by_link_text("Simpan Data Sementara").click()
print("Simpan Data Successful")
"""

# User menklik Bisnis
#driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/h4[1]").click()
driver.implicitly_wait(10)
# Alamat Kantor
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys("Jalan Alamat Kantor")
# Alamat Usaha
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/textarea[1]").send_keys("Jalan Alamat Usaha")
# Link GMaps
driver.find_element_by_id("link_google_maps").send_keys("https://g.page/itsu-jawa-timur?share")
# No Telp
driver.find_element_by_id("no_telp").send_keys("0811234567899")

# Provinsi

waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-kxksty-control')))
dropdownElements = driver.find_elements_by_class_name('css-kxksty-control')
for element in dropdownElements:
    element.click()

    print("Waiting for menu to be clickable")
    waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
    waits.until(EC.presence_of_element_located((By.CLASS_NAME, 'css-bppnuz-option')))
    driver.find_element_by_class_name('css-bppnuz-option').click()
    print("Element dipilih")

"""
driver.find_element_by_class_name('css-kxksty-control').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
driver.find_element_by_class_name('css-1kbxwby-option').click()
print("Provinsi dipilih")

driver.implicitly_wait(10)

# Kota
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]')))
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
driver.find_element_by_class_name('css-bppnuz-option').click()
print("Kota dipilih")
"""

# Merk Usaha
driver.find_element_by_id("merk_usaha").send_keys("Automate Test")
# Logo merk
logo_merk = driver.find_element_by_id("input_logo")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', logo_merk)
logo_merk.send_keys(path_to_image)
print("Logo Merk UPLOADED")
# Status Merek
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/p[1]").click()

# Berdiri Sejak
driver.find_element_by_id("berdiri_sejak").send_keys("2019")

# Total Cabang
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div[2]/input[1]").send_keys("0")

# Tanggal Kampanye (FROM)
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[5]/div[2]/div[1]/div[1]')))
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[5]/div[2]/div[1]/div[1]").click()
print("Waiting for Date Picker to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[5]/div[1]').click()
print("Tanggal FROM dipilih")

# Tanggal Kampanye (TO)
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[5]/div[2]/div[2]')))
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[5]/div[2]/div[2]").click()
print("Waiting for Date Picker to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[5]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[5]/div[7]').click()
print("Tanggal TO dipilih")


# Overview Usaha
driver.find_element_by_id("deskripsi_campaign").send_keys("Ini Overvuew Usaha")

# Kontak Industri
driver.find_element_by_id("industri").send_keys("IT")
# Kontak Jenis Usaha
driver.find_element_by_id("jenis_usaha").send_keys("IT Consultant")

# Tambah Foto Kampanye
foto_kampanye = driver.find_element_by_id("upload-campaign")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', foto_kampanye)
foto_kampanye.send_keys(path_to_image)
print("Foto Kampanye UPLOADED")
driver.implicitly_wait(10)
foto_kampanye.send_keys(path_to_image)

# ROI
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[5]/div[2]/div[1]/input[1]").send_keys("1")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[5]/div[2]/div[2]/input[1]").send_keys("10")
# Dividen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[6]/div[2]/div[1]/input[1]").send_keys("1")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[6]/div[2]/div[2]/input[1]").send_keys("10")
# BEP
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[7]/div[2]/div[1]/input[1]").send_keys("1")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[7]/div[2]/div[2]/input[1]").send_keys("3")
# Terima Hasil
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[8]/div[2]/div[1]/input[1]").send_keys("3")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[8]/div[2]/div[2]/input[1]").send_keys("6")

# Proposal Usaha
file_proposal_usaha = driver.find_element_by_xpath("//input[@id='usaha']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_proposal_usaha)
file_proposal_usaha.send_keys(path_to_file)
print("Proposal Usaha UPLOADED")
# Laporan Keuangan
file_laporan_keuangan = driver.find_element_by_xpath("//input[@id='keuangan']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_laporan_keuangan)
file_laporan_keuangan.send_keys(path_to_file)
print("Laporan Keuangan UPLOADED")
# Roadmap Usaha
file_roadmap_usaha = driver.find_element_by_xpath("//input[@id='roadmap']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_roadmap_usaha)
file_roadmap_usaha.send_keys(path_to_file)
print("Roadmap Usaha UPLOADED")


# Riwayat Pendapatan Bisnis
waits = WebDriverWait(driver, 10)
waits.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[10]/div[1]/div[1]')))
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[10]/div[1]/div[1]').click()
print("Waiting for menu to be clickable")
waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-26l3qy-menu')))
waits.until(EC.presence_of_element_located((By.ID, 'react-select-5-option-0')))
driver.find_element_by_id("react-select-5-option-0").click()
print("Riwayat Pendapatan dipilih")


# Tahun 1 Riwayat Pendapatan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys('2017')
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[1]/div[3]/div[2]/input[1]").send_keys('20000000')
print("Tahun 1 Riwayat Pendapatan")
# Tahun 2 Riwayat Pendapatan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys('2018')
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[2]/div[3]/div[2]/input[1]").send_keys('30000000')
print("Tahun 2 Riwayat Pendapatan")
# Tahun 3 Riwayat Pendapatan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[3]/div[1]/div[2]/input[1]").send_keys('2019')
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[3]/div[3]/div[2]/input[1]").send_keys('40000000')
print("Tahun 3 Riwayat Pendapatan")
# Tahun 4 Riwayat Pendapatan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[4]/div[1]/div[2]/input[1]").send_keys('2016')
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[4]/div[3]/div[2]/input[1]").send_keys('40000000')
print("Tahun 4 Riwayat Pendapatan")
# Tahun 5 Riwayat Pendapatan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[5]/div[1]/div[2]/input[1]").send_keys('2015')
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/div[5]/div[3]/div[2]/input[1]").send_keys('40000000')
print("Tahun 5 Riwayat Pendapatan")
driver.implicitly_wait(10)

# Detail Perhitungan
# User menklik Detail Perhitungan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]").click()
driver.implicitly_wait(10)
print("Simpan Dan Lanjutkan")
print("Detail Perhitungan")
# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys("300000000")
driver.implicitly_wait(10)
print("Dana Dibutuhkan")

# Simpan Data Sementara
#driver.find_element_by_link_text("Simpan Data Sementara").click()
#print("Simpan Data Sementara")

# Submit Data
driver.implicitly_wait(20)
driver.find_element_by_link_text("Submit Semua Data").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/button[1]").click()
print("Submit Data Berhasil")

# Log Out
#driver.implicitly_wait(10)
#driver.find_element_by_link_text("Keluar").click()
#driver.implicitly_wait(10)
#driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/button[1]").click()
#driver.implicitly_wait(100)
#print("Berhasil Keluar")
#driver.close()
