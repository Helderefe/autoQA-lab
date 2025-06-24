# Selenium Automation Script - MercadoLibre Product Search

Author: Helder Fernando Marroquín Barragán  
Language: Python 3.x  
Browser: Google Chrome  
Tool: Selenium WebDriver

---

## Overview

This script automates a product search on MercadoLibre Mexico using Selenium WebDriver.  
It navigates through the following steps:

1. Accesses the MercadoLibre homepage.
2. Selects "México" as the country.
3. Searches for the term "Playstation 5".
4. Filters results to show only new items.
5. Selects "Estado de México" as the location.
6. Sorts results by highest price.
7. Extracts and displays the first five products with their names and prices.

---

## Requirements

- Python 3.7 or higher
- Google Chrome
- pip (Python package installer)

Install required packages using:

```bash
pip install selenium webdriver-manager
```

---

## File Structure

- `python mercadolibre_testaut.py`: The automation script.

---

## Key Technologies Used

- `selenium`: For browser automation
- `webdriver-manager`: To handle ChromeDriver installation
- `time`, `EC`, `WebDriverWait`: For synchronization and delay handling

---

## Output Example

```
1. PlayStation 5 Standard Edition - $15,000
2. Sony PS5 Digital Edition - $14,500
3. PlayStation 5 Bundle - $14,000
...
```

---

## Important Notes

- The script uses XPATH and class-based selectors which may break if MercadoLibre updates its UI.
- Error handling is included to avoid breaking on unexpected HTML structures.
- This script is intended for automation practice and demonstration purposes.

---

## Execution

Run the script using:

```bash
python mercadolibre_testaut.py: ejecuta el script.
```

The browser window will open, execute the automated steps, and display the results in the terminal.  
Press Enter when prompted to close the session.

---

## License

This project is for educational and internal testing use only.