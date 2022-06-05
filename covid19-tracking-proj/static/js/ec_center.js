var ec_center = echarts.init(document.getElementById('c2'), "dark");

// Specify configurations and data graphs 
ec_center.showLoading();

option = {
    tooltip : {
        trigger: 'item',
    },

    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 1,end: 999 },
            {start: 1000, end: 9999 }, 
            { start: 10000, end: 99999 },
            { start: 100000, end: 999999 },
            { start: 1000000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },

    series : [
        {
            name: 'Confirmed',
            type: 'map',
            map: 'USA',
            roam: false, //拖动和缩放
            itemStyle: {
                normal: {
                    borderWidth: .5, //区域边框宽度
                    borderColor: '#009fe8', //区域边框颜色
                    areaColor: "#ffefd5", //区域颜色
                },
                emphasis: { //鼠标滑过地图高亮的相关设置
                    borderWidth: .5,
                    borderColor: '#4b0082',
                    areaColor: "#fff",
                }
            },
            label: {
                normal: {
                    show: true, //省份名称
                    fontSize: 6,
                },
                emphasis: {
                    show: true,
                    fontSize: 6,
                }
            },
            data:[
            ]
        }
    ]
};

ec_center.setOption(option)