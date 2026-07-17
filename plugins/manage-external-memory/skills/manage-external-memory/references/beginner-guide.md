# 外部记忆 Skill 新手教程

> 这是一份纯说明。本教程不会创建、修改或扫描你的任何文件。

## 目录

1. 30 秒看懂它是什么
2. 先判断你属于哪种情况
3. 第一次创建外部记忆
4. 看懂生成的文件
5. 第一次填写内容
6. 平时怎么使用
7. 怎么安全更新记忆
8. 怎么给多个 AI 共用
9. 怎么分享给别人
10. 不能放进记忆的内容
11. 常见问题
12. 不安装 Skill 的手动用法
13. 一页速查

## 1. 30 秒看懂它是什么

把外部记忆想成一本放在你电脑里的“AI 总笔记本”。

- Codex、Claude 等 AI 都来读同一本笔记。
- 你的长期偏好、项目状态和常用流程写在里面。
- AI 自带的聊天记忆只是辅助，不能反过来覆盖这本总笔记。
- 这本笔记默认只能读。想修改时，先把草稿放进 `INBOX`，你确认后才能正式合并。

这个 Skill 就像“笔记管理员”，能帮你：

- 从零建立空白记忆库。
- 告诉不同 AI 去哪里读同一份记忆。
- 按正确顺序读取已有记忆。
- 先给出修改草稿，经过你确认后再写。
- 检查目录是否完整。

你只需要记住三句话：

1. 只有一份记忆真源。
2. 默认只读。
3. 更新先进入 `INBOX` 草稿箱。

## 2. 先判断你属于哪种情况

### 情况 A：我从来没有外部记忆

让 Skill 在一个全新的目录中创建。直接复制：

```text
$manage-external-memory 帮我在 D:\My-AI 创建一套外部记忆。先预演，显示名称用“小明”，创建 Codex 和 Claude 入口。
```

把“小明”和 `D:\My-AI` 换成你自己的称呼与路径。

### 情况 B：我已经有外部记忆

不要再次初始化。让 Skill 读取现有目录：

```text
$manage-external-memory 按 D:\My-AI 开始本次任务。只读取与当前问题有关的内容，并告诉我读取了哪些文件。
```

`D:\My-AI` 是虚构示例，请换成你的实际根目录。

### 情况 C：我想修改长期记忆

先只看草稿，不写文件：

```text
$manage-external-memory 我希望以后回答更简洁。先给出长期记忆候选，不要写文件。
```

确认草稿后再说：

```text
候选内容确认，写入 INBOX，但不要修改主记忆。
```

再次检查无误后才说：

```text
这个 INBOX 候选确认合并。请更新对应主文件和 CHANGELOG，完成后重新读取验证。
```

### 情况 D：我只想把工具分享给别人

推荐把空白 Skill 放进公开 GitHub 仓库。接收者只需一条命令，就能安装到支持 Agent Skills 的 Codex、Claude Code、Cursor、OpenCode 等 Agent：

```bash
npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

Codex 用户还可以通过 Plugin Marketplace 安装。ZIP 只作为离线备用方式。无论用哪种方式，都不要分享你已经填写过的 `Memory`、`INBOX`、`Exports` 或私人工作区。

## 3. 第一次创建外部记忆

### 第一步：选择一个新目录

示例：

```text
D:\My-AI
```

`D:\My-AI` 是 Windows 虚构示例。WSL 可用 `/mnt/d/My-AI`，Linux 或 macOS 可用 `/home/example/My-AI`；这些也都是虚构路径，请换成自己的新目录。

目标目录必须还不存在。这样可以确保初始化器不会覆盖旧文件。不要在 WSL/Linux 命令中直接使用 `D:\My-AI`；初始化器会拒绝混用路径格式，避免把文件建错位置。

如果提示“目标已经存在”，不是程序坏了，而是安全保护生效。已有记忆请使用“读取已有记忆”，需要迁移时请新建空目录后人工比较。

### 第二步：选择 AI 入口

入口就是告诉某个 AI：“总笔记在这里”。

- `codex`：生成 `AGENTS.md`。
- `claude`：生成 `CLAUDE.md`。
- `workbuddy`：生成 `WORKBUDDY.md`。
- `hermes`：生成 `HERMES.MD`。
- `all`：四种全部生成。

如果拿不准，只选 `codex`。以后可以人工增加其他入口。

### 第三步：先预演

Skill 会先告诉你准备创建哪些文件，但不真正写入。确认目标路径正确后，再让它执行创建。

### 第四步：创建并验证

创建完成后，Skill 会运行验证器，检查：

- 必需文件是否齐全。
- 模板中的占位文字是否已替换。
- 是否出现 `.env`、密钥文件等敏感文件名。
- 工具入口是否生成。

验证通过不代表文件内容绝对没有隐私。以后对外分享真实记忆前，仍要人工检查。

## 4. 看懂生成的文件

```text
你的根目录/
├── START-HERE.md
├── Memory/
├── Workspaces/
├── Exports/
├── Archive/
└── AGENTS.md 等工具入口
```

用最简单的话解释：

- `START-HERE.md`：导航页，不知道从哪里开始就看它。
- `Memory/README.md`：总目录，告诉 AI 先读什么、后读什么。
- `Memory/RULES.md`：家规，记录 AI 长期必须遵守的边界。
- `Memory/PROFILE.md`：你的使用习惯，例如语言、表达和工作偏好。
- `Memory/PROJECTS.md`：项目索引，只写当前状态和入口，不放所有操作细节。
- `Memory/INBOX/`：待审批草稿箱。还没有正式进入长期记忆。
- `Memory/WORKFLOWS/`：已经验证、以后还会重复使用的办事流程。
- `Memory/CHANGELOG.md`：正式记忆的修改记录。
- `Workspaces/`：实际干活的地方，放任务和项目资料。
- `Exports/`：给不能读本地文件的 AI 使用的脱敏副本，不是真源。
- `Archive/`：已经结束的旧资料。
- `AGENTS.md`、`CLAUDE.md` 等：工具入口，不存完整记忆，只告诉 AI 去哪里读。

## 5. 第一次填写内容

不要一口气填写所有文件。让 AI 每次只问一个问题：

```text
$manage-external-memory 带我完成首次设置。每次只问一个小问题，先从沟通和工作偏好开始；先给候选内容，不要写文件。
```

建议顺序：

1. `PROFILE.md`：先填语言、回答长短、工作方式等稳定偏好。
2. `RULES.md`：再填不能擅自做什么、什么操作必须确认。
3. `PROJECTS.md`：最后填写当前项目的简短索引。
4. `WORKFLOWS/`：真正重复使用并验证过以后再添加，不必第一天就写。

适合写进长期记忆的内容：

- 长期稳定的沟通偏好。
- 多个任务都会用到的工作规则。
- 当前项目的状态和入口。
- 已经验证、以后还会重复使用的流程。

不适合写进长期记忆的内容：

- 一次性聊天内容。
- 临时猜测或还没有确认的结论。
- 单个项目的全部操作日志。
- 密码、Token、密钥和私人联系方式。

## 6. 平时怎么使用

### 开始一次普通工作

```text
$manage-external-memory 按 D:\My-AI 开始本次任务，只读取相关记忆，然后帮我处理这件事：……
```

### 只查看当前结构

```text
$manage-external-memory 检查 D:\My-AI 的结构，只读，不要修改任何文件。
```

### 检查记忆是否完整

```text
$manage-external-memory 验证 D:\My-AI 的外部记忆结构，告诉我缺少什么，不要自动修复。
```

### 查看当前记住了什么

```text
$manage-external-memory 只读检查我的外部记忆，用简短清单告诉我当前有哪些长期偏好、项目索引和工作流，不要复述敏感信息。
```

AI 应该只读取当前任务需要的部分，而不是每次把整个记忆库全部加载。

## 7. 怎么安全更新记忆

更新分成三个独立权限：

```text
第一步：聊天中提出候选，不写文件
第二步：你确认后写入 INBOX
第三步：你再次确认后合并主记忆
```

授权第二步，不代表自动授权第三步。

这样设计有三个好处：

- 防止 AI 自作主张记住错误内容。
- 让你在正式写入前看清楚文字。
- 多个 AI 同时使用时，不会一起抢着修改主文件。

## 8. 怎么给多个 AI 共用

所有工具都读取同一个 `Memory/`，不要复制多份主记忆。

- Codex：把根目录作为工作区，使用 `AGENTS.md`。
- Claude Code：打开同一个根目录，使用 `CLAUDE.md`。
- WorkBuddy：把 `WORKBUDDY.md` 或 `Memory/README.md` 配置成长期说明。
- Hermes：使用 `HERMES.MD`。
- 不能直接读取本地文件的聊天工具：人工生成脱敏快照放进 `Exports/` 后上传。

入口文件存在，不等于某个产品已经自动加载。新开任务后可以问：

```text
请告诉我你实际读取了哪些入口和记忆文件；没有读取到的不要猜。
```

## 9. 怎么分享给别人

推荐方式：把空白 Skill 放进独立的公开 GitHub 仓库。不要把正在使用的记忆根目录放进这个仓库。

接收者电脑先安装 Node.js 18 或更高版本，然后复制这一整行：

```bash
npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

这条命令会下载公开仓库，并把 Skill 全局安装到自动检测到的兼容 Agent。安装完成后重启 Agent 或新开任务，再输入：

```text
$manage-external-memory 新手教程
```

如果 Agent 不使用 `$技能名` 语法，直接说“使用 manage-external-memory 打开新手教程”也可以。

`skills` 是 Vercel Labs 维护的第三方安装器，不是本 Skill 或 OpenAI 的内置组件。它默认可能收集匿名使用统计。希望关闭时：

Windows PowerShell：

```powershell
$env:DISABLE_TELEMETRY="1"; npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

macOS、Linux 或 WSL：

```bash
DISABLE_TELEMETRY=1 npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

Codex 用户如果希望在 Plugins 页面管理版本，也可以使用专用方式：

```bash
codex plugin marketplace add Caponia/external-memory-tools
```

然后进入 Codex CLI，输入 `/plugins`，在 **External Memory Tools** Marketplace 中安装 **External Memory Manager**。也可以继续运行：

```bash
codex plugin add manage-external-memory@external-memory-tools
```

如果暂时不发布 GitHub，也可以发送没有填写私人内容的原始 ZIP，作为离线备用方式。

分享前检查：

- 仓库或 ZIP 中只有 Plugin/Skill、空白模板、脚本和说明。
- 没有你真实的 `PROFILE.md`。
- 没有真实项目清单。
- 没有 `INBOX` 候选内容。
- 没有 `Exports` 快照。
- 没有密码、Token、密钥、地址或联系方式。

不要把自己已经使用中的整个根目录提交到 GitHub 或压缩后发给别人。

## 10. 不能放进记忆的内容

不要保存：

- 密码、Token、API Key、Cookie。
- SSH 私钥或其他密钥文件。
- `.env`、`.dev.vars` 的内容。
- 银行卡、证件号、完整住址和私人联系方式。
- 不必要的账号标识。
- 可以直接操作付费或线上系统的凭据。

可以这样写：

```text
凭据保存在密码管理器中，不进入共享记忆。
```

不要写具体值，也不要写具体密钥位置。

## 11. 常见问题

### 提示“目标已经存在”怎么办？

这是防覆盖保护。新建记忆请选择一个不存在的路径；已有记忆不要重新初始化。

### 输入 `$manage-external-memory` 没反应怎么办？

先重启 Agent 或新开任务。通用安装后，常见的 Skill 源目录是：

```text
~/.agents/skills/manage-external-memory/SKILL.md
```

安装器还会为检测到的 Agent 建立对应入口。请查看安装命令最后列出的目标 Agent；如果没有列出你正在使用的工具，请确认它是否支持 Agent Skills。也可以不用 `$` 语法，直接说“使用 manage-external-memory 打开新手教程”。

### 为什么教程没有自动创建文件？

这是正确行为。“新手教程”只负责说明，不做任何写入。需要创建时再明确说“帮我在某个新路径创建”。

### 为什么 AI 没有自动读到记忆？

不同工具加载入口的方式不同。先确认打开的是记忆根目录，再让 AI 列出它实际读取的文件。没有验证时不要假设已经加载。

### 多台电脑会自动同步吗？

不会。这个 Skill 负责建立本地真源，不负责云同步和备份。同步方案需要你另外选择，并避免同步凭据。

### 能直接修改 `PROFILE.md` 吗？

可以人工编辑，但使用 AI 时推荐先走候选流程，避免错误内容直接进入长期记忆。

### 验证通过就一定可以公开分享吗？

不一定。验证器只检查结构、占位符和敏感文件名，不扫描所有正文中的私人信息。公开分享前仍需人工阅读。

## 12. 不安装 Skill 的手动用法

这一节是备用方法。看不懂命令行可以跳过，直接安装 Skill 使用。

电脑需要 Python 3。在分享包解压目录运行预演。下面是 Windows PowerShell 示例：

```bash
python manage-external-memory/scripts/init_memory.py --root "D:\My-AI" --owner "小明" --adapters codex,claude --dry-run
```

确认路径正确后，去掉 `--dry-run` 创建：

```bash
python manage-external-memory/scripts/init_memory.py --root "D:\My-AI" --owner "小明" --adapters codex,claude
```

最后验证：

```bash
python manage-external-memory/scripts/validate_memory.py --root "D:\My-AI"
```

如果你在 WSL 中运行 Python，请把路径改成 `/mnt/d/My-AI`；Linux 或 macOS 请使用本机路径。

## 13. 一页速查

一条命令安装：

```bash
npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

打开完整教程：

```text
$manage-external-memory 新手教程
```

创建新记忆：

```text
$manage-external-memory 帮我在 D:\My-AI 创建外部记忆，先预演，创建 Codex 和 Claude 入口。
```

读取已有记忆：

```text
$manage-external-memory 按 D:\My-AI 开始任务，只读取相关内容。
```

首次填写：

```text
$manage-external-memory 带我完成首次设置，每次只问一个问题，先给候选，不要写文件。
```

提出更新：

```text
$manage-external-memory 把这条内容整理成长期记忆候选，不要写文件：……
```

写入候选区：

```text
候选确认，写入 INBOX，但不要合并主记忆。
```

合并主记忆：

```text
这个 INBOX 候选确认合并，请更新主文件和 CHANGELOG 并验证。
```

只读检查：

```text
$manage-external-memory 检查 D:\My-AI 的结构，只读，不要修复。
```

现在可以选择下一步：

1. 从零创建一套外部记忆。
2. 连接并读取已有外部记忆。
3. 一步一步完成首次填写。
4. 学习如何安全更新记忆。
5. 只保留本教程，暂时不操作。
