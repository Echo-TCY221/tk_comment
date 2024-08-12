window = global

document = {}
document.all = {}  // 全局搜索document.all发现并没有检测，因此这里不补typeof
navigator = {}
navigator.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
document.createElement = function (name) {
    if (name == 'span') {
        return [{}]
    }
}
document.documentElement = '<html></html>'
document.createEvent = function () {
    return 'createEvent() { [native code] }'
}
document.createElement = function () {
    return 'createElement() { [native code] }'
}
window.requestAnimationFrame = function () {
    return 'requestAnimationFrame() { [native code] }'
}
window._sdkGlueVersionMap = {
    "sdkGlueVersion": "1.0.0.51",
    "bdmsVersion": "1.0.1.5",
    "captchaVersion": "4.0.2"
}
XMLHttpRequest = function () {
    return 'XMLHttpRequest() { [native code] }'
}

window.fetch = function () {
    return `(input, init) {
	        var _this6 = this;
	        var url, method;
	        if (IS_REQUEST_API_SUPPORTED && input instanceof Request) {
	          url = input.url;
	          method = input.method…`
}

window.onwheelx = {
    "_Ax": "0X21"
}

navigator.vendorSubs = {
    "ink": 1718453241914
}
window.innerWidth = 1920
window.innerHeight = 1080
window.outerWidth = 1914
window.outerHeight = 1026
window.screenX = 2563
window.screenY = 412
window.pageYOffset = 0
window.pageYOffset = 0
window.screen = {
    availWidth: 1536,
    availHeight: 824,
    availLeft: 0,
    availTop: 0,
    width: 	1536,
    height: 864,
    colorDepth: 24,
    pixelDepth: 24,
    isExtended: false,
    orientation: {
        type: "landscape-primary",
        onchange: null,
        angle: 0
    },
};
navigator.platform = 'Win32'
document.body = '<body></body>'
window.performance = {
    now: function() {
        return Date.now();
    }
};
// console.log(window.performance.now())

//上代理
// function get_enviroment(proxy_array) {
//     for (var i = 0; i < proxy_array.length; i++) {
//         handler = '{\n' +
//             '    get: function(target, property, receiver) {\n' +
//             '        console.log("方法:", "get  ", "对象:", ' +
//             '"' + proxy_array[i] + '" ,' +
//             '"  属性:", property, ' +
//             '"  属性类型:", ' + 'typeof property, ' +
//             // '"  属性值:", ' + 'target[property], ' +
//             '"  属性值类型:", typeof target[property]);\n' +
//             '        return target[property];\n' +
//             '    },\n' +
//             '    set: function(target, property, value, receiver) {\n' +
//             '        console.log("方法:", "set  ", "对象:", ' +
//             '"' + proxy_array[i] + '" ,' +
//             '"  属性:", property, ' +
//             '"  属性类型:", ' + 'typeof property, ' +
//             // '"  属性值:", ' + 'target[property], ' +
//             '"  属性值类型:", typeof target[property]);\n' +
//             '        return Reflect.set(...arguments);\n' +
//             '    }\n' +
//             '}'
//         eval('try{\n' + proxy_array[i] + ';\n'
//             + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
//             + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
//     }
// }

// proxy_array = ['window']
// get_enviroment(proxy_array);
