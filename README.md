# 🤖 PaperBot: 你的学术前沿自动化追踪助手

PaperBot 是一个基于 Python 和 GitHub Actions 构建的轻量级、零成本的自动化学术跟进工具。它能够每天定时从 arXiv 抓取指定领域的最新论文，利用大语言模型（LLM）进行专业级的翻译与结构化提炼，并自动推送到飞书工作群。

无论你是科研工作者还是算法工程师，PaperBot 都能帮你从浩如烟海的文献中解放出来，每天早晨只需花 1 分钟，即可精准掌握本领域的最新技术突破。

## ✨ 核心特性

* **🔄 全自动化运行**：基于 GitHub Actions 的定时任务（Cron），无需自建服务器，真正实现 Serverless 和零运维。
* **🧠 LLM 深度提炼**：接入智谱大模型（GLM-4），不只是简单摘抄，而是按“中文标题、主要内容、核心创新、优势突破”的结构输出高度凝练的学术快讯。
* **🆓 完全零成本**：完美利用 GitHub 免费额度与智谱基础模型免费 API，无需为基础设施和算力支付任何费用。
* **📱 飞书丝滑集成**：通过 Webhook 原生推送到飞书群，配合 Emoji 排版，打造极致的移动端阅读体验。

## 🚀 部署指南 (仅需 3 步)

如果你想在自己的 GitHub 账户下运行此机器人，请按照以下步骤操作：

### 1. Fork 本仓库
点击右上角的 `Fork` 按钮，将本项目复制到你的个人账号下。

### 2. 配置环境变量 (Secrets)
在你的仓库页面，依次点击 `Settings` -> `Secrets and variables` -> `Actions`，点击 `New repository secret`，添加以下两个必备密钥：

* `API_KEY`：你的智谱 AI 开放平台 API 密钥。
* `FEISHU_URL`：你的飞书群自定义机器人的 Webhook 链接。

### 3. 启用 GitHub Actions 工作流
1. 进入仓库的 `Actions` 选项卡。
2. 点击 `I understand my workflows, go ahead and enable them` 允许工作流运行。
3. （可选）你可以点击左侧的 `arxiv-daily`，然后点击右侧的 `Run workflow` 进行一次手动测试。

## ⚙️ 个性化配置

你可以通过修改代码文件，轻松将 PaperBot 定制为你专属的研究方向：

* **更改论文领域**：打开 `arxiv_fetch.py`，修改 `query="cs.IR"` 为你关注的领域（例如 `cs.CV` 计算机视觉，或具体的关键字 `"machine learning"`）。
* **更改抓取数量**：打开 `arxiv_fetch.py`，修改 `limit=5` 的数值。
* **更改推送时间**：打开 `.github/workflows/main.yml`，修改 `cron: '0 3 * * *'`（当前为北京时间每天上午 11:00，注意 Cron 表达式使用的是 UTC 时间）。

## 🛠️ 技术栈
* [Python 3.8+](https://www.python.org/)
* [arxiv (Python Library)](https://pypi.org/project/arxiv/)
* [智谱 AI (GLM-4)](https://open.bigmodel.cn/)
* GitHub Actions
