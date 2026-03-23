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

## 附录
**以下是一些最常用、以及可能对你当前研究非常有帮助的具体分类代码：**

**1. 计算机科学核心领域 (Computer Science, cs.*)**
cs.LG (Machine Learning - 机器学习)：涵盖所有机器学习算法、深度学习模型的基础研究。
cs.CL (Computation and Language - 计算与语言)：如果你关注 大语言模型 (LLM)、自然语言处理 (NLP)、文本分析，这是每天必看的分类。
cs.AI (Artificial Intelligence - 人工智能)：偏向 AI 综合理论、专家系统、逻辑推理等。
cs.CV (Computer Vision - 计算机视觉)：图像处理、图像生成、目标检测。
cs.GT (Computer Science and Game Theory - 计算机科学与博弈论)：涉及动态定价、纳什均衡、机制设计以及多智能体竞争模型的论文通常发布在这里。
cs.RO (Robotics - 机器人学)：机器人控制、运动规划。
cs.SE (Software Engineering - 软件工程)：代码生成、自动化测试、软件架构。

**2. 数学与交叉学科 (Math / Econ)**
math.OC (Optimization and Control - 优化与控制)：如果你在做启发式算法、演化算法或者复杂系统的约束优化，这里会有最前沿的数学推导和代理模型研究。
econ.TH (Theoretical Economics - 理论经济学)：涉及微观经济学中的竞争模型（如 Hotelling 模型等）。
stat.ML (Machine Learning - 统计机器学习)：偏向统计学视角的机器学习推导，与 cs.LG 经常交叉提交。

**3.进化优化**
cs.NE (Neural and Evolutionary Computing - 神经与进化计算)：所有关于进化算法（EA）、遗传算法（GA）、粒子群优化（PSO）以及它们在复杂系统中的应用，都会首发在这个类别下。
math.OC (Optimization and Control - 优化与控制)
cs.LG (Machine Learning - 机器学习)

💡 进阶技巧：如何写出更精准的 Query
在 arxiv 库中，query 其实是一个支持逻辑运算符的搜索框。你不仅可以搜分类，还可以把分类和具体的关键字结合起来，实现极其精准的定向追踪。

示例 1：追踪特定分类下的特定技术
如果你只关心自然语言处理领域的“大语言模型”：
```Python
# cat 表示分类，all 表示全文包含
query = 'cat:cs.CL AND all:"large language model"'
```
示例 2：同时追踪博弈论和优化算法中的“定价”问题
如果你想跨领域寻找包含特定关键词的文章：

```Python
# ti 表示标题包含
query = '(cat:cs.GT OR cat:math.OC) AND ti:"dynamic pricing"'
```
示例 3：追踪多类别的纯最新论文
如果你想同时看机器学习和博弈论：

```Python
query = 'cat:cs.LG OR cat:cs.GT'
```
