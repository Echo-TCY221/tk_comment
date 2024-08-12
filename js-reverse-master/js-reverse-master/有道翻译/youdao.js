crypto = require('crypto')
const fs = require('fs');
const { execSync } = require('child_process');

// 从 process.argv 中获取参数
const args = process.argv.slice(2);
const t = args[0];
function get_data(t) {
    const a = Buffer.alloc(16, new Uint8Array(crypto.createHash('md5').update("ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl").digest()));
    const r = Buffer.alloc(16, new Uint8Array(crypto.createHash('md5').update("ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4").digest()));
    i = crypto.createDecipheriv("aes-128-cbc", a, r)
    let s = i.update(t, "base64", "utf-8");
    s += i.final("utf-8")
    return s
}
const data = get_data(t);
console.log(data);
//测试
// const t = 'Z21kD9ZK1ke6ugku2ccWu4n6eLnvoDT0YgGi0y3g-v0B9sYqg8L9D6UERNozYOHqjhvjlnyGxxZI2NfFoZO1ldkbJn7OH2VibgiCW15u0t7mddYVWS_U_9KS3BNwfhiFBTZaZB8xqsAr9x0Pl7zOCURAyrlZwymVUg-EnlZui9n09SgKr9e136hO59ZGn37AnCpkZ8yX7EaANo5njhftBsNnrOs9jjqRX6JMM1jUIdahzXiMVC8UCG7Xl9oxaqwSj9SoDyQ2XxjiZVbekY5mL-kIoWv0goRXr1l0JdaXJpYppFWWWmPHArLaEYnxovxAu4rwhUor1OHiN1pBMjh7YdZkzZ-ck48t0oWQ8cpEb-DgtfELq9LVqUN4qkO_jK3K83Vami3Hins4w26DKWOz2jslcpRWXt3SRE4YjtOz4OcOT8ecGwQPOCD-g-tKuOfh'
// console.log(get_data(t))

