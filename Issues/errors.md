# Attempting to click the `More` button on a user's profile

couldn't click the report user buttons. 
I didn't get the regex xpath selection quite right.
This is always the most difficult part of making a LinkedIn bot.
The most reoccuring theme.

<br>

**An error occurred: Message: invalid selector: Unable to locate an element with the xpath expression**
```html
"//button[contains(@id, "ember* profile-overflow-action")]/svg" because of the following error:
```

<br>

**SyntaxError: Failed to execute 'evaluate' on 'Document': The string**
```bash
# Error messages:

'"//button[contains(@id, "ember* profile-overflow-action")]/svg"' is not a valid XPath expression.
  (Session info: chrome=132.0.6834.83);
  For documentation on this error, please visit:
  https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#invalid-selector-exception
```

## XPath values attempted

`<span>More</span>`

`//*[@id="ember69-profile-overflow-action"]/span`

`report_xpath = '//*[@id="ember76"]/span'`

```python
def report_fake_user(self):
```

I did get it to click the `More` button once; however, was unsuccsesful on subsequent attempts.

<br>

### Janurary 22 2025

- Attempts to successfully run the `report_fake_user()` method were unsuccessful.

- Unit Test of `report_fake_user()` method : Failed

- Error messages, when running both `scammer_bait.py`, and when running `report-fake-user-function-test.py`:
```bash
An error occurred: Message: element not interactable

Login successful.
Attempting to click 'More' button with XPath: //*[starts-with(@id, 'ember') and contains(@id, '-profile-overflow-action')]
Found 2 element(s) matching XPath: //*[starts-with(@id, 'ember') and contains(@id, '-profile-overflow-action')]
Element 1: button
Element 2: button
An error occurred while reporting the fake user: Message:

Current URL: https://www.linkedin.com/in/donnie-thompson-b842532a6/
Page source: <html lang="en" class="theme theme--mercado app-loader--default artdeco"><head>
    <script nonce="">!function(i,n){void 0!==i.addEventListener&&void 0!==i.hidden&&(n.liVisibilityChangeListener=function(){i.hidden&&(n.liHasWindowHidden=!0)},i.addEventListener("visibilitychange",n.liVisibilityChangeListener))}(document,window);</script>
    <meta name="trusted-types" content="script-src-attr 'none'; require-trusted-types-for 'script'; trusted-types 'allow-duplicates' default jSecure highcharts do...
```


