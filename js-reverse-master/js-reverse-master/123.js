const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  const tiktokUrl = 'https://www.douyin.com/user/MS4wLjABAAAAus0kLi-YOQ9NFTLL_ab3qkHAO_dAM4_df8nYDbcJ2iw'; // 替换为实际的抖音主页链接
  await page.goto(tiktokUrl, { waitUntil: 'networkidle2' });

  try {
    // 等待私信按钮并点击
    await page.waitForSelector('button.some-more-stable-class', { visible: true });
    await page.click('button.some-more-stable-class');

    // 等待私信页面加载完毕
    await page.waitForSelector('div.DraftEditor-editorContainer', { visible: true });

    // 使用 page.evaluate() 输入文本
    await page.evaluate(() => {
      const editor = document.querySelector('div.DraftEditor-editorContainer');
      if (editor && editor.contentEditable === 'true') {
        const range = document.createRange();
        range.selectNodeContents(editor);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        editor.focus();
        document.execCommand('insertText', false, '你好，这是自动发送的私信！');
      }
    });

    // 点击发送按钮（确保选择器正确）
    await page.click('span.sCp7KhBv.e2e-send-msg-btn');

    console.log('私信发送成功！');

  } catch (error) {
    console.error('发送私信失败：', error);
  }

  await browser.close();
})();