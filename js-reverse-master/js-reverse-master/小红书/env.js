window = global;
delete global;
delete Buffer;
document = {}
canvas = {
    getContext:function () {}
}
document.createElement = function (ele) {
    if (ele == "canvas"){
        return canvas;
    }else if (ele == "div"){
        return {}
    }else if (ele == "h3"){
        return {}
    }
    //根据需要来补充标签返回对象

}
window.CanvasRenderingContext2D = function () {
}
window.HTMLCanvasElement = function () {
}
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
}
location = {
    "ancestorOrigins": {},
    "href": "https://www.xiaohongshu.com/explore?channel_id=homefeed.fashion_v3",
    "origin": "https://www.xiaohongshu.com",
    "protocol": "https:",
    "host": "www.xiaohongshu.com",
    "hostname": "www.xiaohongshu.com",
    "port": "",
    "pathname": "/explore",
    "search": "?channel_id=homefeed.fashion_v3",
    "hash": ""
}
window.devicePixelRatio = 1.0399999618530273
window.AudioContext = function (){}
document.documentElement = function (){}
window._webmsxyw = function (){}
window.localStorage = {
    getItem: function () {
    }
}

document.cookie = 'abRequestId=962b9322-e85f-533a-bac7-b704b8e713c1; xsecappid=xhs-pc-web; a1=18bb2c116d1davozu4yc2t8yyzy4bdk2lxv980kx450000105644; webId=bbfb0cce5cab1fff7ddff6b1741ed1c4; gid=yYDDJSyJ281yyYDDJSyyKC8Tfyf0hlu74vSJhC49Yvvuvj284DfTJY888y82K448Y8YqWKy0; webBuild=4.17.2; unread={%22ub%22:%22664574c5000000001e02c502%22%2C%22ue%22:%2266385aa1000000001e037c3a%22%2C%22uc%22:25}; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=3f769dc1-0a65-4514-b4c2-91976642fa2f'
//代理
// function get_environment(proxy_array) {
//     for (var i = 0; i < proxy_array.length; i++) {
//         if (proxy_array[i] !== 'Math') {
//             var handler = '{\n' +
//                 '    get: function(target, property, receiver) {\n' +
//                 '        if (property !== "Math" && property !== "isNaN") {  // 添加判断\n' +
//                 '            console.log("方法:", "get  ", "对象:", \'' +
//                 proxy_array[i] + '\' ,' +
//                 ' "  属性:", property, ' +
//                 ' "  属性类型:", typeof property, ' +
//                 // '"  属性值:", ' + 'target[property], ' +
//                 ' "  属性值类型:", typeof target[property]);\n' +
//                 '        }\n' +
//                 '        return target[property];\n' +
//                 '    },\n' +
//                 '    set: function(target, property, value, receiver) {\n' +
//                 '        if (property !== "Math" && property !== "isNaN") {  // 添加判断\n' +
//                 '            console.log("方法:", "set  ", "对象:", \'' +
//                 proxy_array[i] + '\' ,' +
//                 ' "  属性:", property, ' +
//                 ' "  属性类型:", typeof property, ' +
//                 // '"  属性值:", ' + 'target[property], ' +
//                 ' "  属性值类型:", typeof target[property]);\n' +
//                 '        }\n' +
//                 '        return Reflect.set(...arguments);\n' +
//                 '    }\n' +
//                 '}';
//
//             eval('try{\n' + proxy_array[i] + ';\n' +
//                 proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n' +
//                 proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}');
//         }
//     }
// }

proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', 'localStorage', 'sessionStorage'];
// get_environment(proxy_array);