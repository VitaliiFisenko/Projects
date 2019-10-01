let in_game = 0,right_car, left_car,canvas, ctx, animat, score =0 ;
let lo1, lo2, lo3, lo4;
let ro1, ro2, ro3, ro4;
let obstacles1 = [lo1,lo2,lo3,lo4];
let obstacles2 = [ro1,ro2,ro3,ro4];
window.onload = function(){
	canvas = document.getElementById('canvas');
	ctx = canvas.getContext('2d');

	left_car = new Left_car();
	right_car = new Right_car();

	lo1 =  new Left_obstacles();
	lo2 = new Left_obstacles();
	lo3 = new Left_obstacles();
	lo4 = new Left_obstacles();

	ro1 = new Right_obstacles();
	ro2 = new Right_obstacles();
	ro3 = new Right_obstacles();
	ro4 = new Right_obstacles();

	init();

	obstacles1 = [lo1, lo2];
	obstacles2 = [ro1, ro2]
	draw();
};
let init = ()=>{
	lo1.y = -lo1.height;
	lo2.y = lo1.y - 200 - lo2.height;

	ro1.y = (-ro1.height);
	ro2.y = ro1.y - 200 - ro2.height;
}
class Left_car{
	constructor(){
		this.position = 0;
		this.width = 50;
		this.height = 80;
		this.y = 430;
		this.x = 25;
	}

	move(){

	}
	draw(){
		if(this.position == 0){
			ctx.fillStyle = "#FF0000";
			ctx.fillRect(this.x,this.y,this.width, this.height);
		}else if(this.position == 1){
			ctx.fillStyle = "#FF0000";
			ctx.fillRect(this.x+100,this.y,this.width, this.height);

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
			ctx.fillRect(this.x,this.y,this.width, this.height);
		}else if(this.position == 1){
			ctx.fillStyle = "#00A6FF";
			ctx.fillRect(this.x-100,this.y,this.width, this.height);
		}
	}
}

class Left_obstacles{
	constructor(){
		this.height = 40;
		this.width  = 40;
		this.x = 30;
		this.y = 50;
		this.side = Math.round(Math.random());
		this.color = "#FF0000";
		this.type = Math.round(Math.random());
	}
	draw(){
		if(this.side == 0){
			this.x = 30;
		}else if(this.side == 1){
			this.x = 130;
		}
		if(this.type == 0){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x, this.y, this.width, this.height);
			ctx.fillStyle = "#FFFFFF";
			ctx.fillRect(this.x+2, this.y+2, this.width-5, this.height-5);
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x+10, this.y+10, this.width-20, this.height-20);
		}else if(this.type == 1){
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

	collusion_check(){
		if(this.type == 0){
			if(this.y>canvas.height){
				this.y = -this.width;
				check();
				this.type = Math.round(Math.random());
				this.side = Math.round(Math.random());
			}else if(this.y+this.height>left_car.y && this.y<left_car.y+left_car.height && this.side === left_car.position){
				clearInterval(animat);
				in_game = 0;
				score = 0;
			}
		}else if(this.type == 1){
			if(this.y>canvas.height){
				clearInterval(animat);
				in_game = 0;
				score = 0;
			}else if(this.y+this.height/2>left_car.y && this.side == left_car.position && this.y<left_car.y+left_car.height){
				this.y = -this.width;
				check();
				this.type = Math.round(Math.random());
				this.side = Math.round(Math.random());
				score++;
			}
		}
	}
}

class Right_obstacles extends Left_obstacles{
	constructor(){
		super();
		this.color = "#00A6FF";
		this.x = 330;
		this.side = Math.round(Math.random());
	}

	draw(){
		if(this.side == 0){
			this.x = 330;
		}else if(this.side == 1){
			this.x = 230;
		}
		if(this.type == 0 ){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x, this.y, this.width, this.height);
			ctx.fillStyle = "#FFFFFF";
			ctx.fillRect(this.x+2, this.y+2, this.width-5, this.height-5);
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x+10, this.y+10, this.width-20, this.height-20);
		}else if(this.type == 1){
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
	collusion_check(){
		if(this.type == 0){
			if(this.y>canvas.height){
				this.y = -this.width;
				check();
				this.type = Math.round(Math.random());
				this.side = Math.round(Math.random());
			}else if(this.y+this.height>right_car.y && this.y<right_car.y+left_car.height && this.side === right_car.position){
				clearInterval(animat);
				in_game =0;
				score = 0;

			}
		}else if(this.type == 1){
			if(this.y>canvas.height){
				clearInterval(animat);
				in_game = 0;
				score = 0;
			}else if(this.y+this.height/2>right_car.y && this.side == right_car.position && this.y<left_car.y+right_car.height){
				this.y = -this.width;
				check();
				this.type = Math.round(Math.random());
				this.side = Math.round(Math.random());
				score++;
			}
		}
	}
}
function check() {

		if(obstacles1[0].y<0 &&
			obstacles1[0].side != obstacles1[1].side &&
			obstacles1[0].type == obstacles1[1].type ){
			obstacles1[0].y -=200;
		}else if(obstacles1[1].y<0 &&
			obstacles1[0].side != obstacles1[1].side &&
			obstacles1[0].type == obstacles1[1].type ){
			obstacles1[1].y -=200;
		}else if(obstacles2[0].y<0 &&
			obstacles2[0].side != obstacles2[1].side &&
			obstacles2[0].type == obstacles2[1].type){
			obstacles2[0].y -=200;
		}else if(obstacles2[1].y<0 &&
			obstacles2[0].side != obstacles2[1].side &&
			obstacles2[0].type == obstacles2[1].type ){
			obstacles2[1].y -=200;
		}

}
function draw_field(){
	ctx.fillStyle = "#6E84D6";
	ctx.fillRect(98,0,2,600);
	ctx.fillRect(298,0,2,600);
	ctx.fillRect(196,0,4,600);
}

function draw(){
ctx.clearRect(0,0,canvas.width, canvas.height);
draw_field();

left_car.draw();
right_car.draw();

for(let x =0; x<2; x++){
	obstacles1[x].draw();
	obstacles2[x].draw();
}
document.getElementById('score').innerText = +score;
}

function anim() {
	if(in_game == 0){
	animat = setInterval(()=>{
for(let i = 0; i<2 ;i++) {
obstacles1[i].y++;
obstacles1[i].collusion_check();
obstacles2[i].y++;
obstacles2[i].collusion_check();
}
draw();
},3);}
}

addEventListener("keydown",(key)=>{
	switch (key.keyCode) {
		case 37:
			if(left_car.position == 0){
				left_car.position++;
			}else{
				left_car.position--;
			}
			break;
		case 39:
			if(right_car.position == 0){
				right_car.position++;
			}else{
				right_car.position--;
			}
			break;
		case 13:
			if(in_game==0){
			init();
			anim();
			in_game++;
			break;}
	}
})