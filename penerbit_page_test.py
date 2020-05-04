from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import UselessFileDetector
from selenium.webdriver.support import wait

driver = webdriver.Chrome("/Users/kelvin/Documents/Framework/chromedriver")
link_to_web = "https://penerbit.byznis.id/login"
driver.get(link_to_web)
driver.maximize_window()

driver.file_detector = UselessFileDetector()
path_to_file = "/Users/kelvin/Desktop/test_file.pdf"
path_to_image = "/Users/kelvin/Desktop/test_file.jpeg"

# Login
driver.implicitly_wait(10)
driver.find_element_by_class_name("email-input").send_keys("ardyo@byznis.id")
driver.find_element_by_class_name("password-input").send_keys("Jakarta123!")
driver.find_element_by_xpath("//button[contains(text(),'Masuk')]").click()
print("Login Successful")

#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)

driver.implicitly_wait(10)
# User click "Tambah Kampanye"
driver.find_element_by_link_text("Tambah Kampanye").click()
print("Tambah Kampanye Clicked")

driver.implicitly_wait(10)
"""
# User memilih Tipe usaha
driver.find_element_by_xpath("//div[@class='sc-bkAgUZ eyhXOw']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@class='sc-LzLqG btaMha']").click()
print("Tipe Usaha is Chosen")
"""

# User memasukkan nama PT
driver.find_element_by_id("nama_perseroan").send_keys("PT. Automate Test")
print("Nama PT Input")

# Modal Dasar
driver.find_element_by_xpath("//div[@class='sc-bkAgCL ifPjKj']//input[@placeholder='Masukkan modal dasar']").send_keys("2000000000")
print("Modal Dasar")
driver.find_element_by_xpath("//div[@class='sc-bkAgCK btsrMe']//input").send_keys("20000")
print("Terbagi Atas")

# Modal Disetor
driver.find_element_by_xpath("//div[@class='sc-bkAgCM imVffw']//input[@placeholder='Masukkan modal dasar']").send_keys("500000")
print("Modal disetor")

# User memasukkan email pemegang saham (akun belum terdaftar)
"""
driver.find_element_by_id("email_pemegang_saham").send_keys("madzarmr@byznis.id")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/button[1]").click()
print("Email Pemegang Saham Salah")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/img[1]").click()
print("Email Pemegang Saham di hapus")
"""

# User memasukkan email pemegang saham
driver.find_element_by_id("email_pemegang_saham").send_keys("madzar@byznis.id")
driver.find_element_by_xpath("//button[contains(text(),'Enter')]").click()
print("Email Pemegang Saham Benar")


# User memasukkan nomor legalitas dokumen perusahaan
# Akta Pendirian
driver.find_element_by_id("akta_pendirian").send_keys("1234567891234567")
file_akta_pendirian = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='akta_pendirian']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_akta_pendirian)
file_akta_pendirian.send_keys(path_to_file)
print("FILE 1 UPLOADED")

# SK Kemenkumham Akta Pendirian
driver.find_element_by_id("sk_kemenkumham_akta_pendirian").send_keys("1234567891234567")
file_sk_kemenkumham_1 = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='sk_kemenkumham_akta_pendirian']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_sk_kemenkumham_1)
file_sk_kemenkumham_1.send_keys(path_to_file)
print("FILE 2 UPLOADED")

# Anggaran Dasar Terakhir
driver.find_element_by_id("anggaran_dasar_terakhir").send_keys("1234567891234567")
file_anggaran_dasar = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='anggaran_dasar_terakhir']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_anggaran_dasar)
file_anggaran_dasar.send_keys(path_to_file)
print("FILE 3 UPLOADED")

# SK Kemenkumham Anggaran Dasar Terakhir
driver.find_element_by_id("sk_kemenkumham_anggaran_dasar_terakhir").send_keys("1234567891234567")
file_sk_kemenkumham_2 = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='sk_kemenkumham_anggaran_dasar_terakhir']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_sk_kemenkumham_2)
file_sk_kemenkumham_2.send_keys(path_to_file)
print("FILE 4 UPLOADED")

# NIB TDP
driver.find_element_by_id("nib_tdp").send_keys("1234567891234567")
file_nib_tdp = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='nib_tdp']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_nib_tdp)
file_nib_tdp.send_keys(path_to_file)
print("FILE 5 UPLOADED")

# Surat Izin Usaha
driver.find_element_by_id("surat_izin_usaha").send_keys("1234567891234567")
file_surat_izin = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='surat_izin_usaha']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_surat_izin)
file_surat_izin.send_keys(path_to_file)
print("FILE 6 UPLOADED")

# SKDP
driver.find_element_by_id("skdp").send_keys("1234567891234567")
file_skdp = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='skdp']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_skdp)
file_skdp.send_keys(path_to_file)
print("FILE 7 UPLOADED")

# NPWP Perusahaan
driver.find_element_by_id("npwp_perusahaan").send_keys("1234567891234567")
file_npwp = driver.find_element_by_xpath("//label[contains(text(),'Unggah Dokumen')]//input[@id='npwp_perusahaan']")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_npwp)
file_npwp.send_keys(path_to_file)
print("FILE 8 UPLOADED")

# User memilih status hutang
# Ada hutang
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[9]/div[1]/div[1]").click()
driver.implicitly_wait(10)
# Tidak Ada Hutang
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[9]/div[1]/div[2]").click()
print("Status Hutang di pilih")

# User menklik Bisnis
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]").click()
# User menklik Simpan Data
driver.implicitly_wait(10)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[8]/div[1]/div[1]/button[1]").click()
print("Simpan Data Successful")

driver.implicitly_wait(10)
# Alamat Kantor
driver.find_element_by_xpath("//div[@class='sc-fzXfQu koaJkp']//div[1]//div[1]//div[1]//textarea[1]").send_keys("Jalan Alamat Kantor")
# Alamat Usaha
driver.find_element_by_xpath("//div[@class='sc-fzXfQt kBppBG']//div[2]//div[1]//div[1]//textarea[1]").send_keys("Jalan Alamat Usaha")
# Link GMaps
driver.find_element_by_id("link_google_maps").send_keys("https://g.page/itsu-jawa-timur?share")
# No Telp
driver.find_element_by_id("no_telp").send_keys("0811234567899")

# Provinsi
"""
NOT WORKING YET. NEED TO BE REVISED
"""
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
#wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.sc-LzLtg.jZnaCD div.sc-LzLth.eRJXLr div.sc-LzLLG.lozSd div.sc-LzLLD.jTHetp div.sc-LzLLF.kygPOe div.sc-LzLLz.gIcyCJ:nth-child(1) div.sc-LzLLC.eALuzH:nth-child(2) div.sc-LzLLA.gflJNA div.select-option.css-2b097c-container:nth-child(2) div.css-kxksty-control div.css-1hwfws3 > div.css-1uccc91-singleValue"))).click()
print("Provinsi Element Found")


# Kota
"""
NOT WORKING YET. NEED TO BE REVISED
"""
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
driver.implicitly_wait(10)
print("Kota Element Found")


# Merk Usaha
driver.find_element_by_id("merk_usaha").send_keys("Automate Test")
# Logo merk
logo_merk = driver.find_element_by_id("input_logo")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', logo_merk)
logo_merk.send_keys(path_to_image)
print("Logo Merk UPLOADED")
# Status Merek
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/p[1]").click()

# Status Usaha Yang Di Ajukan
# Sudah Berjalan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/p[1]").click()
driver.implicitly_wait(10)
# Belum Berjalan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/p[1]").click()

# Berdiri Sejak
driver.find_element_by_id("berdiri_sejak").send_keys("2019")

# Total Cabang
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]/input[1]").send_keys("0")

# Tanggal Kampanye

# Dana Dibutuhkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[7]/div[1]/input[1]").send_keys("2500000")
# Jumlah Saham Diterbitkan
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[8]/div[1]/input[1]").send_keys("1000")
# Jumlah Saham Publik
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[9]/div[1]/input[1]").send_keys("500")
# % Kepemilikan Saham Publik
driver.implicitly_wait(20)
# Dana Minimum
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[11]/div[1]/input[1]").send_keys("10000")
# Sumber Dana Lain
driver.find_element_by_id("sumber_dana_lain").send_keys("Anywhere")
# Overview Usaha
driver.find_element_by_id("deskripsi_campaign").send_keys("Ini Overvuew Usaha")



# Kontak Industri
"""
NEED TO BE REVISED.
"""
driver.find_element_by_id("industri").send_keys("IT")
# Kontak Jenis Usaha
"""
NEED TO BE REVISED.
"""
driver.find_element_by_id("jenis_usaha").send_keys("IT Consultant")

# Tambah Foto Kampanye
foto_kampanye = driver.find_element_by_id("upload-campaign")
driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', foto_kampanye)
foto_kampanye.send_keys(path_to_image)
print("Foto Kampanye UPLOADED")
driver.implicitly_wait(10)
foto_kampanye.send_keys(path_to_image)
# User Menghapus foto Kampanye
driver.implicitly_wait(10)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]").click()

# ROI
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[4]/div[1]/div[1]/input[1]").send_keys("1")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[4]/div[1]/div[2]/input[1]").send_keys("10")
# Dividen
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[5]/div[1]/div[1]/input[1]").send_keys("1")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[5]/div[1]/div[2]/input[1]").send_keys("10")
# BEP
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[6]/div[1]/div[1]/input[1]").send_keys("1")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[6]/div[1]/div[2]/input[1]").send_keys("3")
# Terima Hasil
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[7]/div[1]/div[1]/input[1]").send_keys("3")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[7]/div[1]/div[2]/input[1]").send_keys("6")

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

"""
# Download Format Dokumen
#driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[8]/div[1]/h3[1]").click()
"""
# Riwayat Pendapatan Bisnis
"""
NOT WORKING YET. NEED TO BE REVISED.
"""
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[14]/div[1]/div[1]/div[1]").click()
driver.implicitly_wait(10)
#driver.find_element_by_class_name("css-2613qy-menu").click()
print("Riwayat Element Found")

# Submit Data (Error Handling)
driver.find_element_by_link_text("Submit Semua Data").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]").click()
print("Error Handling Successful")


# Submit Data (TRUE)


# Log Out
driver.implicitly_wait(10)
#driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
#driver.implicitly_wait(10)
driver.find_element_by_link_text("Keluar").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[9]/div[1]/div[2]/div[1]/button[1]").click()
driver.implicitly_wait(100)
print("Berhasil Keluar")
#driver.close()
