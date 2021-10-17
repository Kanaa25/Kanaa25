package pl.testtest;

import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class Main {

    public static void main(String[] args) {

        System.setProperty("webdriver.chrome.driver", "C:\\WebDriver\\chromedriver.exe");
        ChromeDriver driver = new ChromeDriver();
        driver.get("http://www.selenium.waw.pl/");

        String login = "Kacper";
        String password = "password12";
        String phoneNumber = "060317090814";
        String expectedMessage = "Stworzono użytkownika "+login+"@selenium.waw.pl";

        driver.findElement(By.id("rcmloginuser")).sendKeys(login);
        driver.findElement(By.id("password")).sendKeys(password);
        driver.findElement(By.id("confirm_password")).sendKeys(password);

        new Select(driver.findElement(By.name("birthday-day"))).selectByIndex(7);
        new Select(driver.findElement(By.name("birthday-month"))).selectByIndex(2);
        new Select(driver.findElement(By.name("birthday-year"))).selectByVisibleText("1980");

        driver.findElement(By.xpath("//input[@value = 'K']")).click();
        driver.findElement(By.name("phone")).sendKeys(phoneNumber);
        driver.findElement(By.id("rcmloginsubmit")).click();

        String message = driver.findElement(By.xpath("//thead//td")).getText();

        if(message.equalsIgnoreCase(expectedMessage)){
            System.out.println("Test passed for user: "+login);
        }
        else{
            System.out.println("Test failed. Actual message: "+ message);
        }
        driver.quit();
    }
}