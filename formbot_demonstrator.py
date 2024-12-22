import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# My Browser
My_Browser = 'firefox'

def get_driver(browser='chrome'):
    if browser.lower() == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif browser.lower() == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    elif browser.lower() == 'edge':
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service)
    else:
        raise ValueError("Unsupported browser! Choose between 'chrome', 'firefox', or 'edge'.")

# Initialize the driver
driver = get_driver(My_Browser)


for i in range(3):
    Google_Form_URL = "https://docs.google.com/forms/d/e/1FAIpQLScVk-lxhRlXEcsqH1x3Xrl0B0XsQT6wc8f9baijIYVTaZooEA/viewform?usp=dialog"
    driver.get(Google_Form_URL)
    form_action_url = driver.find_element(By.XPATH, "//form").get_attribute("action")
    # Store the form data
    form_data = {}

    # Find all input fields and radio groups and list elements
    input_elements = driver.find_elements(By.XPATH, "//input | //textarea")
    radio_group = driver.find_elements(By.XPATH, "//div[@role='radiogroup']")
    list_element = driver.find_elements(By.XPATH,"//div[@role='list']")

    # Iterate through list elements
    if list_element:
        for index,list_ele in enumerate(list_element):
            try:
                list_checkboxes = list_ele.find_elements(By.XPATH,".//div[@role='checkbox']")
                list_options = [list_checkbox.get_attribute('aria-label') or "" for list_checkbox in list_checkboxes]
                if list_options:
                    form_data[f"Form_list {index+1}"]={"type":"list","options":list_options,"value":list_options[0]}
                else:
                    print(f"No check box found{index+1}")
            except Exception as e:
                print(f"error Processing list_elements{index+1}:{e}")

    # Iterate through radio buttons
    if radio_group:
        for index, group in enumerate(radio_group):
            print("Radiogroup found:")
            try:
                radio_buttons = group.find_elements(By.XPATH, ".//div[@role='radio']")
                options = [radio_button.get_attribute('aria-label') or "" for radio_button in radio_buttons]
                if options:
                    form_data[f"Radio Group {index + 1}"] = {"type": "radio", "options": options, "value": options[0]}  # Default: first option
                else:
                    print(f"No options found for Radio Group {index + 1}")
            except Exception as e:
                print(f"Error processing Radio Group {index + 1}: {e}")

    # Iterate through input elements
    if input_elements:
        for index, input_ele in enumerate(input_elements):
            label_id = input_ele.get_attribute("aria-labelledby")
            heading_text = []
            if label_id:
                for id_no in label_id.split():
                    try:
                        heading_element = driver.find_element(By.ID, id_no)
                        heading_text.append(heading_element.text.strip())
                    except NoSuchElementException:
                        print(f"Element with ID {id_no} not found! Skipping...")
                        continue  # Skip to the next ID if not found
            combined_heading = " ".join(heading_text)
            print(f"Heading: {combined_heading}")
            form_data[f"Input Field {index + 1}"] = {"type": "text", "heading": combined_heading, "value": "Sample Answer"}  # Default: "Sample Answer"

    # Filling  the form
    for field_name, field_details in form_data.items():
        if field_details["type"] == "text":
            # Locate the input field and fill in the value
            for input_ele in input_elements:
                label_id = input_ele.get_attribute("aria-labelledby")
                label_type = input_ele.get_attribute('type')
                heading_text = []
                if label_id:
                    for id_no in label_id.split():
                        try:
                            heading_element = driver.find_element(By.ID, id_no)
                            heading_text.append(heading_element.text.strip())
                        except NoSuchElementException:
                            continue
                    if " ".join(heading_text) == field_details["heading"]:
                        if label_type == "email":
                            field_details["value"] = "Hacked@gmail.com"
                            input_ele.send_keys(field_details["value"])
                        else:
                            input_ele.send_keys(field_details["value"])
                            break
        elif field_details["type"] == "radio":
            # Select the radio button
            group_index = int(field_name.split()[-1]) - 1
            radio_buttons = radio_group[group_index].find_elements(By.XPATH, ".//div[@role='radio']")
            for radio_button in radio_buttons:
                if radio_button.get_attribute("aria-label") == field_details["value"]:
                    radio_button.click()
                    break
        elif field_details["type"] == 'list':
            # Select the check box
            group_index = int(field_name.split()[-1])-1
            current_list = list_element[group_index]
            list_checkboxes = current_list.find_elements(By.XPATH,".//div[@role='checkbox']")
            for list_checkbox in list_checkboxes:
                option_label = list_checkbox.get_attribute("aria-label")
                is_checked = list_checkbox.get_attribute("aria-checked")
                if option_label == field_details['value']:
                    if is_checked == "true":
                        print(f"option '{option_label}' is already selected. Skipping click")
                    else:
                        print(f"Clicking option '{option_label}'")
                        list_checkbox.click()
                    break

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']/ancestor::div[@role='button']")
    submit_button.click()


driver.quit()

print("Form submitted successfully!")