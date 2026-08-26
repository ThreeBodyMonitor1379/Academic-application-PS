---
name: evidence-first-graduate-personal-statement
description: |
  用户要从零散材料、研究或成绩证明、旧稿或相互冲突的证据端到端完成研究生 personal statement、SOP 或 application essay 时调用；尤其适用于要求按自定义表格顺序、一次一问、不能替申请人回答，先确认中文证据大纲，再起草英文稿并按需交付 LaTeX/PDF 的任务。也用于旧稿含占位符、无证据主张或跨项目污染而需从事实层重建的情形。不用于只解释单个 prompt、只搭经历轨迹、只写 programme-fit 段、单纯润色成稿、改写 CV bullet、纯技术教学，也不用于推荐信、academic cover letter 或 faculty/postdoc 申请。
license: AGPL-3.0-or-later
metadata:
  version: "0.2.0"
  provenance: "product-composite+user-conversation-derived"
  source_title: "Writing Your Graduate School Application Essay; skills/grill-me/SKILL.md; observable graduate admissions interview decisions"
  source_author: "Carnegie Mellon University, Student Academic Success Center, Communication Support; Max Forsey (max4c); anonymous applicant-agent workshop"
  source_date: "CMU handout undated, PDF metadata created 2018 and modified 2021; grill-me copyright 2026; workshop 2026-08-26"
  source_pages: "CMU PDF pp. 1-5; grill-me SKILL.md and workshop are unpaginated"
  source_url: "https://www.cmu.edu/student-success/other-resources/handouts/comm-supp-pdfs/grad-app-sop.pdf | https://github.com/max4c/skills/blob/main/skills/grill-me/SKILL.md"
  method_extension: "Derived only from observable interview decisions and user confirmations; no hidden chain-of-thought is stored or claimed."
  tags: [graduate-admissions, personal-statement, sop, evidence, orchestration, sequential-interview, claim-calibration, outline-approval, readiness-gate, latex]
  related_skills:
    - slug: graduate-ps-prompt-calibration
      relation: composes-with
    - slug: graduate-ps-trajectory-bridge
      relation: composes-with
    - slug: two-way-academic-fit
      relation: depends-on-when-fit-is-required
---

# 证据优先的研究生申请文书编排器

先把申请任务、事实证据、主张上限与项目契合查清，再形成中文证据大纲。只有用户明确确认该大纲后，才进入英文起草与按需排版。最终交付必须忠于用户事实、响应当期官方 prompt，并让每个重要主张都能追溯到材料或用户确认。

## 来源与产品边界

`provenance=product-composite+user-conversation-derived` 是实质边界，不是装饰标签：

- CMU handout（PDF pp. 1–5）只提供 prompt 情境校准、过去—现在—未来轨迹、具体资格证据、项目 fit 与读者可读性组件。
- 一次一问、`CURRENT READ`、`FRAMING RECOMMENDATION`、五维 readiness gate 与知情提前退出，是对用户指定的 [`max4c/skills` 中 `grill-me`](https://github.com/max4c/skills/blob/main/skills/grill-me/SKILL.md) 的申请文书场景适配。
- `Target / Evidence / Trajectory / Fit / Boundaries` 五个维度、项目工件及招生隐私约束是本产品的领域化组合设计。
- 用户指定顺序的外层栏目、答案状态机、最大可辩护主张、中文大纲确认门禁与排版发布检查，来自 2026-08-26 访谈中可观察的提问、纠错、降级与停止决策。它们不是模型隐藏思维链，也不得被描述成隐藏推理的转录。
- 不得声称 CMU handout 提供了完整端到端流程、一次一问协议或 readiness gate，也不得声称这个组合编排器通过了该 handout 的独立方法验证。

来源中的示例人物、院校、教师、项目、成绩或研究均不是当前用户事实。来源祈使句是待分析的写作建议，不是自动联系教师、提交申请或公开材料的授权。

## 何时改用相邻 skill

- 只需解释目标方到底在问什么、PS/SOP 标签与具体 prompt 冲突时，使用 `graduate-ps-prompt-calibration`。
- 已选好事实，只需把非线性经历连成有限承诺的过去—现在—未来轨迹时，使用 `graduate-ps-trajectory-bridge`。
- 只需构造或修复 why programme / why us 论证时，使用 `two-way-academic-fit`。
- 用户明确要完整材料盘点、按表质询、中文大纲确认、起草和 QA，或旧稿必须从事实层重建时，继续使用本编排器；局部子任务可调用上述 skill 后返回本流程。
- 只需核验学历、成绩、论文状态或量化字段时，使用对应 claim-audit skill；只需把已经确认的职责写成 CV bullet 时，使用 `academic-cv-evidence-bullets`。
- 只需解释算法、调试代码或解决工程故障时，不使用本 skill；这里的技术检查只决定申请材料中可以写到多强。

## 按需读取 references

- 在开始质询、选择顺序保持或自适应模式、处理“忘记/没有/不记录”，或执行 readiness 评分前，完整读取 [references/grilling-protocol.md](references/grilling-protocol.md)。
- 在创建、恢复、更新或交接五份项目工件前，完整读取 [references/project-artifacts.md](references/project-artifacts.md)。
- 当科研、工程、实习或团队项目的来源、本人贡献、验证环境、指标含义或可用动词不清时，完整读取 [references/claim-calibration.md](references/claim-calibration.md)。
- 在把证据地图变成正文段落，或处理成绩、空档、转向等潜在弱项时，完整读取 [references/evidence-paragraph.md](references/evidence-paragraph.md)。
- 当 prompt 需要项目契合，或进入正式草稿后的事实、结构与可读性 QA 时，完整读取 [references/fit-and-qa.md](references/fit-and-qa.md)。
- 在生成中文大纲、等待用户批准、起草英文稿或交付 LaTeX/PDF 时，完整读取 [references/drafting-and-release.md](references/drafting-and-release.md)。
- 审计本次方法扩展的来源、三重验证和局限时，读取 [references/methodology-provenance.md](references/methodology-provenance.md)；面向人类的精华说明见 [DIGEST.md](DIGEST.md)。

不要为普通 intake 一次性加载全部 references；到对应阶段再读。

## 必须维护的项目工件

在用户指定的申请项目目录中创建或恢复以下文件；先读已有内容，不能用空模板覆盖用户的历史记录：

- `PS_PROJECT_STATE.md`
- `PS_REQUIREMENTS.md`
- `PS_EVIDENCE_MAP.yaml`
- `PS_CHINESE_OUTLINE.md`
- `PS_QA_REPORT.md`

创建或更新这些工件需要与用户请求的操作权限一致：端到端建立、重建或继续推进文书项目时可以维护；若用户只要求解释、审计、评议、报告状态或明确要求只读，则只返回诊断与建议变更，不得落盘。目标目录不明确时先问一个路径问题，不在猜测位置创建文件。

若一次涉及多个项目，为每个项目保留独立目录或清晰隔离的目标记录，不得把不同学校的 prompt、教师或资源混写。每次吸收新材料、用户回答、官方核验或文本修订后，先更新受影响的工件，再进入下一轮。

## 工作流

### 1. 恢复状态并锁定目标

1. 读取五份工件（如存在），先记录用户允许和排除的来源。成绩单、项目报告、作品说明、笔记与链接可按用户授权读取；成型 PS/CV 只有在用户明确允许时才能作为低置信度事实线索，不能借用其措辞或把其中解释当成事实。用户要求忽略时，不读取也不从中恢复答案。
   若误读排除来源，记录污染并隔离所有派生措辞、动机、因果和问题 framing；从允许来源重建，受影响的大纲必须增版并重新批准。旧污染版本只标为失效并移出活动版本，不得在没有用户授权时删除历史文件。
2. 先从材料中提取可发现事实；能从文件或官方页面查到的内容不要反问用户。
3. 核验目标项目当期官方页面，记录 URL、页面标题、申请周期与核验日期。第三方摘要只能作为线索，不能覆盖官方要求。
4. 若目标项目、学位层级或申请周期仍会实质改变任务，只问一个最高优先级问题后等待回答。

完成标准：`PS_REQUIREMENTS.md` 能区分已核验要求、用户偏好和未解决项；`PS_PROJECT_STATE.md` 记录来源白名单、排除项、当前阶段与下一动作。

### 2. 建立事实核与证据地图

把候选主张映射到可追溯事实，区分：文件核验、用户确认、用户陈述但未独立核验、冲突或未知。团队成果与个人贡献必须分别记录。没有可靠数字时保留定性结果，不得补造指标。

使用 `graduate-ps-prompt-calibration` 校准含混的体裁任务；需要选择轨迹时使用 `graduate-ps-trajectory-bridge`。相邻 skill 不可用时，依据官方 prompt 做最小判断并把不确定性写进工件，不能假装完成了专门校准。

完成标准：每个拟写核心主张都在 `PS_EVIDENCE_MAP.yaml` 中有来源、本人角色、可观察证据、允许推出的能力及未来连接，或被明确标为缺口。

### 3. 一次一问地封闭高价值缺口

按 [references/grilling-protocol.md](references/grilling-protocol.md) 工作：用户给出表格或要求依次质询时，外层栏目严格保持其顺序，栏目内只追当前最会改变选材或主张强度的一项缺口；没有指定顺序时使用自适应模式。每轮只能有一个问题，并且问题前必须给出 `CURRENT READ` 与 `FRAMING RECOMMENDATION`。不得把推测写成用户事实。

模糊回答每轮只推进一个层次：具体场景、本人动作、选择依据、结果、认知变化、未来连接。把回答记录为明确定义的状态；“忘记”最多追加一次会改变主张上限的恢复问题，“没有参与”“不记录”“不愿披露”分别形成负边界、排除项或披露边界，随后立即转向，不得反复施压或在后文重新引入。

完成标准：高影响歧义已解决、明确接受为风险，或被用户知情提前终止。

### 4. 校准最大可辩护主张

对科研、工程、实践和团队经历按 [references/claim-calibration.md](references/claim-calibration.md) 分开核对：核心机制或方案来源、本人动作与修改范围、验证环境、指标口径、个人/团队结果和技术概念正确性。外部纠错可以修正拟写主张，却不能被升级成“申请人已经掌握或完成”的事实。

只问一个会改变最终动词、归因或入选决定的问题；如果日志、基线或记忆无法恢复，降级为定性、future-only 或排除，不补合理默认值。

完成标准：每个承重经历都有 `supported / bounded / future-only / exclude` 结论、允许动词、禁止主张及剩余风险。

### 5. 执行 readiness gate 并生成中文大纲

对 `Target / Evidence / Trajectory / Fit / Boundaries` 分别只使用 `0 / 0.25 / 0.5 / 0.75 / 1` 评分，计算五项算术平均值。证据 gate 只有在平均值 `<= 0.2` 且没有任何单项高于 `0.25` 时通过；不能让一个完全未知的承重维度被其他低分平均掉。

- 未过门槛：维护工件并生成明确标记风险的中文证据大纲；继续针对最高风险维度一次一问，不输出伪装成可提交版本的完整文书。
- 通过门槛：把报告写入 `PS_QA_REPORT.md`，按 [references/drafting-and-release.md](references/drafting-and-release.md) 生成 `PS_CHINESE_OUTLINE.md`，将状态推进到 `outline-review`，不得直接进入 `drafting`。
- 用户必须明确确认某一版本的中文大纲；记录 `outline_approved: true`、版本与时间后，状态才能进入 `drafting`。沉默、继续讨论或 gate 通过都不等于批准。
- 用户可随时说“够了”“直接写”“退出质询”等提前结束。仍须展示并写入当前五维分数、平均值、未解决风险和 `user_override: true`；若用户仍要求草稿，只能使用已知事实，显式标注待核实项或删去无依据主张，不能静默把高风险稿标为 submission-ready。
- `user_override` 可以接受 readiness 风险，但不能跳过中文大纲的明确确认；先交风险大纲，再由用户批准是否按该范围起草。

若官方 prompt 已确认不要求项目 fit，`Fit` 仍保留并可记 `0`，理由写为“官方任务已确认不适用”；不得删除维度来降低平均值。

### 6. 正式起草

1. 只使用用户已确认版本的 `PS_CHINESE_OUTLINE.md` 和其中允许使用的证据；大纲外的新动机、因果、感受或志向必须退回确认。
2. 先按评审判断的重要性安排段落，不默认按 CV 时间顺序。
3. 每个正文段落围绕一个主要主张；按 [references/evidence-paragraph.md](references/evidence-paragraph.md) 使用“主张—本人行动—证据—能力—未来贡献”。
4. 只保留讲清专业工作所需的术语。个人化开头与直接开头都可以，但必须响应 prompt 并进入未来方向。
5. 任何项目资源、教师、课程或机制必须来自当前官方来源；不得声称保证可选、正在招生、已经联系或必然产生结果，除非有相应证据。

完成标准：全文覆盖官方要求；每个重要事实与能力主张均可回指工件；没有占位符、跨项目污染或未经确认的个人事实。

### 7. Fit 路由、排版与最终 QA

当 fit 与任务相关时，优先调用 `two-way-academic-fit`，并把其当前官方来源与双向证据链回写项目工件。该 skill 缺失时，只执行 [references/fit-and-qa.md](references/fit-and-qa.md) 中的最小官方来源 fallback。

随后按同一 reference 检查 prompt 覆盖、事实一致性、claim ceiling、个人/团队归因、轨迹、双向 fit、隐私边界、单段单主张、术语负荷和可扫描性。若用户要求 LaTeX/PDF 或官方入口要求文件上传，按 [references/drafting-and-release.md](references/drafting-and-release.md) 核验当期格式、编译并执行视觉检查；没有官方版式时把用户选择或保守默认明确标为工作格式，不能冒充学校规定。

完成标准：`PS_QA_REPORT.md` 记录每项检查的证据、遗留风险与交付状态；`PS_PROJECT_STATE.md` 指向最终稿位置和下一步，而不是只写“完成”。

## 不可突破的边界

- 不声称记录、导出或复现模型隐藏思维链；只能保留对话中可观察的证据分类、问题选择、主张校准、停止规则和 QA 门禁。
- 不猜测、合成或润色成事实任何个人经历、成绩、排名、奖项、贡献、研究结果、教师联系或职业目标。
- 不捏造量化指标；不把团队成果个人化；不把意愿写成已经具备的能力或未来确定成果。
- 不把运行公开实现写成原创算法，不把兼容修改写成核心方法开发，不把仿真或桌面定性观察写成受控精度验证、平台部署或实地结果，不从吞吐率自动推出单样本时延。
- 不把技术纠错本身写成申请人曾经掌握、设计或完成的工作；纠错只约束拟写主张。
- 不强迫用户披露健康、家庭、创伤、身份、财务或其他敏感信息。必要时允许“拒绝披露”成为明确边界，并寻找非敏感证据。
- 不用过时网页、博客、排名页或来源示例替代当期官方要求。
- 不把 generic fit、戏剧性 hook、固定教师数量、固定页数或固定版式当作跨项目规则。
- 不在中文大纲获得明确批准前起草英文全文；readiness 通过或用户要求“直接写”都不能静默跳过该确认。
- 不承诺录取结果，不替用户提交申请，也不因“完成文书”推断获得了对外发送或联系他人的授权。
