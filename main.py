from selenium import webdriver

# Exemple avec Chrome (assurez-vous d'avoir installé ChromeDriver)
driver = webdriver.Chrome()

# Ouvrir Google
driver.get("https://www.google.com")

# Fermer le navigateur
driver.quit()