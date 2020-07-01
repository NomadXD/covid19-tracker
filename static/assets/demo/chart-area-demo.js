// // Set new default font family and font color to mimic Bootstrap's default styling
// Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
// Chart.defaults.global.defaultFontColor = '#292b2c';

// // Area Chart Example
// var ctx = document.getElementById("myAreaChart");
// //var datetime = JSON.parse('{{time|tojson}}')

// time = window.appConfig.time
// //console.log(time)
// labels_x=[]
// values=[]
// time.forEach(element => {
//   x_axis = element['month']+" "+element["day"]
//   y_axis = element["value"]
//   labels_x.push(x_axis)
//   values.push(y_axis)
// });
// console.log(values)
// var myLineChart = new Chart(ctx, {
//   type: 'line',
//   data: {
//     labels: labels_x,
//     datasets: [{
//       label: "Cases confirmed",
//       lineTension: 0.3,
//       borderColor: "rgba(2,117,216,1)",
//       pointRadius: 5,
//       pointBackgroundColor: "rgba(2,117,216,1)",
//       pointBorderColor: "rgba(255,255,255,0.8)",
//       pointHoverRadius: 5,
//       pointHoverBackgroundColor: "rgba(2,117,216,1)",
//       pointHitRadius: 50,
//       pointBorderWidth: 2,
//       data: values,
//     },{
//       label: "Sessions",
//       lineTension: 0.3,
//       backgroundColor: "transparent",
//       borderColor: "rgba(255,117,216,1)",
//       pointRadius: 5,
//       pointBackgroundColor: "rgba(2,117,216,1)",
//       pointBorderColor: "rgba(255,255,255,0.8)",
//       pointHoverRadius: 5,
//       pointHoverBackgroundColor: "rgba(2,117,216,1)",
//       pointHitRadius: 50,
//       pointBorderWidth: 2,
//       data: [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451],
//     }],
//   },
//   options: {
//     scales: {
//       xAxes: [{
//         time: {
//           unit: 'date'
//         },
//         gridLines: {
//           display: false
//         },
//         ticks: {
//           maxTicksLimit: 7
//         }
//       }],
//       yAxes: [{
//         ticks: {
//           min: 0,
//           max: 20,
//           maxTicksLimit: 5
//         },
//         gridLines: {
//           color: "rgba(0, 0, 0, .125)",
//         }
//       }],
//     },
//     legend: {
//       display: false
//     }
//   }
// });
