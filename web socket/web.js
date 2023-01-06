fetch('https://hackattic.com/challenges/websocket_chit_chat/problem?access_token=')
    .then(response => response.json())
    .then(data => {
        let socket = new WebSocket("wss://hackattic.com/_/ws/"+data.token);
        var prev = Date.now();
        console.log(prev)

        socket.onopen = function(e) {

        };

        // 700, 1500, 2000, 2500 or 3000
        socket.onmessage = function(event) {
            console.log(event.data)
            if(event.data === "ping!"){
                let time = Date.now()
                let interval  = time - prev
                // console.log(time)
                // console.log(interval)
                prev = time
                socket.send(""+nearest(interval))

            }
        };

        socket.onclose = function(event) {
            console.log("CLOSE")
        };

        socket.onerror = function(error) {
            console.log("ERROR")
        };
    })


function nearest(i){
    let possibleIntervals = [1500, 2000, 2500, 3000]
    let min = Math.abs(700 - i);
    let rtn = 700
    for(let t of possibleIntervals){
        if(Math.abs(t-i) < min){
            rtn = t
            min = Math.abs(t-i)
        }
    }
    return rtn
}