from ics import Calendar, Event
from datetime import datetime, timedelta


def generate_campus_calendar(calendar, start_date, total_weeks=18, description=None):
    current_date = start_date
    week_num = 1
    while week_num <= total_weeks:
        if current_date.weekday() == 0:  # 检查是否为周一
            event = Event()
            event.name = f"Week {week_num}"
            event.begin = current_date.strftime('%Y-%m-%d')
            event.make_all_day()
            if description:
                event.description = description
            calendar.events.add(event)
            week_num += 1
        current_date += timedelta(days=1)
        
    return calendar

    
if __name__ == '__main__':
    calendar = Calendar()
    
    start_date = datetime(2024, 9, 2)
    calendar = generate_campus_calendar(calendar, start_date, total_weeks=19, description="同济大学2024-2025学年第一学期校历")
    
    start_date = datetime(2025, 2, 24)
    calendar = generate_campus_calendar(calendar, start_date, total_weeks=23, description="同济大学2024-2025学年第二学期校历")
    
    # 保存ICS文件
    with open('./data/tongji_campus_calendar.ics', 'w') as my_file:
        my_file.writelines(calendar)
    