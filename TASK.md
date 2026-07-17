# 创建外部记忆的技能

## 创建日期

2026-07-17

## 所属项目

技能创建

## 背景

用户希望了解本地外部记忆目录的结构和创建方式，并把其中可复用的方法做成不包含私人内容、可以分享给别人使用的版本。

## 目标

盘点现有外部记忆架构与创建历史，交付一套“工具无关的 Markdown 核心 + Codex Skill + 初始化/验证脚本 + 中文说明”的可分享版本。

## 成功标准

- 已确认任务范围和必要约束。
- 已检查输入文件，不覆盖原始资料。
- 已生成新的交付物并保存在 output 目录。
- 已完成与任务风险相称的实际验证。
- 已在完成记录中写明结果和遗留问题。

## 输入

- 将原始文件放入 input 目录；不要把凭据或密钥放入任务目录。

## 输出

- `output/本地外部记忆说明.md`：现有结构、读取/更新流程和创建历史。
- `output/shareable-external-memory/`：可安装 Skill 和中文使用说明。
- `output/shareable-external-memory-v1.1.3.zip`：当前可直接发送的离线分享包；旧版本保留作历史记录。
- `output/public-repo/manage-external-memory-marketplace/`：可发布到 GitHub 的独立 Codex Plugin Marketplace 仓库。

## 约束

- 开始前阅读本地外部记忆目录中的 README.md 和 RULES.md。
- 长期记忆默认只读。
- 只处理当前任务范围，不顺便修改无关内容。
- 不擅自 Git commit 或 push。
- 不覆盖输入文件或已有交付物。
- 需要用户确认的事项先确认，再继续执行。

## 启动与确认流程

1. 第一轮只进行需求确认，不执行任务、不修改文件、不连接服务器，也不创建正式计划文件。
2. 向用户复述：具体目标、最终交付物、包含与不包含的范围、成功标准、当前假设，以及需要确认的歧义或风险。
3. 只询问会实质影响结果的问题，不为了流程而提问；相关问题尽量集中一次提出。
4. 复述后必须停下，等待用户明确回复“需求确认，可以制定计划”。
5. 收到需求确认后，给出简短的“步骤 -> 验证”计划，并再次停下等待确认。
6. 只有用户明确回复“计划确认，可以开始执行”后，才能进入执行阶段。
7. 如果用户明确要求合并或跳过某个确认阶段，以用户当前指令为准。

## 执行计划

1. 只读盘点现有外部记忆目录、入口与创建链路，并用本地文件验证。
2. 提炼通用规则，隔离个人数据、绝对路径和敏感信息。
3. 按 `skill-creator` 规范创建模板核心、Codex Skill、初始化器、验证器和使用说明。
4. 在临时目录预演并从零初始化，验证结构、入口、拒绝覆盖和分享包完整性。
5. 记录实际验证结果和已知边界。

## 当前状态

已完成

## 完成记录

完成日期：2026-07-17

### 实际结果

- 确认现有系统由 Markdown 单一真源、工具薄入口以及任务/项目工作区组成；原系统是在 2026-07-13 的统一工作流任务中一次性建立，并没有通用记忆库初始化器。
- 创建 `manage-external-memory` Skill，包含结构契约、空白模板、Codex/Claude/WorkBuddy/Hermes 入口、跨平台初始化脚本和验证脚本。
- 分享版不包含现有 `PROFILE.md` 内容、真实项目、INBOX 候选、私有工作流、派生快照或固定个人路径。
- 采用“工具无关 Markdown 真源 + 各工具薄入口”；后续已封装成只包含 Skill 的 Codex Plugin，不引入不需要的 MCP 或应用连接器。

### 验证结果

- `quick_validate.py`：`Skill is valid!`
- 初始化器 `--dry-run`：成功，确认未创建目标目录。
- 从源目录初始化：成功生成 Codex、Claude、WorkBuddy、Hermes 四种入口。
- 结构验证器：必需文件、入口和敏感文件名检查通过。
- 重复指向已有目标：按设计返回失败，未覆盖文件。
- 非法模板标记显示名称：按设计拒绝。
- 分享目录私人项目名、当前用户路径、IP 和邮箱模式扫描：未发现匹配。
- ZIP 完整性测试：通过；从最终 ZIP 解压后重新初始化并验证通过。
- ZIP SHA-256：`9967b014ff0cb9cfec8e009044230dd9d654f0fcbedb30e3487fe072c19a23cf`。

### 已知边界

- 未安装到当前全局 Codex Skill 目录；交付物是可安装包。
- 未在 Codex、Claude、WorkBuddy 或 Hermes 产品界面内验证自动加载状态。
- 不负责云同步、设备间备份或把已有记忆自动迁移到新结构。
- 验证器不扫描文件内容中的凭据；对外分享前仍需人工检查实际填写内容。

### 2026-07-17 后续改进：新手教程

- 根据用户的反馈增加第一优先级触发词：“新手教程”“小白教程”“怎么用”“使用说明”。
- 用户输入 `$manage-external-memory 新手教程` 后，Skill 必须把完整教程直接展示在聊天中，不得只返回摘要、目录或本地文件路径。
- 教程覆盖基本概念、用户情形判断、首次创建、目录解释、首次填写、日常使用、三阶段更新、多 AI 共用、分享边界、安全红线、常见问题、手动用法和一页速查。
- 教程模式明确禁止创建、修改或扫描任何记忆文件；输出教程后停止其他操作。
- 更新 `agents/openai.yaml`，把默认提示改为打开新手教程。
- `quick_validate.py` 再次通过；教程完整性、Markdown 代码围栏、触发优先级、无副作用规则和隐私关键词扫描通过。
- 从 `shareable-external-memory-v1.1.0.zip` 解压后确认教程与触发规则存在，并再次完成四入口初始化和结构验证。
- v1.1.0 ZIP SHA-256：`abfaf6143ca3c250c947feec8290c162d633502e5a5a5419ae819d3ebf37a9f3`。

### 2026-07-17 后续改进：GitHub Plugin Marketplace 发布版

- 将公开示例统一改为明确的虚构路径：Windows 使用 `D:\My-AI`，WSL 使用 `/mnt/d/My-AI`，Linux/macOS 使用 `/home/example/My-AI`。
- 初始化器新增路径格式保护：非 Windows Python 遇到 Windows 盘符路径时明确拒绝，不会在当前目录创建错误文件。
- 按 OpenAI 官方 Plugin 结构创建独立发布仓库，包含 `.agents/plugins/marketplace.json`、`.codex-plugin/plugin.json`、公开 Skill、中文 README 和 `PRIVACY.md`。
- 发布仓库已初始化为独立 `main` Git 仓库，确认没有提交或父仓库内容；未执行 stage、commit 或 push。
- 接收者发布后可运行 `codex plugin marketplace add Caponia/external-memory-tools`，再通过 `/plugins` 安装并新开任务使用，不需要接收 ZIP。
- Plugin validator、Skill validator、两个 JSON 解析均通过。
- dry run、四入口真实初始化、结构验证、拒绝覆盖和 WSL 路径误用保护均通过。
- 公开文件扫描共覆盖 55 个文本文件：没有高置信凭据、邮箱/IP/手机号模式、真实本机路径、已知本地标识、敏感文件名、符号链接、特殊文件或脚本联网/环境变量/子进程 API。
- v1.1.1 ZIP 与源目录逐字节一致，共 24 个文件；无绝对路径、路径穿越、重复项、注释或符号链接。
- v1.1.1 ZIP SHA-256：`1e4444b1eeb8ebdbeb5f3aea01ce9501d822fde1e4ee0bcb69c6498718d4ad30`。

### 2026-07-17 发布身份与许可证定稿

- GitHub 账号：`Caponia`；仓库名采用 Marketplace 名称 `external-memory-tools`。
- 开源许可证：MIT；版权标识为 `Copyright (c) 2026 caponia`。
- 对外显示的发布者：`caponia`。
- Plugin 元数据、README、新手教程、隐私链接、`LICENSE` 和 `CHANGELOG.md` 已全部补齐，版本升级为 1.1.2。
- 本地 origin 已设置为 `https://github.com/Caponia/external-memory-tools.git`。
- v1.1.2 ZIP 与源目录逐字节一致，共 24 个文件；旧 v1.1.1 ZIP 哈希复核未变化。
- v1.1.2 ZIP SHA-256：`0d548f0ab23232de633d7bc99751e11de8de6b8f08f114ce3582c52f42d6d50a`。

### 2026-07-17 GitHub 正式发布

- 用户明确授权创建公开仓库、commit 和 push。
- 创建初始提交 `e2dcfbfd9b5d33303420d43f0b3672a56af639a2`，提交说明为 `feat: publish external memory plugin`。
- 已创建并推送公开仓库：`https://github.com/Caponia/external-memory-tools`，默认分支为 `main`，许可证由 GitHub 识别为 MIT。
- 从 GitHub 全新克隆远端仓库后，确认远端提交与本地提交完全一致，共 31 个公开文件，工作树干净。
- 对全新克隆再次运行 Plugin validator 与 Skill validator，均通过；Marketplace、版本 1.1.2、仓库 URL、MIT 元数据和 README 安装命令均正确。
- 对全新克隆再次扫描高置信凭据和真实本机路径，未发现匹配。

### 2026-07-17 通用一条命令安装版

- 面向支持 Agent Skills 的 Agent，公开推荐命令更新为 `npx --yes skills@latest add Caponia/external-memory-tools -g -y`；Codex Plugin Marketplace 保留为 Codex 专用方式，ZIP 保留为离线备用。
- README、完整新手教程和离线使用说明已把通用安装放到第一入口，并明确 Node.js 18+ 前提、第三方 `skills` CLI 边界、匿名遥测说明及关闭方式。
- Plugin 版本升级到 1.1.3；Plugin validator、Skill validator、JSON、文档命令、源 Skill 一致性和 Git diff 检查均通过。
- dry run、四入口真实初始化、结构验证、拒绝覆盖、非 Windows 环境盘符误用保护均通过。
- 公开仓库与离线分享源共检查 55 个文本文件：未发现高置信凭据、邮箱/IP/手机号、真实本机路径、敏感文件名、符号链接、NUL、非 UTF-8 文件或脚本联网/环境变量/子进程 API。
- v1.1.3 ZIP 与源目录逐字节一致，共 24 个文件；路径安全、重复项、注释、符号链接和 CRC 检查均通过；从 ZIP 解压后再次完成 Skill 校验、初始化和结构验证。
- v1.1.3 ZIP SHA-256：`53f613e7768c11ee58e5bbfdd6dae0cb914d95ad7f2be841d7c519ff7ee970c2`。
- 创建并推送提交 `cc345c3f8b1a1fbbad5068e3ae9d014158958426`（`docs: add universal agent install`）到公开仓库 `main`。
- GitHub 元数据复核为公开仓库、默认分支 `main`、MIT；从远端全新克隆后确认共 31 个公开文件、工作树干净，Plugin/Skill 校验、版本、安装命令和隐私说明均正确。
- 关闭遥测后从 GitHub 运行 `skills` CLI，成功发现唯一的 `manage-external-memory`；在临时项目中执行非全局安装成功，安装结果与远端 Skill 逐文件一致，并再次完成初始化和结构验证。

### 2026-07-17 公开任务与决策记录

- 用户明确要求把脱敏后的 `TASK.md` 和 `DECISIONS.md` 加入现有公开仓库 `Caponia/external-memory-tools`。
- 两份文档中的用户代称统一为“用户”，真实本机路径改为通用描述。
- 发布范围只增加这两份记录，不包含其他父项目文件、真实记忆、工作区、候选内容或导出文件。
- 发布前重新检查独立代称、真实路径、高置信凭据、邮箱、IP、手机号和敏感文件名。
