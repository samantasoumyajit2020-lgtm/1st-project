from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file directly
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'public', 'analytics.html')
        page.goto(f'file://{file_path}')

        print("Checking Back Button...")
        back_btn = page.locator('.back-btn')
        assert back_btn.get_attribute('aria-label') == 'Go back'
        assert back_btn.get_attribute('title') == 'Go back'
        svg = back_btn.locator('svg')
        assert svg.get_attribute('aria-hidden') == 'true'

        print("Checking Bottom Nav...")
        nav_items = page.locator('.nav-item')

        # Home
        home = nav_items.nth(0)
        assert home.get_attribute('aria-label') == 'Home'
        assert home.get_attribute('title') == 'Home'
        assert home.locator('svg').get_attribute('aria-hidden') == 'true'

        # Search
        search = nav_items.nth(1)
        assert search.get_attribute('aria-label') == 'Search'
        assert search.get_attribute('title') == 'Search'

        # Analytics (Active)
        analytics = nav_items.nth(2)
        assert analytics.get_attribute('aria-label') == 'Analytics'
        assert analytics.get_attribute('title') == 'Analytics'
        assert analytics.get_attribute('aria-current') == 'page'

        # Profile
        profile = nav_items.nth(3)
        assert profile.get_attribute('aria-label') == 'Profile'
        assert profile.get_attribute('title') == 'Profile'

        print("All assertions passed!")

        # Screenshot
        page.screenshot(path='verification/analytics_verified.png')
        print("Screenshot saved.")

        browser.close()

if __name__ == '__main__':
    run()
