var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 450,
    scene: {
        preload: preload,
        create: create
    }
}

var game = new Phaser.Game(config);
var game_db = new Phaser.Data.DataManager(game);

function preload() {
    this.load.setBaseURL('https://avoidthebugs.herokuapp.com')
    this.load.image('sky', 'static/images/sky.png')

}

function create() {
    this.add.image(400, 300, 'sky')
}