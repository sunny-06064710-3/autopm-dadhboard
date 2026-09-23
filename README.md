# AutoPM · 唯一交付与协作入口

**业务负责人先看：[接下来做什么、谁来做、做到什么算完成](docs/delivery/README.md)。**

2026-09-23审计已完成；数据、自动化和界面存在待处理问题，普通用户全路径验收尚未完成。当前交付物是审计和整改依据，不能当作零缺陷上线证明。当前状态和批准范围统一读[总协调 Issue #1](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/1)。

| 我现在要做什么 | 去哪里 |
|---|---|
| 看重点、决定首批范围 | [交付行动页：6个工作包](docs/delivery/README.md) |
| 查问题、修复和验收办法 | [审计发现与受限证据索引](docs/delivery/findings.md) |
| 理解系统及接手维护 | [架构、数据流与使用说明](docs/delivery/architecture.md) |
| 查已检查/没检查的范围和底稿 | [审计证据与复用边界](docs/delivery/evidence.md) |
| 让AI领取或交回工作 | [统一规则](AGENTS.md) → [协作入口](collaboration/README.md) → 原Issue |
| 查代码变更、待审交付 | [Pull requests](https://github.com/sunny-06064710-3/autopm-dadhboard/pulls) |
| 查旧资料及本次清理 | [文档索引](docs/README.md) / [清理记录](docs/delivery/cleanup.md) |

## 以后只按这个方式维护

**首页导航；Issue管当前任务状态；PR管变更和审查；带日期的证据管验收。** 本地指南、历史任务卡、聊天记录不再维护第二套状态。完成一个阶段时回写原Issue，更新这里链接的现有文档，不再新建另一个“总入口”。

修复只复读受影响对象及下游，复用审计规则；正式上线前仍全量程序回归。历史计数不是实时数据。提交或合并成功不能自动标记业务完成。

## 仓库边界

- `backend/`及其`frontend/`为现有演示源码，`render.yaml`指向backend；源码存在不证明部署、Airtable或Power Apps已验收。
- `frontend/`、`backend/static/`和版本页面用途尚待确认，本次保留，不作为默认修改入口。
- `collaboration/current/`及各AI的`inbox/outbox`保留输入与交付；`planning/`、`issues/`是历史快照，状态只读Issue。
- 仓库当前公开。本次审计摘要不含原始业务记录；完整包见[受限证据说明](docs/delivery/evidence.md)。删除当前文件不会删除Git历史，本次没有完成历史隐私清除。

**发布过渡：** 本首页随[PR #44](https://github.com/sunny-06064710-3/autopm-dadhboard/pull/44)更新，合并前用该PR的Files changed查看，main可能仍显示旧说明。合并后仓库默认首页即日常唯一入口。其他未合并PR仍需独立验收。
