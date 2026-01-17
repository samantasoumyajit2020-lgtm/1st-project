
from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:3000/analytics.html")

    # Verify Back Button
    back_btn = page.locator(".back-btn")
    expect(back_btn).to_have_attribute("aria-label", "Go back")
    # Verify SVG inside back button has aria-hidden
    back_svg = back_btn.locator("svg")
    expect(back_svg).to_have_attribute("aria-hidden", "true")

    print("Back button verification passed.")

    # Verify Navigation Links
    nav = page.locator(".bottom-nav")

    # Home
    home_link = nav.locator("a.nav-item").nth(0)
    expect(home_link).to_have_attribute("aria-label", "Home")
    expect(home_link.locator("svg")).to_have_attribute("aria-hidden", "true")
    print("Home link verification passed.")

    # Search
    search_link = nav.locator("a.nav-item").nth(1)
    expect(search_link).to_have_attribute("aria-label", "Search")
    expect(search_link.locator("svg")).to_have_attribute("aria-hidden", "true")
    print("Search link verification passed.")

    # Analytics (Active)
    analytics_link = nav.locator("a.nav-item").nth(2)
    expect(analytics_link).to_have_attribute("aria-label", "Analytics")
    expect(analytics_link).to_have_attribute("aria-current", "page")
    expect(analytics_link.locator("svg")).to_have_attribute("aria-hidden", "true")
    print("Analytics link verification passed.")

    # Profile
    profile_link = nav.locator("a.nav-item").nth(3)
    expect(profile_link).to_have_attribute("aria-label", "Profile")
    expect(profile_link.locator("svg")).to_have_attribute("aria-hidden", "true")
    print("Profile link verification passed.")

    # Verify decorative icons in cards
    savings_icon = page.locator(".savings-icon svg")
    expect(savings_icon).to_have_attribute("aria-hidden", "true")

    stat_icon_products = page.locator(".icon-products svg")
    expect(stat_icon_products).to_have_attribute("aria-hidden", "true")

    stat_icon_waste = page.locator(".icon-waste svg")
    expect(stat_icon_waste).to_have_attribute("aria-hidden", "true")
    print("Decorative icons verification passed.")

    # Take screenshot
    page.screenshot(path="verification/analytics_accessibility.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
