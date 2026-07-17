# Codex 协作入口

1. 开始任务前完整阅读 `{{MEMORY_PATH}}/README.md`，并按其顺序读取与当前任务有关的记忆。
2. 长期记忆默认只读；只有用户明确授权“写入 INBOX”后，才可在候选区创建独立文件。
3. 合并主记忆需要再次获得明确批准，并同步更新 `CHANGELOG.md`。
4. 不读取、复述或写入密码、Token、API Key、Cookie、SSH 私钥、`.env`、`.dev.vars` 等敏感内容。
5. 不擅自覆盖、删除、上传、Git commit 或 push。

具体项目中更近层级的 `AGENTS.md` 在其作用域内优先；当前对话中用户的明确要求优先于长期记忆。
