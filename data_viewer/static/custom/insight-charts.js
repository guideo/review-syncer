Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

var myPieChart1;
function drawPieChart1(chart_id, chart_labels, chart_data){
    var ctx = document.getElementById(chart_id);
    myPieChart1 = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: chart_labels,
        datasets: [{
          data: chart_data,
          backgroundColor: ['#3cb44b','#ffe119','#e6194b','#0082c8','#f58231','#911eb4','#46f0f0','#f032e6','#d2f53c','#fabebe','#008080','#e6beff','#aa6e28','#fffac8'],
        }],
      },
      options: {
        legend: {
          display: false
        }
      }
    });
}
var myPieChart2;
function drawPieChart2(chart_id, chart_labels, chart_data){
    var ctx = document.getElementById(chart_id);
    myPieChart2 = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: chart_labels,
        datasets: [{
          data: chart_data,
          backgroundColor: ['#e6194b','#ffe119','#3cb44b','#0082c8','#f58231','#911eb4','#46f0f0','#f032e6','#d2f53c','#fabebe','#008080','#e6beff','#aa6e28','#fffac8'],
        }],
      },
      options: {
        legend: {
          display: false
        }
      }
    });
    console.log('bla1');
}
function updatePieChart1(new_data){
    myPieChart1.data.datasets[0].data = new_data;
    myPieChart1.update();
}
function updatePieChart2(new_label, new_data){
    myPieChart2.data.labels = new_label;
    myPieChart2.data.datasets[0].data = new_data;
    myPieChart2.update();
}

var areaChart;
function drawAreaChart(labels, data){
    var ctx = document.getElementById("areaChart");
    var myLineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: "Reviews",
          lineTension: 0.3,
          backgroundColor: "rgba(2,117,216,0.2)",
          borderColor: "rgba(2,117,216,1)",
          pointRadius: 5,
          pointBackgroundColor: "rgba(2,117,216,1)",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 20,
          pointBorderWidth: 2,
          data: data,
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
              max: 300,
              maxTicksLimit: 5
            },
            gridLines: {
              color: "rgba(0, 0, 0, .125)",
            }
          }],
        },
        legend: {
          display: false
        }
      }
    });
}
function updateAreaChart(new_data){
    areaChart.data.datasets[0].data = new_data;
    areaChart.update();
}