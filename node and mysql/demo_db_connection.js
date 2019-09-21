var mysql = require('mysql');
var con = mysql.createConnection({
	host:"maindb.cx26wwzmixrv.us-east-1.rds.amazonaws.com",
	user:"admin",
	password:"R3idpm8z6e",
	database:"nodedb",
});

con.connect(function(err){
	if(err) throw err;
	console.log("connected!");
	var sql = "INSERT INTO customers (name, adress) VALUES ('someValue1', 'someValue2')";
	var values = [['John', 'Highway 71'],
	    ['Peter', 'Lowstreet 4'],
	    ['Amy', 'Apple st 652'],
	    ['Hannah', 'Mountain 21'],
	    ['Michael', 'Valley 345'],
	    ['Sandy', 'Ocean blvd 2'],
	    ['Betty', 'Green Grass 1'],
	    ['Richard', 'Sky st 331'],
	    ['Susan', 'One way 98'],
	    ['Vicky', 'Yellow Garden 2'],
	    ['Ben', 'Park Lane 38'],
	    ['William', 'Central st 954'],
	    ['Chuck', 'Main Road 989'],
	    ['Viola', 'Sideway 1633']];

	con.query(sql, function(err,result){
		if (err) throw err;
		console.log("1 record inserted "+result.insertId);
	})
});