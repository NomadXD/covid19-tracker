// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myLineChart");
//var datetime = JSON.parse('{{time|tojson}}')

time = window.appConfig.time
total = window.appConfig.total
//console.log(time)
labels_x=[]
daily=[]
totalCount = []

time.forEach(element => {
  x_axis = element['month']+" "+element["day"]
  y_axis = element["value"]
  labels_x.push(x_axis)
  daily.push(y_axis)
});
total.forEach(element => {
    y_axis = element['value']
    totalCount.push(y_axis)
});
let max_val = totalCount[totalCount.length-1]
console.log(max_val)
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: labels_x,
    datasets: [{
      data: daily,
      backgroundColor: 'transparent',
      label: "Cases daily",
      lineTension: 0.3,
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2
    },{
        
            label: "Total Cases",
            lineTension: 0.3,
            backgroundColor: "transparent",
            borderColor: "rgba(255,0,0,0.5)",
            pointRadius: 5,
            pointBackgroundColor: "rgba(255,0,0,1)",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data:totalCount,
          
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: max_val,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: true
    }
  }
});
