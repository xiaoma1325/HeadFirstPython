#! /usr/bin/python3
import athletemodel
import yate
import glob

data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)

# 从一个content-type开始
print(yate.start_response())
# 开始生成web页面，提供一个合适的标题
print(yate.include_header("Coach Kelly's List of Athletes"))
# 开始生成表单，提供要链接的服务器端程序的名称
print(yate.start_form("generate_timing_data.py"))
# 一个段落，告诉用户要做什么
print(yate.para("Select an athlete from the list to work with:"))

# 为各个选手分别生成一个单选钮
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
# 生成表单的最后创建一个定制的提交按钮
print(yate.end_form("select"))
# 结束web
print(yate.include_footer({"Home": "/index.html"}))




