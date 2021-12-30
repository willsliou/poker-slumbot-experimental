console.stdlog = console.log.bind(console);
console.logs = [];
console.log = function(){
    console.logs.push(Array.from(arguments));
    console.stdlog.apply(console, arguments);
}

// Print hole cards
my_hole_cards_ = console.logs[0][0].hole_cards
console.logs[0][0].hole_cards


myMap_cards = {'Kd': 1, 'K'}

if (my_[0] == 'Kd') { document.getElementById("call").click() }


document.getElementById("fold").click()

