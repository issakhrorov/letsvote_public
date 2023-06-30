import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'

const FirstChart = (
  {left_elem, right_elem, left, right}
) => {
  const options = {
    responsive: {
      rules: [{
        condition: {
          maxWidth: 500,
          maxHeight: 200
        },
        chartOptions: {
          legend: {
            enabled: false
          }
        }
      }]
    },
    title: {
      text: 'My chart'
    },
    legend: {
      itemStyle: {
          color: 'white',
          fontWeight: 'bold'
      }
    },
    plotOptions: {
      series: {
        dataLabels: {
          enabled: true
        }
      }
    },
    chart: {
      type: 'column',
      backgroundColor: "#293241",
      height: 300
    },
    colors: [
      "#448aff",
      "#ff1744",
    ],
    xAxis: {
      categories: [''],
      labels: {
        style: {
          color: 'white'
        }
      }
    },
    series: [{
      name: left_elem,
      data: [Number(left)]
      },
      {
      name: right_elem,
      data: [Number(right)]
      }
    ]
  }

  return (
    <div className='Chart'>
      <HighchartsReact 
        className="Chart"
        highcharts={Highcharts}
        options={options}
      />
    </div>
  )
}

export default FirstChart