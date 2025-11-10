import csv

def write_to_csv(filename, data, headers=None):
    """
    将数据写入CSV文件

    参数:
        filename (str): 要写入的CSV文件名
        data (list): 要写入的数据，格式为列表的列表，如[[row1_col1, row1_col2], [row2_col1, row2_col2]]
        headers (list, optional): CSV文件的表头，如果提供会作为第一行写入
    """
    try:
        # 使用with语句打开文件，确保文件正确关闭
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # 创建CSV写入器
            writer = csv.writer(csvfile)

            # 如果提供了表头，先写入表头
            if headers:
                writer.writerow(headers)

            # 写入数据行
            writer.writerows(data)

        print(f"成功将{len(data)}行数据写入到{filename}")
        return True

    except IOError as e:
        print(f"写入文件时发生错误: {e}")
    except Exception as e:
        print(f"发生意外错误: {e}")
    return False


if __name__ == "__main__":
    # 示例数据
    sample_data = [
        ["张三", 25, "工程师", "北京"],
        ["李四", 30, "设计师", "上海"],
        ["王五", 35, "产品经理", "广州"],
        ["赵六", 28, "开发工程师", "深圳"]
    ]

    # 表头
    headers = ["姓名", "年龄", "职业", "城市"]

    # 写入CSV文件
    write_to_csv("人员信息.csv", sample_data, headers)
