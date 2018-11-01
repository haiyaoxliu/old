
var num = [23, 42, -7, -9, 0];

// display prompt box that ask for favorite color and 
// store result in a variable called favcolor
//var favcolor = window.prompt("What is your favorite color");


num.sort(
    function compare(a,b) {
        return b-a;
});

for (var i = 0; i < num.length; i++) {
     console.log(num[i])
}

for(var k = 0; k < 8; k++) {
    for(var m = 0; m <= k; m++) {
        console.log("#");
    }
    console.log("\n");
}