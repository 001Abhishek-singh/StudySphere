const updateTime = () => {
    var dateInfo = new Date();
    // to display the time
    var hour, minute = (dateInfo.getMinutes()<10) ? "0" + dateInfo.getMinutes() : dateInfo.getMinutes();
    var sec = (dateInfo.getSeconds()<10) ? "0" + dateInfo.getSeconds() : dateInfo.getSeconds();
    var ampm = (dateInfo.getHours()>=12)? "PM" : "AM";

    // replace 0 with 12 at midnight, clock cycle will be 0-12
    if(dateInfo.getHours() == 0){
        hour = 12;
    }
    else if(dateInfo.getHours() > 12){
        hour = dateInfo.getHours() - 12;
    }
    else{
        hour = dateInfo.getHours();
    }
    // display current time
    var currentTime = hour + ":" + minute + ":" + sec;
    // display time
    document.getElementsByClassName("hms")[0].innerHTML = currentTime;
    document.getElementsByClassName("ampm")[0].innerHTML = ampm;

    // date
    var weeks = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thrusday',
        'Friday',
        'Saturday'
    ];
    var months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ];
    day = dateInfo.getDate();
    // store the data
    var currentDate = weeks[dateInfo.getDay()] + ',' + " " + day + " " +  months[dateInfo.getMonth()];
    document.getElementsByClassName('date')[0].innerHTML = currentDate;
};
updateTime();
// print time and date once, then update them every second
setInterval(function(){
    updateTime()
},1000);
