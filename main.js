const spawn = require('child_process').spawn; 
const result = spawn('python', ['crolling.py']); 
result.stdout.on('data', function(data) {
    console.log(data.toString()); 
});
result.stderr.on('data', function(data) {
    console.log(data.toString());
});
