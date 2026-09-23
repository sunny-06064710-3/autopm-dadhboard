# AutoPM 交付行动页

这里解释下一步；当前执行状态只在原GitHub Issue维护。本次已整理审计材料，尚不构成生产修复或正式验收。公开版遵守原[#50](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/50)的脱敏边界；完整报告、对象映射与明细由维护者受限保管。

## 你做什么，AI做什么

你负责确认首批给谁用、哪些功能必须交付、有歧义的业务规则，以及参加真实使用验收。AI负责定位、修改方案、影响预览、实施、回读、回退与资料维护；Codex汇总审核，你不需要替不同AI搬运消息。已有规则直接沿用，只有新冲突才需决定。

## 六个工作包，沿用原任务

以下为工作归并，不表示新派工、恢复暂停任务或已完成修复。具体问题及优先级见受限报告。

| 包 | 目标 | 做到什么算完成 | 原任务入口 |
|---|---|---|---|
| W1 | 项目概况数字可信 | 明细、统计、图表一致，增删移动后仍正确 | [#50](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/50)；[#4](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/4)暂停范围不自动恢复 |
| W2 | 创建、导入、身份和编号可靠 | 重复操作不误建、不误覆盖、不认错人，失败可追踪 | [#50](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/50)、[#9](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/9)、[#36](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/36) |
| W3 | 日期有可靠来源 | 继承和人工例外按批准规则，异常值有来源依据 | [#50](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/50)、[#7](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/7) |
| W4 | 入口好找、可用、权限正确 | 普通用户完成创建、更新、返回；系统结果和用户输入分清 | [#5](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/5)、[#11](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/11)、[#33](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/33) |
| W5 | 通知范围和可靠性明确 | 首批需要则获准测试收件人验收；暂缓则入口和承诺同步退出 | [#12](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/12)、[#50](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/50) |
| W6 | 真实角色完整走一次 | 核心操作、结果、权限及发布后导航可验证 | [#14](https://github.com/sunny-06064710-3/autopm-dadhboard/issues/14) |

建议先由Codex在原Issue明确W1范围；W4可准备真实角色验收。共享字段与配置只设一个主执行者，其余AI提供输入，不同时争写。首批需要的功能不能仅在文档写“暂缓”就跳过验收。

## 结果必须分四类

已发生错误、已确认逻辑风险、待业务决定、未完成验收分别记录；不能把本地反例当生产事故，也不能把未测试当通过。具体发现编号和证据已保留在完整底稿，公开版不复述内部细节。

本次交付方式的改进是：先给业务行动页，再由AI查技术证据。以后不把字段ID和脚本清单作为负责人第一层阅读材料。

## 后续如何复用

1. 从[首页](../../README.md)读[规则](../../AGENTS.md)、原Issue及最新评论，确认范围与执行者。
2. 在获准渠道取得所需原始发现及对象映射，只复读本次对象、数据和下游；历史计数不当实时状态。
3. 新证据另存日期批次，不覆盖旧快照；同一问题继续原Issue，变更走PR。
4. 每次只补五项：做了什么、谁负责、实际结果、还差什么、证据与版本。运行成功或PR合并不等于业务验收。
5. 正式上线前、大规模导入或影响范围不明时全量程序回归；平常程序查差异，AI读异常，避免重读整库。

具体审计内容索引见[发现与证据交接](findings.md)，接手原则见[架构说明](architecture.md)，归档完整性见[证据说明](evidence.md)。本页没有启动自动巡检或新派工。
