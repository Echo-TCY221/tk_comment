async function test() {
    let index = 2;
    const url = conf[index].url;

    const browser = await puppeteer.launch({
        headless: true
    });


    const page = await browser.newPage();
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i];
        await page.setCookie(cookie);
    }
    await page.goto(url);
    await page.waitForSelector('.semi-button', { visible: true });
    const targetIndex = await page.$$eval('.semi-button', (els) => {
        return els.findIndex(el => el.childNodes[0].innerText === '私信');
    })
    const target = (await page.$$('.semi-button'))[targetIndex];

    if (target) {
        setTimeout(async () => {
            target.click();
            setTimeout(async () => {
                await page.keyboard.sendCharacter('你好，可以交个朋友吗？');

                setTimeout(async () => {
                    const sendMsgBtn = await page.$('span[class*="send-msg-btn"]');
                    console.log(sendMsgBtn, '获取元素');

                    if (sendMsgBtn) {
                        sendMsgBtn.click();
                        console.log('发送成功');
                        // page.close();
                    }
                }, 1000)
            }, 1000)
        }, 5500)
    }


    // const target = (Array.from(await page.$$('.semi-button'))).find(node => {
    //     console.log(node.offsetTop, 'offsetTop');
    //     return node;
    // });

    // console.log(target, '??????');




    // 输入用户名和密码
    // await page.type('#username', 'admin');
    // await page.type('#password', '123456');
    // await page.click('#loginButton');

    // 验证登录成功
    // const url = await page.url();


    // // 获取消息元素的文本内容
    // const message = await page.evaluate(() => document.querySelector('#message').textContent);

    // // 打印消息文本
    // console.log('Login message:', message);
    // // 保存登录结果截图到本地
    // await page.screenshot({ path: 'login.png' });
    // // 关闭无头浏览器
    // await browser.close();
}