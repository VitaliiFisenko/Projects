var mysql = require('mysql');
const readline = require('readline');

const r1 = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})


var con = mysql.createConnection({
	host:'maindb.cx26wwzmixrv.us-east-1.rds.amazonaws.com',
	user:'admin',
	password:'R3idpm8z6e',
	database:'db',
});
r1.on('line',(input) =>{

con.connect(function(err){
	if(err) throw err;
	
	con.query(input, function(err,result,fields){
		if(err) throw err;
		console.log(result);
	});
});
});