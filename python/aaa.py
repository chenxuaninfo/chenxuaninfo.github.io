from pyecharts import Overlap
overlap = Overlap()
bar = Bar("柱状图-折线图合并", "一年的降水量与蒸发量")
bar.add("降水量", columns, data1, mark_point=["max", "min"])
bar.add("蒸发量", columns, data2, mark_point=["max", "min"])
overlap.add(bar)
overlap.add(line)
overlap.render()