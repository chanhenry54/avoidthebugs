console.log(Phaser.AUTO);
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
        preload = preload,
        create = create
    }
}

var game = new Phaser.Game(config);

var game_ev = new Phaser.Events.EventEmitter();
var game_db = new Phaser.Data.DataManager(game, game_ev);

function preload() {
    this.load.setBaseURL('https://avoidthebugs.herokuapp.com')
    
}

function create() {
    game_db.set('test', 0);
    console.log(game_db.get('test'));
}