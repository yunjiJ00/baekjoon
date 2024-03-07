current_hour, current_minute = map(int, input().split())
cooking_time = int(input())
end_hour = (current_hour + (current_minute + cooking_time) // 60) % 24
end_minute = (current_minute + cooking_time) % 60
print(end_hour, end_minute)