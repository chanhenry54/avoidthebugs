var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 450,
	physics: {
		default: 'arcade',
		arcade: {
			gravity: { y: 300 },
			debug: false
		}
	},
    scene: {
        preload: preload,
        create: create
		update: update
    },
	canvas: 'game-area'
};

var game;
var game_db = new Phaser.Data.DataManager(game);
var platforms;

function preload() {
    this.load.setBaseURL('https://avoidthebugs.herokuapp.com')
    this.load.image('sky', 'static/images/sky.png')
    this.load.image('ground', 'static/images/platform.png')
}

function create() {
    this.add.image(400, 300, 'sky')
	
	platforms = this.physics.add.staticGroup();
	
	platforms.create(400, 568, 'ground').setScale(2).refreshBody();
}

function update() {
    
}

// Must be an indicator from github.js that we can start the game.
$('#gameplay').on('show', function() {
    game = new Phaser.Game(config);
});