var hash = '';
for(var k = 0; k < 8; k++) {
    hash += '#';
    console.log(hash);
}

var size = 8;
var a = ' ';
var b = '#';
for(var i = 0; i < size; i++) {
    var line = '';
    for(var j = 0; j < size; j++) {
        if((i + j) % 2 == 0) {
            line += a;
        }
        else {
            line += b;
        }
    }
    console.log(line)
}