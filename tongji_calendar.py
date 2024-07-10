from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# 定义开始和结束日期
start_date = datetime(2024, 9, 2, tzinfo=pytz.timezone('Asia/Shanghai'))
end_date = datetime(2025, 1, 10, tzinfo=pytz.timezone('Asia/Shanghai'))

# 创建日历对象
calendar = Calendar()

# 计算总共的周数
week_number = 1

# 当前日期小于结束日期时循环
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 0:  # 检查是否为周一
        event = Event()
        event.name = f"Week {week_number}"
        event.begin = current_date.strftime('%Y-%m-%d')
        event.make_all_day()
        # 设置事件时区
        event.begin = event.begin.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
        calendar.events.add(event)
        week_number += 1
    current_date += timedelta(days=1)

# 保存ICS文件
with open('./data/tongji_calendar.ics', 'w') as my_file:
    my_file.writelines(calendar)