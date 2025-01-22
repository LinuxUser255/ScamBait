# Attempting to click the report user three dot elipsies and submit

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

## Other than this, everything is working fine!


More

<span>More</span>

//*[@id="ember69-profile-overflow-action"]/span

report_xpath = '//*[@id="ember76"]/span'

```python
def report_fake_user(self):
```

it's clicking the More button, however thats a drop down selection and it's not clicking on the report
