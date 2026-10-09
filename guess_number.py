# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
import random

answer = random.randint(1, 100)
count = 0

print("猜数字小游戏：我想了一个 1 到 100 之间的数字。")

while True:
    try:
        guess = int(input("请输入你的猜测："))
    except ValueError:
        print("请输入有效的整数。")
        continue

    if not 1 <= guess <= 100:
        print("请输入 1 到 100 之间的数字。")
        continue

    count += 1

    if guess > answer:
        print("大了！")
    elif guess < answer:
        print("小了！")
    else:
        print(f"猜中了！答案是 {answer}，你一共猜了 {count} 次。")
        break
