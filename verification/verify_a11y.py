
from playwright.sync_api import sync_playwright

def verify_analytics_accessibility():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file directly since we are testing static HTML changes
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/public/analytics.html")

        # 1. Verify Back Button
        back_btn = page.locator(".back-btn")
        aria_label = back_btn.get_attribute("aria-label")
        print(f"Back button aria-label: {aria_label}")
        if aria_label != "Go back":
            print("ERROR: Back button missing correct aria-label")

        # Verify SVG hidden in back button
        back_svg = back_btn.locator("svg")
        svg_hidden = back_svg.get_attribute("aria-hidden")
        print(f"Back button SVG aria-hidden: {svg_hidden}")
        if svg_hidden != "true":
            print("ERROR: Back button SVG missing aria-hidden='true'")

        # 2. Verify Navigation Items
        nav_items = page.locator(".nav-item")
        count = nav_items.count()
        print(f"Found {count} nav items")

        expected_labels = ["Home", "Search", "Analytics", "Profile"]

        for i in range(count):
            item = nav_items.nth(i)
            label = item.get_attribute("aria-label")
            print(f"Nav item {i} aria-label: {label}")

            if label != expected_labels[i]:
                print(f"ERROR: Nav item {i} expected '{expected_labels[i]}' but got '{label}'")

            # Verify SVG hidden
            svg = item.locator("svg")
            hidden = svg.get_attribute("aria-hidden")
            if hidden != "true":
                print(f"ERROR: Nav item {i} SVG missing aria-hidden='true'")

            # Check active state for Analytics (index 2)
            if i == 2:
                current = item.get_attribute("aria-current")
                print(f"Nav item {i} aria-current: {current}")
                if current != "page":
                    print(f"ERROR: Analytics nav item missing aria-current='page'")

        page.screenshot(path="verification/analytics_a11y.png")
        browser.close()

if __name__ == "__main__":
    verify_analytics_accessibility()
