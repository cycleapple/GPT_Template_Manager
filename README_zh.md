[English](https://github.com/cycleapple/GPT_Template_Manager) | 繁體中文
# GPT 指令管理器

GPT 指令管理器是一個用來創建和管理使用 GPT 模型產生文本的模板的網頁應用程式。使用者可以建立具有提示和提示描述的模板，並根據主題進行分類。模板可以進行編輯、刪除，並可以複製到剪貼板以用於生成文本。

## 開始使用

### 前置需求

要運行此應用程式，您需要：

* Python 3.7 或更高版本
* pip

### 安裝

1. 克隆此存儲庫到您的本地計算機：

```bash
git clone https://github.com/cycleapple/gpt-templates.git
```

2. 切換到專案目錄：

```bash
cd gpt-templates
```

3. 安裝必要的套件：

```bash
pip install -r requirements.txt
```

4. 初始化數據庫：

```bash
python app.py db init
python app.py db migrate
python app.py db upgrade
```

### 運行應用程式

要啟動應用程式，請運行：

```bash
python app.py
```

然後，打開瀏覽器，並前往 `http://localhost:5000`。

## 使用方法

### 創建模板

要創建新的模板，請在主頁面上單擊“創建區塊”按鈕，並填寫標題、提示、提示描述和類別字段。單擊“創建區塊”保存模板。

### 編輯模板

要編輯現有模板，請單擊模板卡片上的“編輯”按鈕並進行更改。單擊“保存”以更新模板。

### 刪除模板

要刪除模板，請單擊模板卡片上的“刪除”按鈕。

### 複製提示

要將提示複製到剪貼板，請單擊模板卡片上的“複製”按鈕。

### 按類別篩選模板

要按類別篩選模板，請單擊導航欄中的類別按鈕。

## 構建使用

* Flask - 一個 Python Web 框架
* Flask-SQLAlchemy - 一個 Flask 擴展，用於 SQLAlchemy
* Jinja - 一個 Web 模板引擎
* Bootstrap - 一個用於構建響應式網站的前端框架

## 授權

此專案採用 MIT 授權條款