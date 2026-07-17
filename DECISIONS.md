# 决策记录

## 2026-07-17：公开分发使用 Codex Plugin Marketplace

- 决策：保留 ZIP 作为离线备用；正式公开分发采用独立 GitHub 仓库中的 skills-only Codex Plugin 与 Marketplace。
- 原因：接收者可以通过 Marketplace 添加仓库并在 `/plugins` 中安装，不需要从作者手中接收 ZIP；同时能把发布边界限制在空白模板、说明和本地脚本。
- 仓库边界：公开仓库不得包含真实外部记忆、父项目内容、凭据、私人路径、派生导出或使用中的工作区。
- 发布身份：GitHub 账号 `Caponia`，仓库名采用 `external-memory-tools`，发布者显示为 `caponia`。
- 许可证：MIT，版权标识为 `Copyright (c) 2026 caponia`。
- 发布结果：用户已明确授权上线；公开仓库 `https://github.com/Caponia/external-memory-tools` 已创建，`main` 已推送，远端提交和全新克隆验证通过。

## 2026-07-17：通用分发首选 Agent Skills 一条命令

- 决策：面向支持 Agent Skills 的 Agent，首选 `npx --yes skills@latest add Caponia/external-memory-tools -g -y`；该决策取代“Codex Plugin 是唯一正式公开分发方式”的默认顺序。
- 适用边界：它覆盖 Codex、Claude Code、Cursor、OpenCode 等兼容 Agent，但不承诺不支持 Agent Skills 的所有产品都能安装。
- 备用方式：Codex Plugin Marketplace 继续用于 Codex 的 Plugins 管理；ZIP 只用于离线或无法使用 Node.js/网络的场景。
- 依赖边界：一条命令要求 Node.js 18+，并使用 Vercel Labs 维护的第三方 `skills` CLI；公开文档必须说明其可能的匿名遥测以及 `DISABLE_TELEMETRY=1` 关闭方式。
- 安全原则：不采用 `curl | shell` 形式；安装源固定为公开 GitHub 仓库，发布前后都要做 Skill 发现、隔离安装、文件一致性、功能和隐私验证。

## 2026-07-17：公开脱敏任务记录

- 决策：根据用户明确要求，将脱敏后的 `TASK.md` 和 `DECISIONS.md` 加入现有公开仓库。
- 边界例外：这两份文件是“公开仓库不得包含父项目内容”规则的明确例外；其他父项目文件仍不得加入。
- 脱敏要求：用户代称统一写为“用户”，本机绝对路径改成通用描述，发布前重新执行凭据、联系方式和真实路径扫描。
