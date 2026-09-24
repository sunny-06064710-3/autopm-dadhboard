# 文档索引

从[项目首页](../README.md)开始；任务状态只读原GitHub Issue。旧资料不覆盖新决定。

| 层级 | 入口 | 使用方法 |
|---|---|---|
| 交付导航 | [行动页](delivery/README.md)、[问题路由](delivery/issues.md)、[发现清单](delivery/findings.md)、[架构说明](delivery/architecture.md) | 行动页为本期状态快照；当前进度仍读原Issue |
| 审计基线 | [9/23覆盖与证据](delivery/evidence.md) | 历史事实与未验范围，不是实时监控 |
| 协作规则 | [根规则](../AGENTS.md)、[协作入口](../collaboration/README.md) | 唯一规则及任务链接 |
| 近期实施证据 | [9/21自动化进展](../collaboration/current/airtable-automation-progress-2026-09-21.md)、[市场脚本](../collaboration/current/program-markets/IMPLEMENTATION-STATUS.md)、[界面交接](../collaboration/current/interface-handoff.md) | 按原日期和验收边界使用 |
| 待审迁移 | [微软资料](../collaboration/current/microsoft/README.md)及[PR导航](../collaboration/README.md) | 输入保留，未部署不冒称完成 |
| 历史参考 | [9/13评估](../collaboration/review-2026-09-13/README.md)、[9/11规划](../collaboration/planning/README.md)、[更早归档](archive/README.md) | 按需查，不默认全读入AI |
| 来源与清理 | [旧引用缺口](DEPENDENCIES.md)、[本次清理](delivery/cleanup.md) | 缺失、删除及恢复依据 |

不再建立另一份总台账或最新入口。新增成果回原Issue和对应日期批次，本页只补必要导航。

## 仓库与发布边界

- `backend/` 及其 `frontend/` 是现有演示源码，`render.yaml` 指向 backend；源码存在不证明生产部署、Airtable 或 Power Apps 已验收。
- `frontend/`、`backend/static/` 和版本页面用途仍需按实际消费者核对，不能只凭目录名清理。
- `collaboration/current/` 与各 AI 的 inbox/outbox 保留输入和交付；planning、issues、archive 保留历史证据，当前状态读原 Issue。
- 其他未合并 PR 独立审查与验收；PR #44 合并前，main 仍可能是旧入口。
