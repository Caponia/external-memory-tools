# External Memory Tools｜外部记忆工具

这是一个遵循 [Agent Skills](https://agentskills.io/) 规范的 Skill，同时也提供 Codex Plugin。它能创建和安全维护本地 Markdown 外部记忆，让多个 AI 工具读取同一份记忆真源。

仓库中只有空白模板、说明和本地脚本，不包含任何人的真实画像、项目、候选记忆、导出文件或账号信息。

## 一条命令安装（推荐）

电脑先安装 [Node.js 18 或更高版本](https://nodejs.org/)，然后复制这一整行：

```bash
npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

这条命令会从本公开仓库下载 Skill，并全局安装到自动检测到的兼容 Agent。适用于支持 Agent Skills 的 Codex、Claude Code、Cursor、OpenCode 等工具。

安装完成后，重启 Agent 或新开任务，输入：

```text
$manage-external-memory 新手教程
```

如果你的 Agent 不使用 `$技能名` 语法，也可以直接说：

```text
使用 manage-external-memory 打开新手教程。
```

`skills` 是 Vercel Labs 维护的第三方安装器，并非本仓库或 OpenAI 内置组件。它默认可能收集匿名使用统计；如果希望关闭，可使用：

Windows PowerShell：

```powershell
$env:DISABLE_TELEMETRY="1"; npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

macOS、Linux 或 WSL：

```bash
DISABLE_TELEMETRY=1 npx --yes skills@latest add Caponia/external-memory-tools -g -y
```

安装器说明见 [skills CLI 文档](https://www.skills.sh/docs/cli)，完整数据访问说明见 [PRIVACY.md](PRIVACY.md)。

## Codex Plugin 安装（Codex 专用）

希望在 Codex 的 Plugins 页面管理版本时，先添加公开 Marketplace：

```bash
codex plugin marketplace add Caponia/external-memory-tools
```

然后任选一种方式：

1. 启动 Codex CLI，输入 `/plugins`。
2. 切换到 **External Memory Tools** Marketplace，安装 **External Memory Manager**。

也可以继续运行：

```bash
codex plugin add manage-external-memory@external-memory-tools
```

安装后新开一个 Codex 任务，输入：

```text
$manage-external-memory 新手教程
```

Skill 会在聊天中直接输出完整中文教程。“新手教程”只教学，不创建、不修改、也不扫描文件。

在 ChatGPT 桌面 App 中使用时，添加 Marketplace 后重启 App，再从 **Plugins** 中安装；安装后同样要新开任务。

## 第一次创建

Windows 示例：

```text
$manage-external-memory 帮我在 D:\My-AI 创建一套外部记忆。先预演，显示名称用“小明”，创建 Codex 和 Claude 入口。
```

`D:\My-AI` 和“小明”都是虚构示例，请换成自己的新目录和显示名称。WSL 可使用 `/mnt/d/My-AI`，Linux 或 macOS 可使用 `/home/example/My-AI`。

初始化器拒绝覆盖已有目录，也会拒绝在 WSL/Linux 中误用 Windows 盘符路径。

## 它会做什么

- 创建一套新的外部记忆目录，并先支持 dry run（预演）。
- 生成 Codex、Claude Code、WorkBuddy 和 Hermes 的薄入口。
- 默认只读取当前任务相关的记忆。
- 把“提出候选”“写入 INBOX”“合并主记忆”分成三次授权。
- 检查必需文件、未替换模板标记和敏感文件名。

## 它不会做什么

- 不联网、不上传、不发遥测、不调用远程 API。
- 不读取环境变量、浏览器、账号或凭据存储。
- 不自动同步到云端，也不自动 Git commit 或 push。
- 不覆盖、合并、删除已有记忆库。
- 验证器不扫描正文里的凭据；公开真实记忆前仍需人工复核。

## 仓库结构

```text
.
├── .agents/plugins/marketplace.json
├── plugins/manage-external-memory/
│   ├── .codex-plugin/plugin.json
│   └── skills/manage-external-memory/
├── CHANGELOG.md
├── LICENSE
├── PRIVACY.md
└── README.md
```

## 维护者：发布前检查

1. 确认版本号和 `CHANGELOG.md` 一致。
2. 运行 Plugin、Skill、初始化、ZIP（如提供）和隐私检查。
3. 确认这是独立 Git 仓库，提交内容中没有真实记忆或父目录文件，再发布。

## 许可证

[MIT](LICENSE) © 2026 caponia
