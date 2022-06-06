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
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
//import org.testng.Assert;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;
import java.util.concurrent.TimeUnit;

class AndroidAppium {

    WebDriver driver;

    @Before
    public void setUp() throws MalformedURLException {
        // Created object of DesiredCapabilities class.
        DesiredCapabilities dc = new DesiredCapabilities();

        dc.setCapability(MobileCapabilityType.DEVICE_NAME, "emulator-5554");
        dc.setCapability("platformName", "Android");
        dc.setCapability("appPackage", "com.byznis.byniz");
        dc.setCapability("appActivity", "host.exp.exponent.MainActivity");

        AndroidDriver<AndroidElement> driver = new AndroidDriver<AndroidElement>(new URL("http://127.0.0.1:4723/wd/hub"), dc);
    }

    @Test
    public void firstTest() {
        // LOGIN
        MobileElement el1 = (MobileElement) driver.findElement(By.xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"));
        el1.click();
        System.out.println("Klik Masuk");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        MobileElement el2 = (MobileElement) driver.findElement(By.xpath("//android.widget.EditText[@text='Alamat Email']"));
        el2.sendKeys("test_user@gmail.com");
        System.out.println("Email");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        MobileElement el3 = (MobileElement) driver.findElement(By.xpath("//android.widget.EditText[@text='Kata Sandi']"));
        el3.sendKeys("TestUser001!");
        System.out.println("Password");
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        MobileElement el4 = (MobileElement) driver.findElement(By.xpath("//android.widget.TextView[@text='Masuk']"));
        el4.click();
        System.out.println("Login Success");
    }

}
