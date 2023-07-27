import playwright
from playwright.async_api import async_playwright
import asyncio

POST_NUMBER = 264148
LAST_POST_NUMBER = 264300
NEED_TO_SAVE = True
N = 5

async def fetch(post_number: int, page):
    url = f'https://debank.com/stream/{post_number}'
    if post_number == POST_NUMBER:
        t = 5000
    else:
        t = 3000
    await page.goto(url, timeout=t)
    try:
        await page.wait_for_selector('button.Button_button__1yaWD.Button_is_primary__1b4PX.RichTextView_joinBtn__3dHYH',
                                     timeout=t)
    except:
        print(f'No Draw | {post_number}')
        return



    button = await page.query_selector('button.Button_button__1yaWD.Button_is_primary__1b4PX.RichTextView_joinBtn__3dHYH')
    if button:
        button_text = await page.inner_text('button.Button_button__1yaWD.Button_is_primary__1b4PX.RichTextView_joinBtn__3dHYH')
        if 'Join the Draw' in button_text:
            if NEED_TO_SAVE:
                with open('draws.txt', 'a') as file:
                    file.write(f'https://debank.com/stream/{post_number}\n')
                    print(f'NEW DRAW | {post_number}')
        else:
            print(f'No Draw | {post_number}')
    else:
        print(f'No Draw | {post_number}')

async def main():
    async with async_playwright() as p:
        print('Ну пошла пизда по кочкам...')
        browser = await p.chromium.launch(headless=False)
        print('...')
        page = await browser.new_page()
        print('О, начинаю ебать')
        for i in range(POST_NUMBER, LAST_POST_NUMBER + 1):
            await fetch(i, page)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
