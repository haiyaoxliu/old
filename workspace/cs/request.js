//var rconsole = document.getElementById('actions');
var http = require("http");
var request = http.request({
    hostname: "demo-project-haiyao.c9.io",
    path: "/testfolder",
    method: 'MKCOL',
    headers: {
        Accept: 'text/html'
    }
}, function(response) {
    readStreamAsString(response, function(error, content) {
        if (error) throw error;
        document.write(content);
    });
});
request.end();

function readStreamAsString(stream, callback) {
  var content = "";
  stream.on("data", function(chunk) {
    content += chunk;
  });
  stream.on("end", function() {
    callback(null, content);
  });
  stream.on("error", function(error) {
    callback(error);
  });
}

