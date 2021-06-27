$(document).ready(function(){
    console.log($("#hash_value").html());
    const hash = $("#hash_value").html();
    
    const hash_url = "https://floating-temple-20381.herokuapp.com/".concat(`https://api.edo.tzstats.com/explorer/contract/${hash}`)
    fetch(hash_url, {
        headers:{
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': "none",
            'X-Requested-With': 'XMLHttpRequest'
        },
    }).then(response => {
        return response.json() 
    }).then(data => {
        $("#n_ops").html(data["n_ops"]);
    });

    const hash_url_calls = "https://floating-temple-20381.herokuapp.com/".concat(`https://api.edo.tzstats.com/explorer/contract/${hash}/calls?prim=1`)
    fetch(hash_url_calls, {
        headers:{
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': "none",
            'X-Requested-With': 'XMLHttpRequest'
        },
    }).then(response => {
        return response.json() 
    }).then(data => {
        console.log(data);
        if (data[0]["is_contract"]==true){
            $("#is_contract").css("background-color","#0095f6");
        }else{
            $("#is_contract").css("background-color","#dbdbdb");
        }

        $("#confirmations").html(data[0]["confirmations"]);
        
        $("#gas_price").html(data[0]["gas_price"]);
        $("#storage_limit").html(data[0]["storage_limit"]);
        $("#cycle").html(data[0]["cycle"]);

        for (var i=0;i<data[0]["counter"];i++){
            $("#posts").append("<button class='post_btn'></button>");
        };

    });

});