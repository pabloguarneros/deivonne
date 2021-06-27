//const url = window.location.origin.concat("/api")
// GET FORMATTED DATE FROM  https://muffinman.io/blog/javascript-time-ago-function/
const MONTH_NAMES = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ];
  
  
  function getFormattedDate(date1, prefomattedDate = false, hideYear = true) {
    const date = new Date(date1)
    const day = date.getDate();
    const month = MONTH_NAMES[date.getMonth()];
    const year = date.getFullYear();
    const hours = date.getHours();
    let minutes = date.getMinutes();
  
    if (minutes < 10) {
      // Adding leading zero to minutes
      minutes = `0${ minutes }`;
    }
  
    if (prefomattedDate) {
      // Today at 10:20
      // Yesterday at 10:20
      return `${ prefomattedDate } at ${ hours }:${ minutes }`;
    }
  
    if (hideYear) {
      // 10. January at 10:20
      return `${ month } ${ day } at ${ hours }:${ minutes }`;
    }
  
    // 10. January 2017. at 10:20
    return `${ month } ${ day }. ${ year }. at ${ hours }:${ minutes }`;
  }



  function timeAgo(dateParam) {
  
    console.log(dateParam);
    const date = new Date(dateParam);
    const DAY_IN_MS = 86400000; // 24 * 60 * 60 * 1000
    const today = new Date();
    const yesterday = new Date(today - DAY_IN_MS);
    const seconds = Math.round((today - date) / 1000);
    const minutes = Math.round(seconds / 60);
    const isToday = today.toDateString() === date.toDateString();
    const isYesterday = yesterday.toDateString() === date.toDateString();
    const isThisYear = today.getFullYear() === date.getFullYear();
  
    if (seconds < 5) {
      return 'now';
    } else if (seconds < 60) {
      return `${ seconds } seconds ago`;
    } else if (seconds < 90) {
      return 'about a minute ago';
    } else if (minutes < 60) {
      return `${ minutes } minutes ago`;
    } else if (isToday) {
      return getFormattedDate(date, 'Today'); // Today at 10:20
    } else if (isYesterday) {
      return getFormattedDate(date, 'Yesterday'); // Yesterday at 10:20
    } else if (isThisYear) {
      return getFormattedDate(date, false, true); // 10. January at 10:20
    }
  
    return getFormattedDate(date); // 10. January 2017. at 10:20
  }

$(document).ready(function(){

    const url = window.location.origin.concat("/api")
    fetch(url, {
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest' //Necessary to work with request.is_ajax()
        },
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        data.forEach(value=>{
            const html_pk = value["pk"];
            //const hash_url = "https://floating-temple-20381.herokuapp.com/".concat(`https://api.edo.tzstats.com/explorer/contract/KT19tRVRWLcvqnJWHiW8BQ26nPq9TnPYvvyu`)
            const hash_url = "https://floating-temple-20381.herokuapp.com/".concat(`https://api.edo.tzstats.com/explorer/contract/${value["hash"]}`)
            fetch(hash_url, {
                headers:{
                    'Accept': 'application/json',
                    'Access-Control-Allow-Origin': "none",
                    'X-Requested-With': 'XMLHttpRequest'
                },
            }).then(response => {
                return response.json() 
            }).then(data => {
                //$(`#contract_${html_pk} .api_updated`).html(timeAgo(Date(data["last_time_seen"])));
                var d = getFormattedDate(Date(data["last_time_seen"]));
                $(`#contract_${html_pk} .api_updated`).html(d);
                d = getFormattedDate(Date(data["first_time_seen"]));
                $(`#contract_${html_pk} .api_created`).html(d);
                $(`#contract_${html_pk} .api_storage_size`).html(data["storage_size"]);
                $(`#contract_${html_pk} .api_storage_paid`).html(data["storage_paid"]);
        }
    )})})
})