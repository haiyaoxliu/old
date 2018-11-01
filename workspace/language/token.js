//new token form:
//  { type: var, val, list, func?,
//    value: some value }
//
//env:
//  { some var: some value,
//    ... }
//
//parse:

var top = Object.create(null);
top['set'] = function() {
    
};
top['chars'] = {
    '/':'',
    '(':'',
    ')':'',
    '.':'',
    ';':'',
    ',':'',
}

var tokenize = function(text) {
  var program = text.split(' ').join('');
  var tokens = [];
  for(var i = 0; i < program.length; i++) {
      if(program[i] == '(') {
          //basic operators
          console.log(program[i]);
          console.log(program[i]);
      }
  }
  console.log(program);
  return program;
};

tokenize("(blahblah((())");