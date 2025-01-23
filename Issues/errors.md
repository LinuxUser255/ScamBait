# Error log

All errors are regarding the successfully locating and clicking of elements/xpaths in the
page source.

<br>

Sometimes it works, but most the time it does not.
The front end source code might be very dynamic and changes too much for a solid aim to stay on point.

- couldn't click the report user buttons:
- I didn't get the regex xpath selection quite right.
- This is always the most difficult part of making a LinkedIn bot.

```bash
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

Other than the element locating and clicking, the bot works as intended

<br>


###  Janurary 22 2025 - Unit testing:

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

<br>


### Janurary 23 2025 Unit testing:
```bash
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

<br>

updated/fixed the ` DeprecationWarning: 'telnetlib' is deprecated and slated for removal in Python 3.13
  from telnetlib import EC` issue

_How to fix the telnetlib problem_
To resolve the deprecation warning about 'telnetlib', you need to update your import statement for the `EC` (Expected Conditions) class. The warning suggests that you're importing `EC` from `telnetlib`, which is incorrect and deprecated. Instead, you should import it from Selenium's `expected_conditions` module.

Here's how to fix it:

1. First, locate the line in your code where you're importing `EC`. It might look something like this:

```python
from telnetlib import EC
```

2. Replace that line with the correct import statement:

**File: /home/linux/Projects/Bots/Experimental/ScamBait/scammer_bait.py**
```python
from selenium.webdriver.support import expected_conditions as EC
```

3. If you haven't already, make sure you have the following import at the top of your file:

```python
from selenium.webdriver.support.wait import WebDriverWait
```

4. After making these changes, the warning about 'telnetlib' should be resolved.

This change ensures that you're using the correct `EC` class from Selenium's expected conditions module, which is designed to work with WebDriverWait for handling dynamic elements on web pages.

Remember to make this change in all files where you might be using the incorrect import. If you're using an IDE, you can usually perform a project-wide search and replace to ensure you catch all instances of the incorrect import.




**and problem persists**
```bash
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

I will now attempt to use the login button location functionality as a template for all other button 
locating and clicking operations, and refer to the Selenium documentation**
**here it is**
```python
    def sign_in(self):
        try:
            self.driver.get('https://www.linkedin.com/login')
            self.driver.find_element(By.ID, "username").send_keys(config.email)
            self.driver.find_element(By.ID, "password").send_keys(config.password)
            time.sleep(8)
            sign_in_button_xpath = ("//button[contains(@class, 'btn__primary--large') and contains(@type, 'submit') "
                                    "and (contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
                                    "'abcdefghijklmnopqrstuvwxyz'), 'sign in') or contains(translate(., "
                                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'signin'))]")
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath))
            )
            sign_in_button.click()
            if self.driver.current_url == 'https://www.linkedin.com/feed/':
                print("Login successful.")
        except Exception as e:
            print(f"An error occurred during sign-in: {str(e)}")
```

## Applied the variable value format, and problem persists
**Error message:**
```bash
Login successful.
Attempting to click 'More' button with XPath: //*[starts-with(@id, 'ember') and contains(@id, '-profile-overflow-action')]
Found 2 element(s) matching XPath: //*[starts-with(@id, 'ember') and contains(@id, '-profile-overflow-action')]
Element 1: button
Element 2: button
An error occurred while reporting the fake user: Message: 

Current URL: https://www.linkedin.com/in/donnie-thompson-b842532a6/
Page source: <html lang="en" class="theme theme--mercado app-loader--default artdeco"><head>
    <script nonce="">!function(i,n){void 0!==i.addEventListener&&void 0!==i.hidden&&(n.liVisibilityChangeListener=function(){i.hidden&&(n.liHasWindowHidden=!0)},i.addEventListener("visibilitychange",n.liVisibilityChangeListener))}(document,window);</script>
    <meta name="trusted-types" content="script-src-attr 'none'; require-trusted-types-for 'script'; trusted-types 'allow-duplicates' default jSecure highcharts do..
```

<br>

### Prompt used:
Use the `sign_in_button_xpath` variable as a template to refactor the  ` more_button_xpath` variable. 

**Response:**
Based on the provided information and the template, 
here's a refactored version of the `more_button_xpath` variable:

**File: /home/linux/Projects/Bots/Experimental/ScamBait/Issues/ElementsAndXPaths.md**
```python
more_button_xpath = ("//button[contains(@class, 'artdeco-dropdown__trigger') and "
                     "contains(@class, 'artdeco-button--secondary') and "
                     "contains(@aria-label, 'More actions')]//span[contains(text(), 'More')]")
```

This XPath:
1. Targets a `button` element
2. Checks for specific classes: 'artdeco-dropdown__trigger' and 'artdeco-button--secondary'
3. Looks for the aria-label containing 'More actions'
4. Finds a `span` child element with the text 'More'

This approach is more robust than using specific IDs (like 'ember65') which may change dynamically, 
and it follows the structure of the `sign_in_button_xpath` template you provided.

### New errors:
```bash
Login successful.
An error occurred while reporting the fake user: name 'more_button_xpath' is not defined
Current URL: https://www.linkedin.com/in/donnie-thompson-b842532a6/
Page source: <html lang="en" class="theme theme--mercado app-loader--default artdeco"><head>
    <script nonce="">!function(i,n){void 0!==i.addEventListener&&void 0!==i.hidden&&(n.liVisibilityChangeListener=function(){i.hidden&&(n.liHasWindowHidden=!0)},i.addEventListener("visibilitychange",n.liVisibilityChangeListener))}(document,window);</script>
    <meta name="trusted-types" content="script-src-attr 'none'; require-trusted-types-for 'script'; trusted-types 'allow-duplicates' default jSecure highcharts do...
Total number of buttons on the page: 60
Button 1: Class: mr4 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view, Text: , Aria-label: None
Button 2: Class: artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view, Text: , Aria-label: None
Button 3: Class: artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view ml4, Text: , Aria-label: None
Button 4: Class: global-nav__a11y-menu-close artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view, Text: , Aria-label: None
Button 5: Class: search-global-typeahead__collapsed-search-button, Text: , Aria-label: Click to start a search
```
### Claims: ` name 'more_button_xpath' is not defined`

__Rechecked the More button element__
```html
<button aria-expanded="false" aria-label="More actions" id="ember65-profile-overflow-action" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view dftrUCpNznrIIjSqQSUDxUiKCAlHBJdQHTHg
      artdeco-button artdeco-button--secondary artdeco-button--muted
      artdeco-button--2
      
      " type="button" tabindex="0">
      <span>More</span>
      
<!----></button>
```
**the xpath**
```html
//*[@id="ember65-profile-overflow-action"]
```
**the Full xpath**
```html
/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button
```

**Same problem, will need to investigate, trouble shoot the `more_button_xpath` variable**
```bash

An error occurred while reporting the fake user: 
name 'more_button_xpath' is not defined

Current URL: https://www.linkedin.com/in/donnie-thompson-b842532a6/
Page source: <html lang="en" class="theme theme--mercado app-loader--default artdeco"><head>
    <script nonce="">!function(i,n){void 0!==i.addEventListener&&void 0!==i.hidden&&(n.liVisibilityChangeListener=function(){i.hidden&&(n.liHasWindowHidden=!0)},i.addEventListener("visibilitychange",n.liVisibilityChangeListener))}(document,window);</script>
    <meta name="trusted-types" content="script-src-attr 'none'; require-trusted-types-for 'script'; trusted-types 'allow-duplicates' default jSecure highcharts do...
Total number of buttons on the page: 60
Button 1: Class: mr4 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view, Text: , Aria-label: None
Button 2: Class: artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view, Text: , Aria-label: None
Button 3: Class: artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view ml4, Text: , Aria-label: None
Button 4: Class: global-nav__a11y-menu-close artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view, Text: , Aria-label: None
Button 5: Class: search-global-typeahead__collapsed-search-button, Text: , Aria-label: Click to start a search
Browser session persist...
```

When running scammer_bait.test-More-Button.py, I receive this error:
"An error occurred while reporting the fake user: name 'more_button_xpath' is not defined"
Explain the cause of this error, and from where in the code-base is it originating?

**_I added the more button xpath to the class instance_**
```python
self.more_button_xpath = ("//button[contains(@class, 'artdeco-dropdown__trigger') and "
                                  "contains(@class, 'artdeco-button--secondary') and "
                                  "contains(@aria-label, 'More actions')]//span[contains(text(), 'More')]")
```
And refactored the method click the More button
```python
 def click_more_button(self):
        try:
            # Now you can use self.more_button_xpath here
            more_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.more_button_xpath))
            )
            more_button.click()
```

And same result:
An error occurred while reporting the fake user: name 'more_button_xpath' is not defined

But I'm not trying to report the fake user.
Just find and click the More button

Turns out I wasn't calling the method in the run_bot() function
```python
    def run_bot(self):
        """The methods are called sequentially."""
        self.sign_in()
        self.get_opentowork_url()
        self.find_posts_comments_by_fake_users()  # This method needs to be implemented
        self.get_fakeuser_url()
        # self.fakeuser_url()
        self.click_more_button() # <-- That was commented out
#        self.report_fake_user()  # Make sure this line is uncommented
        browser_persist()
```

I also commented out the entire `self.report_fake_user()` method

### How I solved the more_button_xpath is not defined and accessable problem
Solved that issue by making sure the more_button was accessable by placing it in the class
as a way to define it , and make that defined value accessable to all methods in the code.
At whcih point, I could reference it in the `click_more_button`  method. As illustrated above.

now the errror message is:
**Help me understand what this error means, and how to fix it.**
```bash
An error occurred while clicking the 'More' button: Message: 

Current URL: https://www.linkedin.com/in/donnie-thompson-b842532a6/
Page source: 

<html lang="en" class="theme theme--mercado app-loader--default artdeco"><head>
    <script 
    
    nonce="">!function(i,n){void 0!==i.addEventListener&&void 0!==i.hidden&&(n.liVisibilityChangeListener=function()
    { i.hidden&&(n.liHasWindowHidden=!0)},i.addEventListener("visibilitychange",n.liVisibilityChangeListener))}(document,window);
   
    </script>
    
    <meta name="trusted-types" 
          content="script-src-attr 'none'; 
          require-trusted-types-for 'script'; 
          trusted-types 'allow-duplicates' default jSecure highcharts do...
````
Browser session persist...```
No details, just page source code. Will need to read through and analyze that
and make proper changes

### Possible explanation and soulution
This error message indicates that there was a problem when trying to click the 'More' button on the LinkedIn profile page. Let's break down the error and discuss potential solutions:

1. Empty error message:
   The error message is empty (`Message: `), which suggests that Selenium encountered an issue but didn't provide a specific error description. This can happen when the element is not found or when there's a timing issue.

2. Current URL:
   The URL shows that the bot is on the correct profile page, so navigation isn't the issue.

3. Page source:
   The page source snippet doesn't show the full HTML, but it does indicate that the page has loaded to some extent.

To address this issue, consider the following steps:

1. Wait for page load:
   Ensure that the page is fully loaded before attempting to click the 'More' button. Add an explicit wait:

   ```python
   WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
   ```

2. Scroll to the button:
   The 'More' button might be out of view. Try scrolling to it before clicking:

   ```python
   more_button = WebDriverWait(self.driver, 10).until(
       EC.presence_of_element_located((By.XPATH, self.more_button_xpath))
   )
   self.driver.execute_script("arguments[0].scrollIntoView();", more_button)
   ```

3. Use JavaScript to click:
   If Selenium can't click the button directly, try using JavaScript:

   ```python
   more_button = WebDriverWait(self.driver, 10).until(
       EC.presence_of_element_located((By.XPATH, self.more_button_xpath))
   )
   self.driver.execute_script("arguments[0].click();", more_button)
   ```

4. Check for overlays or popups:
   Ensure there are no overlays or popups blocking the button. You might need to handle these first.

5. Re-evaluate the XPath:
   The button's structure might have changed. Verify the XPath is still correct by inspecting the page source. You might need to update `self.more_button_xpath`.

6. Add more detailed error handling:
   Enhance your error handling to provide more information:

   ```python
   try:
       more_button = WebDriverWait(self.driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, self.more_button_xpath))
       )
       more_button.click()
   except Exception as e:
       print(f"An error occurred while clicking the 'More' button: {str(e)}")
       print(f"Button visibility: {more_button.is_displayed() if 'more_button' in locals() else 'Not found'}")
       print(f"Button enabled: {more_button.is_enabled() if 'more_button' in locals() else 'Not found'}")
   ```

7. Check for iframes:
   The button might be inside an iframe. If so, you'll need to switch to the iframe before interacting with the button.

Implement these suggestions one by one, testing after each change. This should help you identify and resolve the issue with clicking the 'More' button.



### Based on my code as is a current moment,  I am going to implement:

**Use JavaScript to click:**
```js
more_button = WebDriverWait(self.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, self.more_button_xpath))
)
self.driver.execute_script("arguments[0].click();", more_button)
```
**Re-evaluate the XPath:**
   The button's structure might have changed. 
  Verify the XPath is still correct by inspecting the page source. 
  You might need to update self.more_button_xpath.

**AND**

**Add more detailed error handling:**
   Enhance your error handling to provide more information:
class WebDriverWait:
pass

```python
try:
    more_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, self.more_button_xpath))
    )
    more_button.click()
except Exception as e:
    print(f"An error occurred while clicking the 'More' button: {str(e)}")
    print(f"Button visibility: {more_button.is_displayed() if 'more_button' in locals() else 'Not found'}")
    print(f"Button enabled: {more_button.is_enabled() if 'more_button' in locals() else 'Not found'}")
```

Getting closer. After implementing the JS, and verbose error messages, I belive it comes down to 
sorting out the xpath value...again

```bash
An error occurred while clicking the 'More' button: Message: 

Button visibility: Not found
Button enabled: Not found
```

<br>


**_Might need to do something mentiond in the first line of the element regarding and that drop down placed ontop of the button?_**
```html
<div id="ember66" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-left ember-view">

```
<!>
```html
  <button aria-expanded="false" aria-label="More actions" id="ember65-profile-overflow-action" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view dftrUCpNznrIIjSqQSUDxUiKCAlHBJdQHTHg
      artdeco-button artdeco-button--secondary artdeco-button--muted
      artdeco-button--2
      
      " type="button" tabindex="0">
      <span>More</span>
```

```html
<div id="ember66"
     class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-left ember-view">

   <button aria-expanded="false"
           aria-label="More actions"
           id="ember65-profile-overflow-action"
           class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom 
                ember-view dftrUCpNznrIIjSqQSUDxUiKCAlHBJdQHTHg
                artdeco-button artdeco-button--secondary artdeco-button--muted
                artdeco-button--2
      
      " type="button" tabindex="0">
      <span>More</span>
      <!---->
   </button>
   <div tabindex="-1" 
        aria-hidden="true" 
        id="ember68" 
        class="NWeoigmAqkTuOSlhXlCLKtGhSFqQQlFA artdeco-dropdown__content artdeco-dropdown--is-dropdown-element 
               artdeco-dropdown__content--justification-left artdeco-dropdown__content--placement-bottom ember-view">
      
   <div class="artdeco-dropdown__content-inner">

      <ul>
         <li>
            <!---->
```
```python
    def click_more_button(self):
        try:
            more_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.more_button_xpath))
            )
            #more_button.click() <-- using python to click the button. JS used below:
            self.driver.execute_script("arguments[0].click();", more_button)
            print("Successfully clicked 'More' button")
        except Exception as e:
            print(f"An error occurred while clicking the 'More' button: {str(e)}")
            print("Button visibility: Not found")
            print("Button enabled: Not found")
```
<br>

