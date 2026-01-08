from playwright.sync_api import Page, expect, sync_playwright

def verify_analytics_a11y(page: Page):
    # Navigate to the analytics page
    page.goto("http://localhost:3000/analytics.html")

    # Check that the back button has the correct aria-label
    back_btn = page.locator("button.back-btn")
    expect(back_btn).to_have_attribute("aria-label", "Go back")

    # Check that the SVGs inside the back button are hidden from screen readers
    back_svg = back_btn.locator("svg")
    expect(back_svg).to_have_attribute("aria-hidden", "true")

    # Check navigation items
    home_link = page.get_by_role("link", name="Home")
    expect(home_link).to_be_visible()

    search_link = page.get_by_role("link", name="Search")
    expect(search_link).to_be_visible()

    analytics_link = page.get_by_role("link", name="Analytics")
    expect(analytics_link).to_be_visible()
    expect(analytics_link).to_have_attribute("aria-current", "page")

    profile_link = page.get_by_role("link", name="Profile")
    expect(profile_link).to_be_visible()

    # Take a screenshot to verify visual regression (should look the same)
    page.screenshot(path="verification/analytics_a11y.png")
    print("Verification successful!")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_analytics_a11y(page)
        finally:
            browser.close()
