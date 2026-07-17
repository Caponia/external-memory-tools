# {{OWNER}} 的 AI 工作目录

本目录让多个 AI 工具共用一份本地外部记忆。实际位置：`{{ROOT_PATH}}`。

## 目录职责

- `Memory/`：长期记忆唯一真源。
- `Workspaces/`：具体任务和项目的工作资料，不自动进入长期记忆。
- `Exports/`：给无法读取本地文件的工具使用的脱敏快照，不是真源。
- `Archive/`：已结束资料，不能覆盖当前状态。
- `START-HERE.md`：人工导航入口。
- `AGENTS.md`、`CLAUDE.md` 等：可选的工具薄入口，只引用 `Memory/`。

开始使用前，先填写 `Memory/PROFILE.md`，再按需要填写 `Memory/PROJECTS.md` 和 `Memory/RULES.md`。不要把密码、Token、密钥、完整地址或账号信息写入本目录。
