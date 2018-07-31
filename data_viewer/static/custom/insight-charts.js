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

var lineChart;
function drawLineChart(labels, data){
    var ctx = document.getElementById("lineChart");
    lineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: "Good Reviews",
          lineTension: 0.1,
          backgroundColor: "rgba(40,167,69,0.2)",
          borderColor: "rgba(40,167,69,1)",
          pointRadius: 3,
          pointBackgroundColor: "rgba(40,167,69,1)",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(40,167,69,1)",
          pointHitRadius: 10,
          pointBorderWidth: 2,
          data: data,
        },{
          label: "Regular Reviews",
          lineTension: 0.1,
          backgroundColor: "rgba(255,193,7,0.2)",
          borderColor: "rgba(255,193,7,1)",
          pointRadius: 3,
          pointBackgroundColor: "rgba(255,193,7,1)",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(255,193,7,1)",
          pointHitRadius: 10,
          pointBorderWidth: 2,
          data: data,
        },{
          label: "Bad Reviews",
          lineTension: 0.1,
          backgroundColor: "rgba(220,53,69,0.2)",
          borderColor: "rgba(220,53,69,1)",
          pointRadius: 3,
          pointBackgroundColor: "rgba(220,53,69,1)",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(220,53,69,1)",
          pointHitRadius: 10,
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
              max: 100,
              maxTicksLimit: 5
            },
            gridLines: {
              color: "rgba(0, 0, 0, .125)",
            }
          }],
        },
        legend: {
          display: false
        },
        tooltips: {
            enabled: true,
            mode: 'single',
            callbacks: {
                label: function(tooltipItems, data) {
                    return data.datasets[tooltipItems.datasetIndex].label + ': ' + tooltipItems.yLabel + '%';
                },
                afterLabel: function(tooltipItems, data) {
                    return 'Represents ' + ((tooltipItems.yLabel*parseInt(tooltipItems.xLabel[1].replace('Total: ',''))/100).toFixed(0) + ' reviews');
                }
            }
        }
      }
    });
}
function updateLineChart(new_labels, new_data0, new_data1, new_data2){
    lineChart.data.labels = new_labels;
    lineChart.data.datasets[0].data = new_data0;
    lineChart.data.datasets[1].data = new_data1;
    lineChart.data.datasets[2].data = new_data2;
    lineChart.update();
}