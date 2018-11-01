var token = function(string) {
  var tokens = [];
  for(var i = 0; i < string.length; i++) {
    if(string[i] == ' ') {
      continue
    } else if(string[i] == '(') {
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
      tokens.push( ['number:', num] );
    }
    else if (string[i] == "'") {
      i++;
      var str = ''
      while(string[i] != "'") {
        if(!string[i]) {
          console.log('Error: No end quote found.');
          return;
        }
        str = str + string[i]
        i++;
      }
      tokens.push( ['string:', str] );
    }
    else {
      var word = '';
      while(typeof string[i] == 'string' && string[i] != ' ' && string[i] != '(' && string[i] != ')') {
        word = word + string[i];
        i++;
      }
      i--;
      tokens.push(['symbol:', word]);
    }
  }
  return tokens;
};


var parse = function(string) {
  var tokens = token(string);
  var parens = 0;
  var stack = [[]];
  for(var i = 0; i < tokens.length; i++) {
    if(parens < 0) {
      //console.log('Error: Unmatched parentheses');
      return false;
    }
    
    //console.log("current stack:" + stack);
    if(tokens[i][1] == '(') {
      stack.push([]);
    } else if(tokens[i][1] == ')') {
      var tmp = stack.pop();
      //console.log("tmp is: " + tmp)
      stack[stack.length - 1].push(tmp);
    } else {
      stack[stack.length - 1].push(tokens[i]);
    }
    if(tokens[i][0] == 'list start:') {
      parens++;
    } else if(tokens[i][0] == 'list end:') {
      parens--;
    }
  }
  if(parens != 0) {
    console.log('Error: Unmatched parentheses');
    return false;
  }
  //console.log(tokens);
  if(stack[0].length > 1) {
    console.log('invalid exp');
    return false;
  }
  console.log(stack[0])
  return stack[0];
};

var evaluate = function(thing, env) {
  //console.log(thing);
  if(thing[0][0] == 'string:') {
    //console.log('string: ' + thing[0][1]); 
    return [thing[0][1], 'atom'];
  } else if(thing[0][0] == 'number:') {
    //console.log('number: ' + thing[0][1]);
    return [thing[0][1], 'atom'];
  } else if(thing[0][0] == 'symbol:') {
    if(!env[thing[0][1]]) {
      //console.log('symbol: ' + thing[0][1] + '\n not defined');
      return ['undefined', 'atom'];
    } else {
      //console.log('symbol: ' + thing[0][1] + '\n value: ' + env[thing[0][1]]);
      return [env[thing[0][1]], 'atom'];
    }
  }
  else {
    if(thing[0].length < 1) {
      //console.log('Empty list');
      return [[], 'list'];
    } else if(thing[0][0][1] in top) {
      var result = top[thing[0][0][1]](thing[0].slice(1), env);
      return [result, 'list'];
    } else {
      console.log('invalid program');
    }
  }
};

var top = {
  aaa: 'test var aaa reached',
  'set': function(data, env) {
    env[data[0][1]] = evaluate([data[1]], env)[0];
    //console.log('Set ' + data[0][1] + ' to ' + data[1][1]);
    return 'set ' + data[0][1] + ' to ' + top[data[0][1]];
  },
  '+': function(data, env) {
    var sum = 0;
    for(var i = 0; i < data.length; i++) {
      //console.log(data[i])
      var num = Number(evaluate([data[i]], env)[0]);
      sum += num;
    }
    //console.log('Sum: ' + sum);
    return sum;
  },
  'do': function(data, env) {
    for(var i = 0; i < data.length; i++) {
      var result = evaluate([data[i]], env)[0];
      if(i == data.length - 1) {
        //console.log('Result: ' + result);
        return result;
      }
    }
  },
  'if': function(data,env) {
    var conditional = evaluate([data[0]], env)[0];
    //console.log(conditional)
    if(conditional) {
      return 'conditional is true: ' + evaluate([data[1]], env)[0];
    } else {
      return 'conditional is false: ' + evaluate([data[2]], env)[0];
    }
  },
  '==': function(data, env) {
    //console.log(data);
    if(evaluate([data[0]], env)[0] == evaluate([data[1]], env)[0]) {
      return true;
    }
    return false;
  },
  'print': function(data, env) {
    console.log(evaluate(data, env)[0]);
  },
  '>': function(data, env) {
    if(evaluate([data[0]], env)[0] > evaluate([data[1]], env)[0]) {
      return true;
    }
    return false;
  },
  'atom': function(data, env) {
    if(evaluate(data, env)[1] == 'atom') {
      return true;
    }
    return false;
  }
};

evaluate(parse("(print 'somestring 1')"), top);
evaluate(parse("(print (+ 6 (+ 2 3) 9 10) )"), top);
evaluate(parse("(+ (+ 7 8) 5)"), top);
evaluate(parse("(print (set a 7))"), top);
evaluate(parse("a"), top);
evaluate(parse("(do (set a 8) (set b 7) (+ a b))"), top);
evaluate(parse("()"), top);
evaluate(parse("(do (set x 123) (+ 5 x))"), top);
evaluate(parse("(do (set x 234) (set y 678))"), top);
evaluate(parse("(print (do (set x 234) (set y 678) (+ 11 x y 10)))"), top);
evaluate(parse("(print(if (== 1 7) (+ x 66) (+ x '-34')))"), top);
evaluate(parse("(print(if (== 1 1) (+ 10 20) (+ 20 30)))"), top);
evaluate(parse("(print(if (> 1 7) (+ 10 20) (+ 20 30)))"), top);
evaluate(parse("(print(if (> 7 1) (+ 10 20) (+ 20 30)))"), top);
evaluate(parse("(print(if (atom 5) (+ 10 20) (+ 20 30)))"), top);
//evaluate(parse("(print(atom (+ 10 20)))"), top);
//evaluate(parse("(print (atom ()))"), top);
//evaluate(parse("(print (== 5 5))"), top);
//evaluate(parse("(print (== 5 '5'))"), top);
//evaluate(parse("(print (== () ()))"), top);
//evaluate(parse("(print (== (5) (5)))"), top);