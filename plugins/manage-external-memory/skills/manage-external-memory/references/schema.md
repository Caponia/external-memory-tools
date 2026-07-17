# 外部记忆库结构契约

## 目录树

```text
<root>/
├── README.md
├── START-HERE.md
├── Memory/
│   ├── README.md
│   ├── RULES.md
│   ├── PROFILE.md
│   ├── PROJECTS.md
│   ├── CHANGELOG.md
│   ├── INBOX/
│   │   └── README.md
│   └── WORKFLOWS/
│       └── README.md
├── Workspaces/
│   ├── README.md
│   ├── Projects/
│   └── Tasks/
├── Exports/
│   └── README.md
├── Archive/
│   └── README.md
└── 可选工具入口
    ├── AGENTS.md
    ├── CLAUDE.md
    ├── WORKBUDDY.md
    └── HERMES.MD
```

## 文件职责

| 文件或目录 | 职责 | 是否真源 |
|---|---|---|
| `Memory/README.md` | 记忆读取路由、优先级和更新入口 | 是 |
| `Memory/RULES.md` | 长期有效的协作、安全和写入边界 | 是 |
| `Memory/PROFILE.md` | 稳定且能改善协作的个人偏好与背景 | 是 |
| `Memory/PROJECTS.md` | 跨任务需要了解的项目状态索引 | 是 |
| `Memory/WORKFLOWS/` | 经验证、跨项目可复用的流程 | 是 |
| `Memory/CHANGELOG.md` | 主记忆的变更记录 | 是 |
| `Memory/INBOX/` | 尚未合并的候选更新，每次更新独立成文件 | 候选区 |
| `Workspaces/` | 具体任务和项目的工作资料 | 否 |
| `Exports/` | 给无法直接读取本地文件的工具使用的脱敏快照 | 否 |
| `Archive/` | 已结束资料；不得覆盖当前状态 | 否 |
| 工具入口文件 | 告诉各 AI 去哪里读取同一份真源 | 否 |

## 读取顺序

1. 完整读取 `Memory/README.md`。
2. 读取 `Memory/RULES.md`。
3. 只读取当前任务需要的 `PROFILE.md` 和 `PROJECTS.md` 部分。
4. 读取相关 `WORKFLOWS/` 文件。
5. 只有需要确认历史时才读取 `CHANGELOG.md`。

当前对话的明确指令优先于记忆。记忆冲突时优先采用日期更新且经过明确确认的记录；仍不确定时保留冲突并询问用户。

## 更新状态机

```text
聊天中提出候选
        ↓ 用户明确授权写入候选区
Memory/INBOX/独立候选文件
        ↓ 用户再次明确批准合并
更新主文件 + CHANGELOG
        ↓
候选文件标记已合并并保留
```

“提出候选”“写入 INBOX”“合并主记忆”是三个独立权限。任何一步都不能自动推导下一步的授权。

## 工具入口

- Codex：使用根目录 `AGENTS.md`。
- Claude Code：使用根目录 `CLAUDE.md`。
- WorkBuddy：把 `WORKBUDDY.md` 或 `Memory/README.md` 配置为工作区说明；是否自动加载必须在产品内验证。
- Hermes：使用根目录 `HERMES.MD`。
- 无本地文件访问能力的聊天工具：使用 `Exports/` 中人工生成并脱敏的快照，不建立第二份可写主库。

工具入口只记录读取路径和治理规则，不复制 `PROFILE.md`、`PROJECTS.md` 等内容。

## 分享边界

可以分享：空白模板、目录契约、初始化脚本、验证脚本、通用工具入口、候选更新流程。

不可直接分享：真实个人画像、真实项目状态、INBOX 候选内容、派生导出、私有工作流、凭据、账号标识、联系方式、完整地址或环境专用配置。

## 初始化约束

- 只在一个尚不存在的新路径中初始化。
- 不提供覆盖参数。
- 先 `--dry-run`，再执行创建，最后运行验证。
- 迁移现有库时新建空库并人工比较，不把初始化器当成合并器。
