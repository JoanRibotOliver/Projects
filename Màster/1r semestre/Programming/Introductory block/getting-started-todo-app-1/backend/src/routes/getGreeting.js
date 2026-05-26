const GREETINGS = [
    "Whalecome",
    "Uep, com anam?",
];

module.exports = async (req, res) => {
    res.send({
        greeting: GREETINGS[ Math.floor( Math.random() * GREETINGS.length )],
    });
};
