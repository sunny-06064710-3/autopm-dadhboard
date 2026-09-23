# 协作入口

项目唯一入口为[根首页](../README.md)。本页只维护约定和导航；当前状态读[总协调#1](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/1)及原Issue，完整规则仅维护[根AGENTS](../AGENTS.md)。

## 从哪里接续

- Airtable交付：[行动页](../docs/delivery/README.md) → [#50治理](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/50)及对应原Issue。发现问题没有自动授权修复。
- 角色分工：[使用分工指南](使用分工指南.md)。Codex管理审核和集成，用户不做消息中转。
- 旧任务编号：[导航映射](issue-map.json)。body_file仅指历史草稿，不是当前Issue正文。
- 交付：team/角色/outbox/任务ID/result.md，沿用[模板](planning/templates/DELIVERY.md)，回链原Issue及PR。

## 仍有效的约定

1. Tasks承载计划；业务Issues及措施承载异常；GitHub Issues承载开发，三者不自动复制。
2. 保留现有Task完成机制，旧进度改造#4仍暂停；修复当前结果与改变业务口径须分开确认。
3. 业务规则维护在配置表；缺Owner只警告不阻止创建；重跑补缺并保护人工值。日期/Owner规则沿用原Issue最新批准约定。
4. P01与L系列沿用原Issue专属维护责任，不能多AI争写同一对象。
5. Power Apps目标为业务功能等效；MVP/方案不证明租户、许可、Dataverse、部署和访问已验收，不能自行替换Airtable生产。
6. 旧文件均按取证日期理解，新事实需要新证据。角色标签、Ready、任务卡不等于AI已启动；没有已验证的自动唤醒连接。

## 保留的待审工作

下表仅导航，实时状态读PR；本次整理不接受其业务结果。

| 工作 | 入口 | 边界 |
|---|---|---|
| 统一管理与交付入口 | [PR #44](https://github.com/sunny-06064710-3/autopm-dadhboard/pull/44) | 合并前用管理分支文档；合并后main为正式入口 |
| Qoder接入 | [#42](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/42) / [PR #45](https://github.com/sunny-06064710-3/autopm-dadhboard/pull/45) | 保留输入及回执，不代验收 |
| 微软环境与Bridge契约 | [PR #46](https://github.com/sunny-06064710-3/autopm-dadhboard/pull/46) / [PR #47](https://github.com/sunny-06064710-3/autopm-dadhboard/pull/47) | 保留current/microsoft与派工；基线变化后同步并重验 |
| 本地演示 | [PR #49](https://github.com/sunny-06064710-3/autopm-dadhboard/pull/49) | 演示不是生产交付 |
| 导入保护与使用说明 | [PR #51](https://github.com/sunny-06064710-3/autopm-dadhboard/pull/51) | 依赖独立importer分支，未并入本次变更 |
