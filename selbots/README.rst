selbots
============
https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html

testing
============
.. code-block:: shell

  poetry install
  brew install geckodriver
  poetry run pytest -v -n auto

bug hunt
============
rustic escentuals needs to get around cloudflare

mountain rose herbs doing the arrow down for postal code city suggestion can result in the incorrect city (for pennsylvania). I mean it didn't but if you run with a head you can see the potential. I guess it doesn't matter since shipping is on a postcode basis anyway?

mountain rose herbs has nondeterministic test failure

selenium
============
How to convert a class name into a local CSS SELECTOR (for when you are finding a nested element from an already selected element)
<span class="input-group-addon plus-option noselect">+</span>
element.find_element(By.CSS_SELECTOR, ".input-group-addon.plus-option.noselect").click()