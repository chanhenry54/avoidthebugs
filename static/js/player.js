var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 450,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 200 }
        }
    },
    scene: {
        preload: preload,
        create: create
    }
}

var game = new Phaser.Game(config);
var game_db = new Phaser.Data.DataManager(game);

function preload() {
    this.load.setBaseURL('https://avoidthebugs.herokuapp.com')
    
}

function create() {
    
}