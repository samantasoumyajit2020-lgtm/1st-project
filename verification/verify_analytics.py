import os
from playwright.sync_api import sync_playwright

def verify_analytics():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the analytics.html file
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'public/analytics.html')
        print(f"Loading: file://{file_path}")
        page.goto(f'file://{file_path}')

        # Take a screenshot
        os.makedirs('verification', exist_ok=True)
        screenshot_path = 'verification/analytics_screenshot.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        # Check if the elements with aria-labels exist
        try:
            if page.get_by_label("Go back").count() > 0:
                print("Found 'Go back' button")
            else:
                print("ERROR: 'Go back' button not found")

            if page.get_by_label("Home").count() > 0:
                print("Found 'Home' link")

            if page.get_by_label("Analytics").count() > 0:
                print("Found 'Analytics' link")
        except Exception as e:
            print(f"Error checking labels: {e}")

        browser.close()

if __name__ == "__main__":
    verify_analytics()
