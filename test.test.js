// Generated by Selenium IDE
//npm install --save-dev mocha
//yarn add --dev mocha

//Add the drivers for Chrome web browser
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')
const chrome = require("selenium-webdriver/chrome")
const chromedriver = require("chromedriver")
chrome.setDefaultService(new chrome.ServiceBuilder(chromedriver.path).build());

describe('failed_login', function() {
  this.timeout(30000)
  let driver
  let vars

  beforeEach(async function() {
    driver = await new Builder().forBrowser('chrome').build()
    vars = {}
  })//End of beforeEach

  afterEach(async function() {
    await driver.quit();
  })//End of afterEach

  it('failed_login', async function() {
    await driver.get("http://demo.guru99.com/test/newtours/")
    await driver.manage().window().setRect(1440, 1080)

    const userName = await driver.findElement(By.name("userName"));
    await driver.wait(() => {
      return userName.isDisplayed();
    }, 15000);
    await driver.findElement(By.name("userName")).sendKeys("test@example.com")

    const password = await driver.findElement(By.name("password"));
    await driver.wait(() => {
      return password.isDisplayed();
    }, 15000);
    await driver.findElement(By.name("password")).sendKeys("wrongPassword")

    await driver.findElement(By.name("submit")).click()

    const message = await driver.findElement(By.tagName("span"));
    await driver.wait(() => {
      return message.isDisplayed();
    }, 15000);

    const actualMessage = await message.getText();
    const expectedMessage = 'Enter your userName and password correct';

    assert.equal(actualMessage, expectedMessage, 'an unexpected message was displayed');
  })//End of it

})//End of describe
