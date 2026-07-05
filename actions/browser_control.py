def browse(url: str, headless: bool = True, screenshot_path: str | None = None) -> bool:
    """Open a page using Playwright if available. If not, print install instructions.

    Returns True if navigation (or fallback open) succeeded.
    """
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print('[Browser] Playwright not installed. Install with `pip install playwright` and run `playwright install`')
        return False

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless)
            page = browser.new_page()
            resp = page.goto(url, timeout=30000)
            status = resp.status if resp is not None else 'unknown'
            print(f'[Browser] Opened {url} (status {status})')
            if screenshot_path:
                page.screenshot(path=screenshot_path)
                print(f'[Browser] Screenshot saved to {screenshot_path}')
            browser.close()
        return True
    except Exception as e:
        print(f'[Browser] Playwright navigation failed: {e}')
        return False
