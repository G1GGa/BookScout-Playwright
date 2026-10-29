#import lybraries
import csv
from playwright.sync_api import sync_playwright

#open browser with playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")
#find elements in web all pages
    box = []
    while True:
        all_elements = page.query_selector_all(".product_pod")
        for element in all_elements:
            dictionary = {
                "Title": element.query_selector("h3 a").get_attribute("title"),
                "Price": float(element.query_selector("p.price_color").inner_text().replace("£", ""))
            }
            box.append(dictionary)
        #if/else logic for "next button"
        next_button = page.query_selector("li.next a")
        if next_button:
            next_button.click()
            page.wait_for_load_state("networkidle")
        else:
            break 

#write all elements in csv
fieldnames = ["Title","Price"]
with open("books.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  
    writer.writerows(box) 


