# Git 分支與推送學習紀錄

## 📅 日期: 2025年11月23-24日

## 🎯 學習目標
學習如何建立分支、提交變更、推送到 GitHub,以及理解 Pull Request 的流程

---

## 📚 學習內容

### 1. Git 分支操作

#### 建立新分支
```bash
git checkout -b originaloriginal
```
- 從 `main` 分支建立新分支 `originaloriginal`
- `-b` 表示建立並切換到新分支

#### 查看分支
```bash
git branch        # 查看本地分支
git branch -a     # 查看所有分支(包含遠端)
git branch -r     # 只查看遠端分支
```

#### 切換分支
```bash
git checkout main              # 切換到 main 分支
git checkout originaloriginal  # 切換到 originaloriginal 分支
```

---

### 2. 提交變更流程

#### 步驟:
1. **查看狀態**
   ```bash
   git status
   ```

2. **加入檔案到暫存區**
   ```bash
   git add data/originaloriginal.txt
   # 或加入所有變更
   git add .
   ```

3. **提交變更**
   ```bash
   git commit -m "Add originaloriginal.txt to demonstrate branch workflow"
   ```

4. **推送到遠端**
   ```bash
   git push -u origin originaloriginal
   ```

---

### 3. 查看歷史紀錄

#### 查看 commit 歷史
```bash
git log --oneline        # 簡潔模式
git log --oneline -10    # 只顯示最近 10 筆
```

#### 本次專案的歷史:
```
01edbb9 (HEAD -> originaloriginal) Add originaloriginal.txt to demonstrate branch workflow
5379274 (origin/main, origin/HEAD, main) Add emphasis to README project description
5cd1e9b Reorganize project structure for GitHub Pages deployment
51b2823 新增 JSON 學習程式與更新網頁樣式
dfbc492 初始提交：新增專案檔案
```

---

### 4. 回到舊版本的方法

#### 只是查看 (不改變檔案)
```bash
git log --oneline                    # 找到 commit ID
git checkout <commit-id>             # 回到該版本(唯讀)
git checkout originaloriginal        # 回到最新版
```

#### 恢復單一檔案
```bash
git checkout <commit-id> -- <檔案路徑>
```

#### 完全回退 (危險!)
```bash
git reset --hard <commit-id>   # 硬回退,刪除之後的變更
git reset --soft <commit-id>   # 軟回退,保留變更但取消 commit
```

---

### 5. Git 遠端操作

#### 查看遠端設定
```bash
git remote -v
```

#### 更改遠端 URL
```bash
git remote set-url origin <新的 URL>
```

#### 拉取遠端更新
```bash
git pull
```

---

### 6. 專案結構整理

#### 整理前:
```
visual code 練習/
├── herofinishjsonphar.html
├── style.css
├── json_example.py
├── notjson.js
└── student.json
```

#### 整理後:
```
visual code 練習/
├── .vscode/           # VS Code 設定檔
├── data/              # 資料檔案
│   ├── herr.json
│   ├── student.json
│   └── originaloriginal.txt
├── src/               # 程式原始碼
│   ├── json_example.py
│   └── notjson.js
├── index.html         # 主頁(改名自 herofinishjsonphar.html)
├── style.css
└── README.md
```

---

### 7. GitHub Pages 部署

#### 不需要 `.yml` 檔案的情況:
- ✅ 純靜態網頁 (HTML/CSS/JS)
- ✅ 不需要建置步驟
- ✅ 直接在 GitHub Settings → Pages 啟用即可

#### 需要 `.yml` (GitHub Actions) 的情況:
- TypeScript 需要編譯
- Sass/SCSS 需要轉換
- 需要自動化測試
- 複雜的建置流程

---

### 8. 遇到的問題與解決

#### 問題 1: 權限錯誤
```
Permission to kevinlin888908/my-app888908.git denied to lyixiong928-netizen
```

**原因:** 
- 本地 Git 使用 `lyixiong928-netizen` 帳號
- 儲存庫屬於 `kevinlin888908` 帳號

**解決方案:**
1. 在 GitHub 授權協作者權限
2. 或在 GitHub Desktop 切換帳號
3. 或重新建立儲存庫到有權限的帳號

#### 問題 2: 儲存庫不存在
```
The repository does not seem to exist anymore
```

**解決方案:**
1. 在 GitHub 重新建立儲存庫
2. 更新 remote URL
3. 推送所有分支

---

### 9. 本地伺服器測試

#### 啟動 Python HTTP Server
```bash
python -m http.server 8000
```

#### 訪問網頁
```
http://localhost:8000/index.html
```

#### 常見埠號:
- 80 = HTTP 標準埠
- 443 = HTTPS 標準埠
- 3000 = Node.js/React 常用
- 5000 = Flask 預設
- 8000 = Python HTTP Server 預設
- 8080 = 備用 HTTP 埠

---

### 10. Pull Request 流程 (尚未完成)

#### 標準流程:
1. ✅ 建立新分支
2. ✅ 做出變更並 commit
3. ⏳ 推送分支到 GitHub
4. ⏳ 在 GitHub 建立 Pull Request
5. ⏳ Code Review (可選)
6. ⏳ 合併 PR 到 main 分支
7. ⏳ 刪除已合併的分支 (可選)

---

## 💡 重要概念釐清

### 分支 (Branch)
- 像是平行宇宙,可以獨立開發功能
- 不影響主分支 (main)
- 開發完成後可以合併回主分支

### 資料夾名稱 vs 儲存庫名稱
- **本地資料夾名稱:** `visual code 練習`
- **GitHub 儲存庫名稱:** `my-app888908`
- 這兩者可以不同!沒有矛盾!

### .vscode 資料夾的用途
- 存放 VS Code 的專案設定
- 不應該放練習用的資料檔案
- 應該只包含:
  - `settings.json` (設定)
  - `launch.json` (偵錯)
  - `tasks.json` (任務)
  - `c_cpp_properties.json` (C/C++ 設定)

### 靜態網頁 vs 動態網頁
- **靜態網頁:** HTML/CSS/JS 直接執行,不需要伺服器處理
- **動態網頁:** 需要後端伺服器 (PHP/Python/Node.js)
- 本專案是靜態網頁,適合 GitHub Pages

---

## 📝 學習重點

1. **分支是獨立的開發線** - 可以安全地實驗新功能
2. **commit 是存檔點** - 可以隨時回到過去的狀態
3. **推送需要權限** - 確保帳號和儲存庫匹配
4. **專案結構很重要** - 清楚的組織讓開發更順暢
5. **本地測試很有用** - 推送前先確認網頁正常運作

---

## 🎯 下一步學習

1. ⏳ 成功推送分支到 GitHub
2. ⏳ 建立第一個 Pull Request
3. ⏳ 學習 Code Review 流程
4. ⏳ 合併 PR 到 main 分支
5. ⏳ 了解 Git Flow 工作流程
6. ⏳ 學習解決 merge conflicts

---

## 🔗 有用的資源

- Git 官方文件: https://git-scm.com/doc
- GitHub 指南: https://guides.github.com/
- GitHub Pages 文件: https://docs.github.com/en/pages
- VS Code Git 整合: https://code.visualstudio.com/docs/sourcecontrol/overview

---

## 📌 備註

這次學習過程雖然遇到權限和儲存庫問題,但理解了:
- Git 分支的概念和操作
- 專案結構的重要性
- 本地開發和遠端推送的流程
- GitHub 帳號權限管理

**錯誤訊息是學習的好機會!** 透過解決問題,更深入理解了 Git 的運作原理。

---

*紀錄者: GitHub Copilot*
*日期: 2025年11月24日*
