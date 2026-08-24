# 项目工件与状态维护

在创建、恢复、更新或交接申请项目时读取本文件。四份工件属于当前用户的申请项目，不是放在 skill 包里的静态模板。

## 通用维护规则

- 使用用户指定目录；未指定而当前 workspace 明确属于该申请任务时，使用该 workspace。目标位置仍不明确时，先问一个路径/项目选择问题，不要散落文件。
- 先读后写。保留用户已有事实、来源和决策记录；冲突项并列记录，不能静默用新说法覆盖旧说法。
- 每次处理用户回答、材料、官方页面、路线选择、readiness 判断或草稿修订后，更新受影响工件再继续。
- 时间使用明确日期；项目和申请周期分别记录。多个学校使用独立目录或严格分区，禁止跨项目复用未经重新核验的 prompt 与 fit 事实。
- 未知值写 `null`、`unknown` 或“待核实”，不得用看似合理的值填空。
- 用户陈述可以成为可用事实，但必须标为 `user_confirmed` 或 `user_stated_unverified`；不要冒充文件核验。

## `PS_PROJECT_STATE.md`

这是恢复会话与控制阶段的唯一状态入口，至少维护：

- 项目标识：申请人使用的项目别名、学校、项目、学位、周期；未知项明确标记。
- 当前阶段：`intake / official-source-audit / evidence-mapping / grilling / readiness-review / drafting / qa / delivered / early-exit`。
- 最近更新：日期、吸收了哪些材料或回答、改动了哪些工件。
- 已确认决策：目标、优先主张、叙述边界、禁用材料、语言与交付格式。
- 开放项：按五维归类，标注影响和下一动作。
- 质询状态：上一问、用户回答摘要、下一项最高优先级缺口；不要保存推测为事实。
- 草稿状态：文件位置或版本、是否过 gate、是否存在 user override。
- 下一步：一个明确动作，而不是笼统“继续完善”。

恢复任务时先以本文件定位阶段，再到其他工件核实，不能只信状态摘要。

## `PS_REQUIREMENTS.md`

这是目标任务的官方约束账本，至少维护：

- 目标项目、学位、申请周期和官方页面核验日期。
- 官方 prompt 原文或准确摘录及直接 URL；若用户提供截图/文件，记录来源位置。
- 字数、字符、页数、文件格式、语言、截止周期等硬约束。
- 必答问题、明确要求或禁止的内容、额外 short answers 与它们和主文书的分工。
- 从官方文本可合理推出的评价任务；把“原文事实”和“解释”分栏。
- 用户偏好与官方要求分开记录。
- 冲突、过时页面、无法访问页面与待核实项。

第三方博客、论坛、排名或往年范文只能提供检索线索。当前官方要求与通用写作建议冲突时，以当前官方要求为准。

## `PS_EVIDENCE_MAP.yaml`

保持为可解析 YAML。可按以下字段扩展，但不能删除 provenance、归因和状态信息：

```yaml
schema_version: "0.1"
target_id: null
updated: null
claims:
  - id: E01
    proposed_claim: null
    relevance_to_prompt: null
    source:
      kind: null # document | user_confirmed | user_stated_unverified
      locator: null # file/page/section or dated conversation turn
    context: null
    personal_action: null
    method_or_choice: null
    team_outcome: null
    personal_outcome: null
    quantitative_claims: []
    capability_supported: null
    trajectory_link: null
    future_contribution: null
    attribution_status: unresolved # bounded | unresolved | conflicting
    verification_status: unresolved # verified | user_confirmed | unverified | conflicting
    sensitivity: ordinary # ordinary | sensitive | do_not_disclose
    allowed_use: null
    open_questions: []
fit_resources:
  - id: F01
    official_url: null
    page_title: null
    application_cycle: null
    verified_on: null
    mechanism: null
    applicant_use: null
    evidence_backed_contribution: null
    status: unresolved
conflicts: []
excluded_materials: []
```

### 证据状态规则

- `verified`：文件或可核验来源直接支持，locator 足以回查。
- `user_confirmed`：用户明确确认个人事实；这不等于第三方独立认证，但可以在其申请材料中使用。
- `unverified`：只有模糊旧稿、推测或未确认来源，不能写成确定事实。
- `conflicting`：两个来源不一致；正式起草前须解决或排除该主张。

数字需逐项保留来源与口径。团队成果写在 `team_outcome`，用户个人动作或产物写在 `personal_outcome`；除非材料支持，不得把前者移到后者。

## `PS_QA_REPORT.md`

这是门禁与交付风险记录，至少维护四部分：

1. **Source audit**：读过的用户材料、当前官方页面、核验日期、无法访问或过时项。
2. **Readiness report**：五维分数、逐项理由、算术平均值、门禁决定、是否 user override。
3. **Draft QA**：prompt 覆盖、事实与数字、本人/团队归因、轨迹、fit、隐私、段落主张、术语和可读性。
4. **Release status**：`hold / draft-with-risk / ready-for-user-review`，遗留风险、需要用户最终确认的内容、对应稿件版本。

每个结论写证据或定位，不使用无依据的“全部通过”。正式稿修订后重新运行相关 QA；旧报告可保留为有日期的历史，不得伪造测试、审核或录取结果。

## 一致性检查

交付前执行：

- `PS_PROJECT_STATE.md` 的目标与 `PS_REQUIREMENTS.md` 一致。
- 正文每个承重主张都能回指 `PS_EVIDENCE_MAP.yaml`。
- `PS_QA_REPORT.md` 的分数理由与工件当前状态一致，平均值计算正确。
- 被标为 `do_not_disclose`、`conflicting` 或 `unverified` 的内容没有偷偷进入正式稿。
- fit URL、项目周期和教师/课程事实没有跨目标污染。
- 状态文件所指的稿件版本确实存在；没有把未过门稿标成 submission-ready。
