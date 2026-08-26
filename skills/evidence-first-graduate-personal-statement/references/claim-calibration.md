# 最大可辩护主张校准

当科研、工程、实习、创作或团队项目的来源、本人贡献、验证环境、指标含义或可用动词不清时读取本文件。目标不是把经历写得最强，而是确定在现有证据下最强且仍可辩护的说法。

## R — 可观察原话

> “我只修改了……兼容性冲突的部分，没有修改算法等核心机制。”

> “没有误差记录。”

> “没有完成……测试。”

来源：2026-08-26 匿名研究生申请访谈；为保护隐私已删除设备、项目和申请人信息。以上只证明对话中出现过这些边界，不证明任何当前申请人的事实，也不是隐藏思维链。

## I — 核心解释

一项经历的主张上限由最弱边界决定，而不是由最亮眼的名词决定：

```text
最大可辩护主张 = 最保守地同时满足：
技术/概念正确性、核心方案来源、本人动作、修改范围、验证强度、指标可解释性、个人/团队归因
```

这不是算术评分，也不是把所有项目排成单一贡献阶梯。系统集成、参数调整、方法修改、验证和原创设计是不同维度；“全部由本人操作”不自动等于“核心算法由本人原创”。任何一项仍未知时，措辞必须停在能够被已知事实独立支持的下限。

## A1 — 已观察到的应用模式

### 公开实现与兼容适配

核心算法来自公开示例，申请人只替换依赖或 API 并完成桌面运行。可写 `adapted / configured / ran / observed`；不能写 `developed the algorithm / proposed / validated accuracy / deployed`。独立完成全部操作只证明执行所有权，不改变算法来源。

### 吞吐率与时延
批处理后运行界面报告单位时间处理量提高，但没有逐样本时延、尾延迟或端到端日志。可以写“在给定设置下观察到更高推理吞吐率”；不能自动推出单帧时延降低、实时链路改善或完整系统加速。

### 团队结果与个人职责
团队方法取得定量结果，申请人负责数据处理、运行监控或辅助分析。可分别写“团队实现 X；本人负责 Y”；不能把模型提出、核心架构或全部结果个人化。

### 未完成的集成
原型完成仿真或桌面验证，但因空间、供电、成本或接口约束未进入真实平台。可写已完成范围、识别的约束和后续设计认识；不能写成真实部署或性能验证。

## A2 — 触发与路由

### 触发场景

1. 用户不确定能否在 PS/SOP 中使用 `designed / developed / implemented / optimised / validated / deployed`。
2. 经历涉及公开代码、教程、复现、版本兼容、参数调整、系统集成或团队协作。
3. 只有仿真、桌面观察、运行界面数字或论文摘录，却想写成精度、时延、鲁棒性或真实部署成果。
4. 用户说“全部操作是我完成的”，但核心方法来源和个人修改仍不清楚。
5. 用户忘记参数、日志、误差、版本或测试条件，需要决定降级还是排除。

### 常见语言信号

- “这能写成我开发了算法吗？”“只是按公开示例跑通，PS 怎么说？”
- “FPS 提高能不能写成 latency reduced？”“只做仿真能写 deployed 吗？”
- “The team achieved the result, but what can I claim personally?”
- “I reproduced/adapted/integrated this project. Which verb is defensible?”

### 相邻任务边界

- 纯算法解释、公式推导、代码调试或工程修复：不使用本模块。
- 只核验学历、日期、成绩、论文状态或官方字段：使用 claim-audit 类 skill。
- 事实边界已经确定，只需写一条 CV bullet：使用 `academic-cv-evidence-bullets`。
- 只构造未来方向或 programme fit：分别使用 trajectory 或 fit skill。

## E — 执行步骤

### 1. 拆解候选主张

记录：技术/活动对象、核心机制或方案、本人动作、来源、修改范围、验证环境、结果、数字、团队动作和明确限制。

完成标准：能分别指出“谁提出核心方法”“用户本人做了什么”“系统在哪里被怎样测试”。

### 2. 做概念 sanity check

检查术语、系统层级、因果与指标语义。若用户理解有误，分成两层：

- `CONCEPT CORRECTION`：正确机制或指标解释。
- `APPLICANT FACT`：用户实际理解、操作或观察到的内容。

纠错不得回填成新的 applicant fact。

完成标准：拟写主张在技术或领域语义上成立，且没有把外部解释冒充个人能力。

### 3. 标记来源与修改范围

`core_source`：`applicant_original / team / public_example / tutorial / external_method / unknown / not_applicable`。

`modification_scope`：`none / dependency_compatibility / parameters / component_integration / system_design / core_method / unknown / not_applicable`。

完成标准：执行所有权与核心机制作者身份已分开；如果仍未知，只允许保守动词。

### 4. 标记验证阶段

`validation_stage`：`not_run / simulation / bench_qualitative / bench_quantitative_uncontrolled / controlled_quantitative / integrated_platform / field_deployment / unknown / not_applicable`。

`bench_quantitative_uncontrolled` 表示已有仪器或运行时数字，但基线、变量、样本或重复条件不足以支持受控比较。不得把阶段自动向上折算：仿真不是桌面硬件，桌面定性不是量化输出，未受控数字不是受控量化，平台集成也不是实地部署。

完成标准：正文所称测试或部署不超过实际阶段。

### 5. 通过指标门禁

对每个数字记录：实际测量对象、基线、输入或样本、硬件/环境、batch 或其他关键条件、测量方法、重复范围和结果所有权。然后检查：

- throughput 不自动等于 per-sample latency；平均值不自动等于 p95/p99。
- 方向一致的定性变化不等于角度精度或误差分布。
- 模型或论文指标不自动等于用户个人造成的提升。
- 主观评价需说明样本、评委、量表和汇总规则；否则只写有限反馈。
- 没有基线、控制变量或日志时，不使用 `optimised / improved / validated` 等因果或性能动词。

完成标准：数字的含义、条件和归属均能一句话说清；否则改为定性观察。

### 6. 只问一个决定性问题

选择最可能改变允许动词、个人归因、量化口径或是否入选的问题。用户回答 `forgotten / unknown` 后，仅在一次恢复会改变结论时再问；否则立即降级。

完成标准：没有为了补齐表格追问不影响主张的版本号、参数或日期。

### 7. 输出 Claim Boundary Card

```text
CLAIM BOUNDARY CARD
Candidate claim:
Mechanism status: correct / partial / incorrect / unknown / not_applicable
Core source:
Personal action:
Modification scope:
Team action or outcome:
Validation stage:
Metric scope and ownership:
Known limitations:
Maximum defensible claim:
Allowed verbs:
Unsupported claims:
Release: supported / bounded / future-only / exclude
Next decisive evidence or question: none / [one item]
```

完成标准：卡片足以直接更新 `PS_EVIDENCE_MAP.yaml` 和中文大纲，不需要写作者再猜贡献或测试强度。

## B — 边界与失败模式

- 不用“更保守”掩盖事实冲突；冲突必须标记并解决、降级或排除。
- 不把没有数字视为没有证据。完成的产物、观察到的变化、外部反馈、明确的约束或后续设计改变都可作为有限定性证据。
- 不把一个正确的技术解释追溯为申请人当时的理解，也不替用户制造“因此我意识到”的因果。
- 不因“本人完成全部操作”推断核心方法原创，不因“参与论文/项目”推断提出架构或拥有团队结果。
- 不把未完成项目包装成成功；只有在真实尝试、限制和认知变化清楚时，才写成边界化反思。
- 不要求恢复无法合理获得的日志或版本。保守版本已经足以服务论证时即停止。
- 该模块只控制申请材料主张，不是技术审查、同行评议、专利新颖性判断或算法正确性证明。
