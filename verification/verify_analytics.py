from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file
        filepath = f"file://{os.getcwd()}/public/analytics.html"
        print(f"Loading {filepath}")
        page.goto(filepath)

        # Verify Back Button
        back_btn = page.locator("button.back-btn")
        expect(back_btn).to_have_attribute("aria-label", "Go back")
        print("Verified back button aria-label")

        # Verify Navigation Items
        # Home
        nav_home = page.locator("a.nav-item").nth(0)
        expect(nav_home).to_have_attribute("aria-label", "Home")
        print("Verified Home link aria-label")

        # Search
        nav_search = page.locator("a.nav-item").nth(1)
        expect(nav_search).to_have_attribute("aria-label", "Search")
        print("Verified Search link aria-label")

        # Analytics
        nav_analytics = page.locator("a.nav-item").nth(2)
        expect(nav_analytics).to_have_attribute("aria-label", "Analytics")
        expect(nav_analytics).to_have_attribute("aria-current", "page")
        print("Verified Analytics link aria-label and aria-current")

        # Profile
        nav_profile = page.locator("a.nav-item").nth(3)
        expect(nav_profile).to_have_attribute("aria-label", "Profile")
        print("Verified Profile link aria-label")

        # Take screenshot
        page.screenshot(path="verification/analytics_a11y.png")
        print("Screenshot saved to verification/analytics_a11y.png")

        browser.close()

if __name__ == "__main__":
    run()
