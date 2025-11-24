from pyecharts.charts import Bar
from pyecharts import options as opts


# 创建一个柱状图对象
bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .set_global_opts(title_opts=opts.TitleOpts(title="示例柱状图", subtitle="这是一个简单的示例"))
)

# 渲染图表到 HTML 文件
bar.render("bar_chart.html")

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 也可以传入路径参数，如 bar_chart.render("bar_chart.html")
bar_chart.render()
# bar_chart.render("bar_chart.html")
