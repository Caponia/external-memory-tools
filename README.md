# External Memory Tools｜外部记忆工具

这是一个只包含 Skill 的 Codex Plugin。它能创建和安全维护本地 Markdown 外部记忆，让多个 AI 工具读取同一份记忆真源。

仓库中只有空白模板、说明和本地脚本，不包含任何人的真实画像、项目、候选记忆、导出文件或账号信息。

## 使用者：3 步安装

添加公开 Marketplace：

```bash
codex plugin marketplace add Caponia/external-memory-tools
```

然后：

1. 启动 Codex CLI，输入 `/plugins`。
2. 切换到 **External Memory Tools** Marketplace，安装 **External Memory Manager**。
3. 新开一个 Codex 任务，输入：

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

完整数据访问说明见 [PRIVACY.md](PRIVACY.md)。

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
