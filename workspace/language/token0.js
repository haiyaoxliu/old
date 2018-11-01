var parse = function(string) {
  var tokens = [];
  for(var i = 0; i < string.length; i++) {
    if(string[i] == ' ') {
      continue
    }
    else if(string[i] == '(') {
      tokens.push( ['list start:', '('] );
    }
    else if(string[i] == ')') {
      tokens.push( ['list end:', ')'] );
    }
    else if(!isNaN(string[i])) {
      var num = '';
      while(!isNaN(string[i]) && string[i] != ' ' && string[i] != '(' && string[i] != ')') {
        num = num + string[i];
        i++;
      }
      i--;
      tokens.push( ['number:', num] )
    }
    else {
      var word = '';
      while(typeof string[i] == 'string' && string[i] != ' ' && string[i] != '(' && string[i] != ')') {
        word = word + string[i];
        i++;
      }
      i--;
      tokens.push(['symbol:', word])
    }
  }
  console.log(tokens);
};
parse("(somestring 1 (33 abc 33) def 3))))))");
