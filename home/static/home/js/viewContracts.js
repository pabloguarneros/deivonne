//const url = window.location.origin.concat("/api")
const url = "https://floating-temple-20381.herokuapp.com/".concat("https://api.edo.tzstats.com/explorer/contract/KT19tRVRWLcvqnJWHiW8BQ26nPq9TnPYvvyu")
console.log("yey")
fetch(url, {
    headers:{
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': "none",
        'X-Requested-With': 'XMLHttpRequest' //Necessary to work with request.is_ajax()
    },
})
.then(response => {
    return response.json() //Convert response to JSON
})
.then(data => {
    console.log(data)
})