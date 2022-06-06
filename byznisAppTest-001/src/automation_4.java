import java.net.MalformedURLException;

import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.android.nativekey.AndroidKey;
import io.appium.java_client.android.nativekey.KeyEvent;
import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.touch.WaitOptions;
import io.appium.java_client.touch.offset.PointOption;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.Assert;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;
import java.util.concurrent.TimeUnit;

public class automation_4 {

    public static void main(String args[]) throws MalformedURLException {

        DesiredCapabilities dc = new DesiredCapabilities();

        dc.setCapability(MobileCapabilityType.DEVICE_NAME, "emulator-5554");
        dc.setCapability("platformName", "Android");
        dc.setCapability("appPackage", "com.byznis.byniz");
        dc.setCapability("appActivity", "host.exp.exponent.MainActivity");

        AndroidDriver<AndroidElement> driver = new AndroidDriver<AndroidElement>(new URL("http://127.0.0.1:4723/wd/hub"), dc);
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        TouchAction ts = new TouchAction(driver);
        KeyEvent back = new KeyEvent(AndroidKey.BACK);
        Dimension screenSize = driver.manage().window().getSize();
        System.out.println("Screen Size is " + screenSize);

        // Membeli Saham
        // Transaksi
        // Liat Aset

        // LOGIN
        MobileElement el1 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]");
        el1.click();
        System.out.println("Klik Masuk");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        MobileElement el2 = (MobileElement) driver.findElementByXPath("//android.widget.EditText[@text='Alamat Email']");
        el2.sendKeys("test_user@gmail.com");
        System.out.println("Email");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        MobileElement el3 = (MobileElement) driver.findElementByXPath("//android.widget.EditText[@text='Kata Sandi']");
        el3.sendKeys("TestUser002!");
        System.out.println("Password");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        MobileElement el4 = (MobileElement) driver.findElementByXPath("//android.widget.TextView[@text='Masuk']");
        el4.click();
        System.out.println("Login Success");

        // Wait & Check til Beranda show up
        driver.manage().timeouts().implicitlyWait(6000, TimeUnit.SECONDS);
        Assert.assertEquals(driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[1]").getText(), "Selamat datang!");
        System.out.println("Beranda Muncul");
        driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);

        // Klik Jelajah
        MobileElement el1_2 = (MobileElement) driver.findElementByAccessibilityId("Jelajah, tab, 2 of 4");
        el1_2.click();
        System.out.println("Jelajah");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Search Kampanye
        MobileElement el2_0 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup");
        el2_0.click();
        System.out.println("Search");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Kata Pencarian
        MobileElement el3_0 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText");
        el3_0.sendKeys("Kopi");
        System.out.println("Kata Pencarian");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Klik Kampanye
        MobileElement el2_2 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup");
        el2_2.click();
        System.out.println("Memilih Kampanye");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Klik Beli Saham
        MobileElement el3_2 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]");
        el3_2.click();
        System.out.println("Beli Saham");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Klik +
        MobileElement el4_2 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup");
        el4_2.click();
        el4_2.click();
        el4_2.click();
        // Klik Lanjut ke Pembayaran
        MobileElement el5 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView");
        el5.click();
        System.out.println("Lanjut Ke Pembayaran");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Menyalin Nomor Akun Virtual
        MobileElement el6 = (MobileElement) driver.findElementByXPath("//android.widget.TextView[@text='SALIN']");
        el6.click();
        System.out.println("Menyalin Nomor VA");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Konfirmasi Pembelian Saham
        MobileElement el7 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup");
        el7.click();
        System.out.println("Konfirmasi Pembelian Saham");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        // Menyetujui Syarat Pembelian Saham
        MobileElement el8 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup");
        el8.click();
        System.out.println("Tick Box Syarat Pembelian Saham");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Konfirmasi
        MobileElement el9 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]");
        el9.click();
        System.out.println("Konfirmasi");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Invoice
        Assert.assertEquals(driver.findElementByXPath("//android.widget.TextView[@text='Menunggu Pembayaran']").getText(), "Menunggu Pembayaran");
        System.out.println("Invoice Muncul");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Batalkan Transaksi
        MobileElement el1_3 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]");
        el1_3.click();
        System.out.println("Batalkan Transaksi");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Batal
        MobileElement el2_3 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]");
        el2_3.click();
        System.out.println("Klik Ya");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        // Invoice Transaksi Gagal
        Assert.assertEquals(driver.findElementByXPath("//android.widget.TextView[@text='Transaksi Gagal']").getText(), "Transaksi Gagal");
        System.out.println("Transaksi Gagal");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Scroll
        ts.press(PointOption.point(826, 1800)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(862, 420)).release().perform();
        System.out.println("Scroll Success");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        // Pesan Ulang
        MobileElement el3_3 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView");
        el3_3.click();
        System.out.println("Pesan Ulang");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Kembali
        driver.navigate().back();
        System.out.println("Kembali");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);


        // Lihat Portfolio Saham
        MobileElement el10 = (MobileElement) driver.findElementByXPath("//android.widget.Button[@content-desc=\"Portofolio, tab, 3 of 4\"]");
        el10.click();
        System.out.println("Lihat Portfolio Saham");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Refresh Page
        //ts.press(PointOption.point(785, 380)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(1300))).moveTo(PointOption.point(785, 1900)).release().perform();
        ts.press(PointOption.point(screenSize.getWidth()/2, (int) (screenSize.height * 0.2))).waitAction(WaitOptions.waitOptions(Duration.ofMillis(500))).moveTo(PointOption.point(screenSize.getWidth()/2, (int) (screenSize.height * 0.8))).release().perform();
        System.out.println("Refresh Page");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Riwayat Transaksi
        MobileElement el11 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView");
        el11.click();
        System.out.println("Riwayat Transaksi");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // RIwayat Pendapatan
        MobileElement el12 = (MobileElement) driver.findElementByXPath("//android.widget.Button[@content-desc=\"Riwayat Pendapatan\"]/android.view.ViewGroup");
        el12.click();
        System.out.println("Riwayat Pendapatan");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Kembali
        MobileElement el13 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup");
        el13.click();
        System.out.println("Kembali");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Total Aset
        MobileElement el14 = (MobileElement) driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup");
        el14.click();
        System.out.println("Total Aset");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Daftar Aset
        Assert.assertEquals(driver.findElementByXPath("//android.widget.TextView[@text='Daftar Aset Kamu']").getText(), "Daftar Aset Kamu");
        System.out.println("Daftar Aset");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // Kembali
        driver.navigate().back();
        System.out.println("Kembali");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

    }
}
