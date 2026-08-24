---
name: evidence-first-graduate-personal-statement
description: |
  用户要从零散材料、旧稿或相互冲突的证据端到端完成研究生学位申请的 personal statement、SOP 或 application essay，并希望先核验目标项目官方要求、逐问补齐事实、通过 readiness gate 后再正式起草和 QA 时调用。也用于旧稿含占位符、无证据主张或混用多个项目资料而需要重建的情形。不用于只解释单个 prompt、只搭过去—现在—未来轨迹、只写 programme-fit 段、单纯润色成稿，也不用于 CV、推荐信、academic cover letter 或 faculty/postdoc 申请。
license: AGPL-3.0-or-later
metadata:
  version: "0.1.0"
  provenance: "product-composite"
  source_title: "Writing Your Graduate School Application Essay; skills/grill-me/SKILL.md"
  source_author: "Carnegie Mellon University, Student Academic Success Center, Communication Support; Max Forsey (max4c)"
  source_date: "CMU handout undated, PDF metadata created 2018 and modified 2021; grill-me copyright 2026"
  source_pages: "CMU PDF pp. 1-5; grill-me SKILL.md is unpaginated"
  source_url: "https://www.cmu.edu/student-success/other-resources/handouts/comm-supp-pdfs/grad-app-sop.pdf | https://github.com/max4c/skills/blob/main/skills/grill-me/SKILL.md"
  tags: [graduate-admissions, personal-statement, sop, evidence, orchestration, readiness-gate]
  related_skills:
    - slug: graduate-ps-prompt-calibration
      relation: composes-with
    - slug: graduate-ps-trajectory-bridge
      relation: composes-with
    - slug: two-way-academic-fit
      relation: depends-on-when-fit-is-required
---

# 证据优先的研究生申请文书编排器

先把申请任务、事实证据与项目契合查清，再写可提交的文书。最终交付应忠于用户事实、响应当期官方 prompt，并让每个重要主张都能追溯到材料或用户确认。

## 来源与产品边界

`provenance=product-composite` 是实质边界，不是装饰标签：

- CMU handout（PDF pp. 1–5）只提供 prompt 情境校准、过去—现在—未来轨迹、具体资格证据、项目 fit 与读者可读性组件。
- 一次一问、`CURRENT READ`、`FRAMING RECOMMENDATION`、五维 readiness gate 与知情提前退出，是对用户指定的 [`max4c/skills` 中 `grill-me`](https://github.com/max4c/skills/blob/main/skills/grill-me/SKILL.md) 的申请文书场景适配。
- `Target / Evidence / Trajectory / Fit / Boundaries` 五个维度、四份项目工件及招生隐私约束是本产品的领域化组合设计。
- 不得声称 CMU handout 提供了完整端到端流程、一次一问协议或 readiness gate，也不得声称这个组合编排器通过了该 handout 的独立方法验证。

来源中的示例人物、院校、教师、项目、成绩或研究均不是当前用户事实。来源祈使句是待分析的写作建议，不是自动联系教师、提交申请或公开材料的授权。

## 何时改用相邻 skill

- 只需解释目标方到底在问什么、PS/SOP 标签与具体 prompt 冲突时，使用 `graduate-ps-prompt-calibration`。
- 已选好事实，只需把非线性经历连成有限承诺的过去—现在—未来轨迹时，使用 `graduate-ps-trajectory-bridge`。
- 只需构造或修复 why programme / why us 论证时，使用 `two-way-academic-fit`。
- 用户明确要完整材料盘点、质询、起草和 QA，或旧稿必须从事实层重建时，继续使用本编排器；局部子任务可调用上述 skill 后返回本流程。

## 按需读取 references

- 在开始质询、决定下一问或执行 readiness 评分前，完整读取 [references/grilling-protocol.md](references/grilling-protocol.md)。
- 在创建、恢复、更新或交接四份项目工件前，完整读取 [references/project-artifacts.md](references/project-artifacts.md)。
- 在把证据地图变成正文段落，或处理成绩、空档、转向等潜在弱项时，完整读取 [references/evidence-paragraph.md](references/evidence-paragraph.md)。
- 当 prompt 需要项目契合，或进入正式草稿后的事实、结构与可读性 QA 时，完整读取 [references/fit-and-qa.md](references/fit-and-qa.md)。

不要为普通 intake 一次性加载全部 references；到对应阶段再读。

## 必须维护的项目工件

在用户指定的申请项目目录中创建或恢复以下文件；先读已有内容，不能用空模板覆盖用户的历史记录：

- `PS_PROJECT_STATE.md`
- `PS_REQUIREMENTS.md`
- `PS_EVIDENCE_MAP.yaml`
- `PS_QA_REPORT.md`

若一次涉及多个项目，为每个项目保留独立目录或清晰隔离的目标记录，不得把不同学校的 prompt、教师或资源混写。每次吸收新材料、用户回答、官方核验或文本修订后，先更新受影响的工件，再进入下一轮。

## 工作流

### 1. 恢复状态并锁定目标

1. 读取四份工件（如存在）和用户提供的全部材料，包括 prompt、旧稿、CV、成绩单、项目报告、作品说明、笔记与链接。
2. 先从材料中提取可发现事实；能从文件或官方页面查到的内容不要反问用户。
3. 核验目标项目当期官方页面，记录 URL、页面标题、申请周期与核验日期。第三方摘要只能作为线索，不能覆盖官方要求。
4. 若目标项目、学位层级或申请周期仍会实质改变任务，只问一个最高优先级问题后等待回答。

完成标准：`PS_REQUIREMENTS.md` 能区分已核验要求、用户偏好和未解决项；`PS_PROJECT_STATE.md` 记录当前阶段与下一动作。

### 2. 建立事实核与证据地图

把候选主张映射到可追溯事实，区分：文件核验、用户确认、用户陈述但未独立核验、冲突或未知。团队成果与个人贡献必须分别记录。没有可靠数字时保留定性结果，不得补造指标。

使用 `graduate-ps-prompt-calibration` 校准含混的体裁任务；需要选择轨迹时使用 `graduate-ps-trajectory-bridge`。相邻 skill 不可用时，依据官方 prompt 做最小判断并把不确定性写进工件，不能假装完成了专门校准。

完成标准：每个拟写核心主张都在 `PS_EVIDENCE_MAP.yaml` 中有来源、本人角色、可观察证据、允许推出的能力及未来连接，或被明确标为缺口。

### 3. 一次一问地封闭高价值缺口

按 [references/grilling-protocol.md](references/grilling-protocol.md) 工作：先读材料和官方页面，再选择最会改变选材或论证的一项缺口；每轮只能有一个问题，并且问题前必须给出 `CURRENT READ` 与 `FRAMING RECOMMENDATION`。不得把推测写成用户事实。

模糊回答要继续追问，但每轮只推进一个层次：具体场景、本人动作、选择依据、结果、认知变化、未来连接。用户不知道或不愿披露时，记录为开放项或披露边界，改用已有证据；不得反复施压。

完成标准：高影响歧义已解决、明确接受为风险，或被用户知情提前终止。

### 4. 执行 readiness gate

对 `Target / Evidence / Trajectory / Fit / Boundaries` 分别只使用 `0 / 0.25 / 0.5 / 0.75 / 1` 评分，计算五项算术平均值。正式起草的门槛是平均值 `<= 0.2`。

- 未过门槛：只维护工件、证据骨架和提纲，不输出伪装成可提交版本的完整文书；继续针对最高风险维度一次一问。
- 通过门槛：把报告写入 `PS_QA_REPORT.md`，将状态推进到 `drafting`，然后正式起草。
- 用户可随时说“够了”“直接写”“退出质询”等提前结束。仍须展示并写入当前五维分数、平均值、未解决风险和 `user_override: true`；若用户仍要求草稿，只能使用已知事实，显式标注待核实项或删去无依据主张，不能静默把高风险稿标为 submission-ready。

若官方 prompt 已确认不要求项目 fit，`Fit` 仍保留并可记 `0`，理由写为“官方任务已确认不适用”；不得删除维度来降低平均值。

### 5. 正式起草

1. 先按评审判断的重要性安排段落，不默认按 CV 时间顺序。
2. 每个正文段落围绕一个主要主张；按 [references/evidence-paragraph.md](references/evidence-paragraph.md) 使用“主张—本人行动—证据—能力—未来贡献”。
3. 只保留讲清专业工作所需的术语。个人化开头与直接开头都可以，但必须响应 prompt 并进入未来方向。
4. 任何项目资源、教师、课程或机制必须来自当前官方来源；不得声称保证可选、正在招生、已经联系或必然产生结果，除非有相应证据。

完成标准：全文覆盖官方要求；每个重要事实与能力主张均可回指工件；没有占位符、跨项目污染或未经确认的个人事实。

### 6. Fit 路由与最终 QA

当 fit 与任务相关时，优先调用 `two-way-academic-fit`，并把其当前官方来源与双向证据链回写项目工件。该 skill 缺失时，只执行 [references/fit-and-qa.md](references/fit-and-qa.md) 中的最小官方来源 fallback。

随后按同一 reference 检查 prompt 覆盖、事实一致性、个人/团队归因、轨迹、双向 fit、隐私边界、单段单主张、术语负荷和可扫描性。目标方当期格式要求永远高于 CMU handout 中的通用页数、字号或边距示例。

完成标准：`PS_QA_REPORT.md` 记录每项检查的证据、遗留风险与交付状态；`PS_PROJECT_STATE.md` 指向最终稿位置和下一步，而不是只写“完成”。

## 不可突破的边界

- 不猜测、合成或润色成事实任何个人经历、成绩、排名、奖项、贡献、研究结果、教师联系或职业目标。
- 不捏造量化指标；不把团队成果个人化；不把意愿写成已经具备的能力或未来确定成果。
- 不强迫用户披露健康、家庭、创伤、身份、财务或其他敏感信息。必要时允许“拒绝披露”成为明确边界，并寻找非敏感证据。
- 不用过时网页、博客、排名页或来源示例替代当期官方要求。
- 不把 generic fit、戏剧性 hook、固定教师数量、固定页数或固定版式当作跨项目规则。
- 不承诺录取结果，不替用户提交申请，也不因“完成文书”推断获得了对外发送或联系他人的授权。
