from conn import *


class SourceDataDemo:
    def __init__(self):
        self.title = "Unbug商品后台数据可视化"
        self.counter = {"name": "商品总出库情况", "value": 53}
        self.counter2 = {"name": "商品总入库情况", "value": 65}
        result = refresh()  # 目的是依据数据库实时更新数据
        self.echart1_data = {"title": "品牌库存数", "data": result}
        self.echart2_data = {
            "title": "种类库存分布",
            "data": [
                {"name": "iPhone智能手环", "value": 47},
                {"name": "华为音箱", "value": 52},
                {"name": "小米蓝牙耳机", "value": 90},
            ],
        }
        self.echarts3_1_data = {
            "title": "颜色",
            "data": [
                {"name": "红色", "value": 47},
                {"name": "蓝色", "value": 52},
                {"name": "白色", "value": 90},
            ],
        }
        self.echarts3_2_data = {
            "title": "型号",
            "data": [
                {"name": "meta10", "value": 10},
                {"name": "p30", "value": 20},
                {"name": "air2", "value": 20},
                # {"name": "金融", "value": 30},
                # {"name": "学生", "value": 40},
                # {"name": "其他", "value": 50},
            ],
        }
        self.echarts3_3_data = {
            "title": "产品需求",
            "data": [
                {"name": "iPone手环", "value": 4},
                {"name": "华为手机", "value": 5},
                {"name": "小米手机", "value": 9},
                {"name": "海尔手机", "value": 8},
                {"name": "oppo手机", "value": 9},
                {"name": "其他", "value": 9},
            ],
        }
        self.echart4_data = {
            "title": "出入库趋势",
            "data": [
                {"name": "出库", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 5]},
                {"name": "入库", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8]},
            ],
            "xAxis": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "11", "12"],
        }
        self.echart5_data = {
            "title": "销售地区分布",
            "data": [
                {"name": "浙江", "value": 2},
                {"name": "上海", "value": 3},
                {"name": "江苏", "value": 3},
                {"name": "广东", "value": 9},
                {"name": "北京", "value": 15},
                {"name": "深圳", "value": 18},
                {"name": "安徽", "value": 20},
                {"name": "四川", "value": 13},
            ],
        }
        self.echart6_data = {
            "title": "主要销售地区情况",
            "data": [
                {
                    "name": "浙江",
                    "value": 80,
                    "value2": 20,
                    "color": "01",
                    "radius": ["59%", "70%"],
                },
                {
                    "name": "上海",
                    "value": 70,
                    "value2": 30,
                    "color": "02",
                    "radius": ["49%", "60%"],
                },
                {
                    "name": "广东",
                    "value": 65,
                    "value2": 35,
                    "color": "03",
                    "radius": ["39%", "50%"],
                },
                {
                    "name": "北京",
                    "value": 60,
                    "value2": 40,
                    "color": "04",
                    "radius": ["29%", "40%"],
                },
                {
                    "name": "深圳",
                    "value": 50,
                    "value2": 50,
                    "color": "05",
                    "radius": ["20%", "30%"],
                },
            ],
        }
        self.map_1_data = {
            "symbolSize": 100,
            "data": [
                {"name": "海门", "value": 239},
                {"name": "鄂尔多斯", "value": 231},
                {"name": "招远", "value": 203},
            ],
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            "title": data.get("title"),
            "xAxis": [i.get("name") for i in data.get("data")],
            "series": [i.get("value") for i in data.get("data")],
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            "title": data.get("title"),
            "xAxis": [i.get("name") for i in data.get("data")],
            "series": [i.get("value") for i in data.get("data")],
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            "title": data.get("title"),
            "xAxis": [i.get("name") for i in data.get("data")],
            "data": data.get("data"),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            "title": data.get("title"),
            "xAxis": [i.get("name") for i in data.get("data")],
            "data": data.get("data"),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            "title": data.get("title"),
            "xAxis": [i.get("name") for i in data.get("data")],
            "data": data.get("data"),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            "title": data.get("title"),
            "names": [i.get("name") for i in data.get("data")],
            "xAxis": data.get("xAxis"),
            "data": data.get("data"),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            "title": data.get("title"),
            "xAxis": [i.get("name") for i in data.get("data")],
            "series": [i.get("value") for i in data.get("data")],
            "data": data.get("data"),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            "title": data.get("title"),
            "xAxis": [i.get("name") for i in data.get("data")],
            "data": data.get("data"),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            "symbolSize": data.get("symbolSize"),
            "data": data.get("data"),
        }
        return echart


class SourceData(SourceDataDemo):
    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = "Unbug商品后台数据可视化"
