# 项目工件与状态维护

在创建、恢复、更新或交接申请项目时读取本文件。五份工件属于当前用户的申请项目，不是放在 skill 包里的静态模板。

## 通用维护规则

- 使用用户指定目录；未指定而当前 workspace 明确属于该申请任务时，使用该 workspace。目标位置仍不明确时，先问一个路径/项目选择问题，不要散落文件。
- 工件写入必须服从当前请求的权限。用户要求建立、重建或继续推进完整文书项目时可以维护；只要求解释、审计、评议、状态报告或明确要求只读时，不创建、不更新、不删除，只给出拟议变更。
- 先读后写。保留用户已有事实、来源和决策记录；冲突项并列记录，不能静默用新说法覆盖旧说法。
- 每次处理用户回答、材料、官方页面、路线选择、readiness 判断或草稿修订后，更新受影响工件再继续。
- 时间使用明确日期；项目和申请周期分别记录。多个学校使用独立目录或严格分区，禁止跨项目复用未经重新核验的 prompt 与 fit 事实。
- 未知值写 `null`、`unknown` 或“待核实”，不得用看似合理的值填空。
- 用户陈述可以成为可用事实，但必须标为 `user_confirmed` 或 `user_stated_unverified`；不要冒充文件核验。
- 在状态文件中维护 `source_scope`：允许读取、仅供事实核对、明确排除的来源分别记录。成型 PS/CV 默认不是申请人动机或措辞的权威来源；用户要求忽略时不得读取或借用。
- `answer_status` 与 `verification_status` 是两条轴：前者描述用户回答的状态，后者描述外部证据强度，不得混用。
- 一个 claim 只保存一个原子主张和一个 `answer_status`。同一回答同时包含“参数忘记、无日志、未参与、不要写”等状态时，拆成多个 claim 或明确的项目子项，不把多个状态压进一个字段。用 `evidence_availability` 单独记录日志、文件或测量证据是否存在，不能把“用户确认没有日志”误写成性能主张已获验证。
- 若误读了排除来源，立即记录 `source_contamination`，隔离该来源产生的措辞、动机、因果和问题 framing；从活动大纲/草稿中移除派生内容，再只用允许来源重建。若承重内容受影响，先失效旧大纲与旧稿，只重建一个未批准的新大纲；取得该版本的明确批准后，才生成新英文稿。在 `artifact_versions` 记录失效版本与当前活动版本；旧污染文件保留为隔离审计记录，不得继续使用，也不得在未获用户授权时删除。保留污染事实供审计，但不得保留被禁用文本本身作为可用素材。

## `PS_PROJECT_STATE.md`

这是恢复会话与控制阶段的唯一状态入口，至少维护：

- 项目标识：申请人使用的项目别名、学校、项目、学位、周期；未知项明确标记。
- 当前阶段：`intake / official-source-audit / evidence-mapping / schema-interview / claim-calibration / readiness-review / outline-review / drafting / qa / delivered / early-exit`。
- 最近更新：日期、吸收了哪些材料或回答、改动了哪些工件。
- 已确认决策：目标、优先主张、叙述边界、禁用材料、语言与交付格式。
- 来源范围：`allowed_sources / fact_check_only_sources / excluded_sources`，以及用户是否允许读取成型 PS/CV。
- 开放项：按五维归类，标注影响和下一动作。
- 质询状态：上一问、用户回答摘要、下一项最高优先级缺口；不要保存推测为事实。
- 顺序状态：当前模式、`section_cursor`、当前子项、已完成/跳过栏目和下一项；顺序保持模式不能丢失 cursor。
- 大纲与草稿状态：证据 gate、中文大纲位置与版本、`outline_approved`、批准时间、草稿位置、是否存在 user override。
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
schema_version: "0.2"
target_id: null
updated: null
source_scope:
  allowed_sources: []
  fact_check_only_sources: []
  excluded_sources: []
  allow_completed_ps_cv: false
  source_contamination:
    # - id: SC01
    #   source: null
    #   accessed_at: null
    #   affected_artifacts: []
    #   remediation_status: null # detected | isolated | rebuilt | reapproved
artifact_versions:
  outline:
    active_version: null
    invalidated_versions: []
  draft:
    active_version: null
    invalidated_versions: []
interview:
  mode: adaptive # adaptive | order-preserving
  schema_sections: []
  section_cursor: null
outline:
  path: PS_CHINESE_OUTLINE.md
  version: null
  outline_approved: false
  approved_at: null
claims:
  - id: E01
    proposed_claim: null
    relevance_to_prompt: null
    answer_status: null # confirmed | tentative | unknown | forgotten | none | not_involved | excluded_by_user | do_not_disclose | conflicting
    source:
      kind: null # document | official_public_source | user_confirmed | user_stated_unverified
      locator: null # file/page/section or dated conversation turn
    evidence_availability: unknown # available | absent_confirmed | not_provided | inaccessible | unknown | not_applicable
    context: null
    personal_action: null
    method_or_choice: null
    core_source: null # applicant_original | team | public_example | tutorial | external_method | unknown | not_applicable
    modification_scope: null # none | dependency_compatibility | parameters | component_integration | system_design | core_method | unknown | not_applicable
    validation_stage: null # not_run | simulation | bench_qualitative | bench_quantitative_uncontrolled | controlled_quantitative | integrated_platform | field_deployment | unknown | not_applicable
    team_outcome: null
    personal_outcome: null
    quantitative_claims: []
    metric_scope:
      metric_name: null
      measured_property: null
      baseline: null
      conditions: null
      ownership: null # personal_test | team_test | cited_result | unknown
    capability_supported: null
    trajectory_link: null
    future_contribution: null
    claim_ceiling: null
    allowed_verbs: []
    unsupported_claims: []
    release_status: null # supported | bounded | future-only | exclude
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

`evidence_availability` 只描述支撑材料能否取得：例如用户明确确认从未保留日志时写 `absent_confirmed`，但相关性能主张仍保持 `verification_status: unverified`，数字、比较和因果不得由“没有日志”反向获得支持。

数字需逐项保留来源与口径。团队成果写在 `team_outcome`，用户个人动作或产物写在 `personal_outcome`；除非材料支持，不得把前者移到后者。

`answer_status` 使用质询协议中的九个状态；`not_involved / excluded_by_user / do_not_disclose` 不得在后续自动升级。`release_status` 决定主张怎样进入大纲：

- `supported`：当前强度有证据支持，可进入大纲。
- `bounded`：只有降级后的有限说法可进入，必须保留 `claim_ceiling` 与禁用主张。
- `future-only`：只能作为学习或研究目标，不能写成已有能力或成果。
- `exclude`：不进入大纲或正式稿；保留原因供审计。

## `PS_CHINESE_OUTLINE.md`

这是申请人确认内容所有权的必经工件，不是可跳过的临时提纲。至少维护：

- 项目、prompt、字数与大纲版本。
- 来源范围：允许、仅事实核对和明确排除的材料。
- 按用户 schema 或最终论证顺序列出的栏目；两种顺序不同时同时记录映射。
- 每栏的已确认事实、拟用有限主张、证据等级、个人/团队归因、未来连接和 paragraph role。
- `bounded / future-only / exclude` 项、禁用表述、冲突、披露边界和待核实风险。
- readiness 分数与 `user_override`（如有）。
- 审批区：`outline_version / outline_approved / approved_at / approval_locator`。

只有用户对具体版本作出明确同意，才能把 `outline_approved` 设为 `true`。修改承重事实、动机、因果、职业目标、programme fit 或禁用边界后必须增加版本并重新确认；纯格式和不改变含义的语言修订不必重开内容审批，但要记录。

## `PS_QA_REPORT.md`

这是门禁与交付风险记录，至少维护五部分：

1. **Source audit**：读过的用户材料、当前官方页面、核验日期、无法访问或过时项。
2. **Readiness and outline report**：五维分数、逐项理由、算术平均值、门禁决定、是否 user override，以及已批准大纲版本和批准定位。
3. **Draft QA**：prompt 覆盖、事实与数字、claim ceiling、本人/团队归因、轨迹、fit、隐私、段落主张、术语和可读性。
4. **Format and render QA**：官方格式来源、工作格式声明、编译器与结果、页数、溢出、字体、边距、断页、文件大小及视觉检查；未执行的项目明确写未执行。
5. **Release status**：`hold / outline-awaiting-approval / draft-with-risk / ready-for-user-review`，遗留风险、需要用户最终确认的内容、对应大纲与稿件版本。

每个结论写证据或定位，不使用无依据的“全部通过”。正式稿修订后重新运行相关 QA；旧报告可保留为有日期的历史，不得伪造测试、审核或录取结果。

## 一致性检查

交付前执行：

- `PS_PROJECT_STATE.md` 的目标与 `PS_REQUIREMENTS.md` 一致。
- `source_scope` 与实际读取材料一致；被排除的成型 PS/CV 没有贡献措辞、动机或因果。
- 若存在 `source_contamination`，污染内容已从活动工件隔离，受影响版本已写入 `invalidated_versions`。等待审批期间，outline 的 `active_version` 可以指向只用允许来源重建但尚未批准的新版本，发布状态必须为 `outline-awaiting-approval`，draft 的 `active_version` 必须为 `null`；只有大纲获批后才可生成并激活新英文稿。旧文件没有被擅自删除，审计记录也没有被误当作可用来源。
- 正文每个承重主张都能回指 `PS_EVIDENCE_MAP.yaml`。
- 正文只使用已批准 `PS_CHINESE_OUTLINE.md` 中的内容；批准版本、时间和定位可回查。
- `PS_QA_REPORT.md` 的分数理由与工件当前状态一致，平均值计算正确。
- 被标为 `do_not_disclose`、`conflicting` 或 `unverified` 的内容没有偷偷进入正式稿。
- `not_involved / excluded_by_user / exclude` 没有重新进入大纲或正文；`future-only` 没有写成既有成果。
- `claim_ceiling`、允许动词、验证阶段和指标口径与正文措辞一致；团队结果没有个人化。
- fit URL、项目周期和教师/课程事实没有跨目标污染。
- 状态文件所指的大纲、稿件与排版版本确实存在；没有把未过门或未视觉核验的稿件标成 submission-ready。
