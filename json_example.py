import json

# 1. 創建一個 Python 字典 (類似 JSON 格式)
student_data = {
    "name": "張小明",
    "age": 20,
    "courses": ["數學", "英文", "程式設計"],
    "grades": {
        "數學": 85,
        "英文": 92,
        "程式設計": 88
    },
    "is_active": True
}

# 2. 將資料寫入 JSON 檔案
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, ensure_ascii=False, indent=4)
print("✓ 已將資料寫入 student.json")

# 3. 從 JSON 檔案讀取資料
with open("student.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
print("\n✓ 從檔案讀取的資料:")
print(f"姓名: {loaded_data['name']}")
print(f"年齡: {loaded_data['age']}")
print(f"課程: {', '.join(loaded_data['courses'])}")

# 4. 修改資料並儲存
loaded_data["age"] = 21
loaded_data["courses"].append("物理")
loaded_data["grades"]["物理"] = 90

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(loaded_data, file, ensure_ascii=False, indent=4)
print("\n✓ 已更新資料 (年齡+1, 新增物理課程)")

# 5. 將 JSON 字串轉換為 Python 物件
json_string = '{"title": "學習JSON", "difficulty": "簡單", "hours": 2}'
parsed_data = json.loads(json_string)
print(f"\n✓ 解析 JSON 字串: {parsed_data['title']} - 難度: {parsed_data['difficulty']}")

# 6. 將 Python 物件轉換為 JSON 字串
new_obj = {"status": "完成", "score": 95}
json_output = json.dumps(new_obj, ensure_ascii=False)
print(f"\n✓ 轉換為 JSON 字串: {json_output}")
