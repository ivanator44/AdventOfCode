const fs = require('fs')
const data = fs.readFileSync('./inputDay2.txt','utf8').split('\n')
const info = {'red' : 12, 'green' : 13, 'blue' :14}

let num = 0
data.forEach((line) =>{
    let id = parseInt(line.substring(5,line.indexOf(':')).trim())
    let array = line.substring(line.indexOf(':')+1).split(';')
    let pass = true
    for(let i = 0; i < array.length && pass;i++){
        let set = array[i].split(',').map((x) => x.trim())
        for(let j = 0; j <  set.length && pass;j++){
            balls = set[j]
            if(parseInt(balls.substring(0,2).trim()) > info[balls.substring(2).trim()]){
                pass = false
            }
        }
    }
    if(pass){num += id}
})

console.log(num)