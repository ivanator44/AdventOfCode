const fs = require("fs")
const data = fs.readFileSync("inputDay2.txt", "utf8");
const lines = data.split('\n');

const id = /Game \d+/g;
const red = /[0-9]+ red/g;
const green = /[0-9]+ green/g;
const blue = /[0-9]+ blue/g;

let m;
last = 0

for (line in lines) {
    const result_red = [];
    const result_green = [];
    const result_blue = [];
    while ((m = red.exec(lines[line])) !== null) {
        result_red.push(parseInt(m[0]));
    }

    while ((m = green.exec(lines[line])) !== null) {
        result_green.push(parseInt(m[0]));
    }

    while ((m = blue.exec(lines[line])) !== null) {
        result_blue.push(parseInt(m[0]));
    }
    if (Math.max(...result_red) <= 12 && Math.max(...result_green) <= 13 && Math.max(...result_blue) <= 14) {
        while ((m = id.exec(lines[line])) !== null) {
            last += parseInt(m[0].slice(5));
        }
    }
    console.log(last)
}