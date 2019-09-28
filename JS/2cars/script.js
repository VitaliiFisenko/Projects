let right_car, left_car,canvas, ctx;
window.onload = function(){
	canvas = document.getElementById('canvas');
	ctx = canvas.getContext('2d');
	left_car = new Left_car();
	right_car = new Right_car();
	left_car.draw();
	right_car.draw();
	draw_field();
}
class Left_car{
	constructor(){
		this.position = 0;
		this.width = 50;
		this.heigth = 100
		this.y = 460;
		this.x = 25;
	}

	move(){

	}
	draw(){
		if(this.position == 0){
			ctx.fillStyle = "#FF0000";
			ctx.fillRect(this.x,this.y,this.width, this.heigth);
		}else if(this.position == 1){

		}
	}
}


class Right_car extends Left_car{
	constructor(){
	super();
	this.x = 325;
	}
	draw(){
		if(this.position == 0){
			ctx.fillStyle = "#00A6FF";
			ctx.fillRect(this.x,this.y,this.width, this.heigth);
		}else if(this.position == 1){

		}
	}
}

class Left_obstacles{
	constructor(){
		this.heigth = 40;
		this.width  = 40;
		this.x = 30;
		this.y = 50;
		this.color = "#FF0000";
		this.type = Math.round(Math.random());
	}
	draw(){
		if(this.type == 1 ){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x, this.y, this.width, this.heigth);
			ctx.fillStyle = "#FFFFFF";
			ctx.fillRect(this.x+2, this.y+2, this.width-5, this.heigth-5);
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x+10, this.y+10, this.width-20, this.heigth-20);
		}else if(this.type == 0){
			ctx.fillStyle = this.color;
			ctx.beginPath();
			ctx.arc(this.x+20, this.y, 20, 0, 2 * Math.PI);
			ctx.fill();
			ctx.fillStyle = "#FFFFFF";
			ctx.beginPath();
			ctx.arc(this.x+20, this.y, 17	, 0, 2 * Math.PI);
			ctx.fill();
			ctx.fillStyle = this.color;
			ctx.beginPath();
			ctx.arc(this.x+20, this.y, 10, 0, 2 * Math.PI);
			ctx.fill();
		}
	}
}

class Right_obstacles extends Left_obstacles{
	constructor(){
		super();
		this.color = "#00A6FF";
		this.x = 330;
	}
}

function draw_field(){
	ctx.fillStyle = "#6E84D6";
	ctx.fillRect(98,0,2,600);
	ctx.fillRect(298,0,2,600);
	ctx.fillRect(196,0,4,600);
}

function draw(){

}