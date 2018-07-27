Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

var myBarChart;
function drawSelectedChart(){
    var ctx = document.getElementById("myBarChart");
    myBarChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: star_ratings,
        datasets: [{
          label: "Reviews",
          backgroundColor: "rgba(2,117,216,1)",
          borderColor: "rgba(2,117,216,1)",
          data: star_ratings_count,
        }],
      },
      options: {
        scales: {
          xAxes: [{
            time: {
              unit: 'rating'
            },
            gridLines: {
              display: false
            },
            ticks: {
              maxTicksLimit: 6
            }
          }],
          yAxes: [{
            ticks: {
              min: 0,
              maxTicksLimit: 5
            },
            gridLines: {
              display: true
            }
          }],
        },
        legend: {
          display: false
        }
      }
    });
}
function updateBarChart(new_data){
    myBarChart.data.datasets[0].data = new_data;
    myBarChart.update();
}