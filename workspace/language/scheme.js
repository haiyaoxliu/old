//Supports only basic operators (+, -, *, /)
//Checks for unmatched parentheses
//Note: no environments, no eval function
var operators = {
    '+': function(data) {
    var sum = 0;
    for(var i = 0; i < data.length; i++) {
      sum += num;
    }
    return sum;
  },
}
var tokenize = function(string) {
    var chars = string.split('');
    var tokens = [];
    var parens = 0;
    for(var i = 0; i < chars.length; i++) {
        if(chars[i] == ' ') 
        if(!isNaN(chars[i])) {
            console.log(chars[i]);
        }
    }
    if(parens !== 0) { console.log('Unmatched parentheses') }
};

var run = function() {
    
}

run('');
tokenize('abc123adf 24324   455');