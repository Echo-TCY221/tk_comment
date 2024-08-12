function randomGarbledCharactersArrayList() {
     function randomGarbledCharactersArray1() {
        let arr = []
        random = Math.random() * 10000
        num1 = random & 255
        num2 = random >> 8 & 255
        arr.push((num1 & 170) | (3 & 85))
        arr.push((num1 & 85) | (3 & 170))
        arr.push((num2 & 170) | (45 & 85))
        arr.push((num2 & 85) | (45 & 170))
        return String.fromCharCode.apply(null,arr);
    }
    function randomGarbledCharactersArray2() {
        let arr = []
        random = Math.random() * 10000
        num1 = random & 255
        num2 = random >> 8 & 255
        arr.push((num1 & 170) | (1 & 85))
        arr.push((num1 & 85) | (1 & 170))
        arr.push((num2 & 170) | (0 & 85))
        arr.push((num2 & 85) | (0 & 170))
        return String.fromCharCode.apply(null,arr);
    }

    function randomGarbledCharactersArray3() {
        let arr = []
        random = Math.random() * 10000
        num1 = random & 255
        num2 = random >> 8 & 255
        arr.push((num1 & 170) | (1 & 85))
        arr.push((num1 & 85) | (1 & 170))
        arr.push((num2 & 170) | (1 & 85))
        arr.push((num2 & 85) | (1 & 170))
        return String.fromCharCode.apply(null,arr);
    }
    return randomGarbledCharactersArray1()+randomGarbledCharactersArray2()+randomGarbledCharactersArray3()
}

