window = global
delete global;
delete Buffer;
navigator = {}
document = {}
window.requestAnimationFrame = function () {

}
XMLHttpRequest = function () {
}
screen = {
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
}
//上代理
function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        console.log("方法:", "set  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return Reflect.set(...arguments);\n' +
            '    }\n' +
            '}'
        eval('try{\n' + proxy_array[i] + ';\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}
window.performance = {
    now: function() {
        return Date.now();
    }
};
window._sdkGlueVersionMap = {
    "sdkGlueVersion": "1.0.0.51",
    "bdmsVersion": "1.0.1.5",
    "captchaVersion": "4.0.2"
}
window.pageYOffset = 0

// console.log(window.performance.now())
proxy_array = ['window']
get_enviroment(proxy_array);

