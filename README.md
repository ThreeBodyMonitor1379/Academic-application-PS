# Graduate Personal Statement Skills港新研究生申请工具包

一套面向 Codex 的中文研究生申请文书 skills：先审计允许来源和项目当期要求，再按用户栏目一次一问，校准可辩护主张并确认中文证据大纲，最后按需交付英文稿与 LaTeX/PDF。目标是生成**任务响应准确、主张可追溯、轨迹可信且保留答案所有权**的 Personal Statement、Statement of Purpose 或 application essay。

**稳定版：[`v0.2.0`](https://github.com/ThreeBodyMonitor1379/Academic-application-PS/tree/v0.2.0)** · [更新日志](./CHANGELOG.md) · [测试说明](./docs/TESTING.md) · [AGPL-3.0](./LICENSE)

适用于授课型硕士、研究型硕士和博士申请，并适配不同国家、项目与文书语言。它不是固定模板，也不会用 PS/SOP 标签或通用 handout 覆盖目标方当期官方要求。

> [!IMPORTANT]
> 事实一致高于措辞亮眼；具体 prompt 高于文件标签；当期官方要求高于通用指南。不得虚构经历、数字、个人贡献、教师联系或项目资源。本项目与 Carnegie Mellon University 及其 Student Academic Success Center 无隶属、赞助或认证关系。

## 🚀 懒人指令｜整段复制给 Agent（推荐）

> [!TIP]
> 下面是**给 Agent 执行的安装任务**，不是给人手动运行的 shell 命令。复制整个代码块即可。

```text
你是本次安装执行 Agent。请直接完成操作，不要只给教程；在满足验收标准前持续检查。

仓库：https://github.com/ThreeBodyMonitor1379/Academic-application-PS
固定版本：v0.2.0
目标：安装该版本 skills/ 下全部 3 个 Codex skills。

3 个目标：evidence-first-graduate-personal-statement、graduate-ps-prompt-calibration、graduate-ps-trajectory-bridge。

执行要求：
1. 检测实际 Codex skills 目录、操作系统、Python 3.10+ 和现有同名 skills；不要假设固定 HOME 路径。
2. 从 v0.2.0 tag 下载仓库到系统临时目录；不得从 main 或未经固定的分支安装。优先使用已有 GitHub/skill 安装能力，必要时只对临时副本执行 git clone。
3. 在仓库和 skills 目录之外创建临时虚拟环境，按 requirements-dev.txt 安装固定依赖；不要修改系统 Python，不要在 skill 目录内创建 .venv。
4. 先运行 scripts/validate_release.py，再分别运行 scripts/quick_validate.py <skill_dir>。要求 3/3 结构校验通过。
5. 运行 python -m unittest discover -s tests -p 'test_*.py'；要求全部测试实际执行，failures=0、errors=0、skipped=0。
6. 使用 scripts/install_skills.py 安装完整目录。该脚本必须按相对文件清单与 SHA-256 将每个目标判为：不存在则 installed；完全相同则 identical；任何内容不同或目标不是普通目录则 conflict。
7. 任何 conflict 都不得覆盖、删除、合并、移动或加符号链接；保留目标原状，并继续检查其他 skill。不得只复制缺少的文件来制造混装状态。
8. 安装后再次比较源目录和目标目录的相对文件清单及 SHA-256；installed/identical 才算成功。
9. 只检测、不擅自安装仓库外的 two-way-academic-fit；缺失时说明编排器将使用最小官方来源 fallback。
10. 不读取、复制、上传或测试真实申请材料和联系方式；不联系教师，不提交申请，不付款，不执行外部发布。

完成标准：3 个目标均为 installed 或 identical；3/3 结构校验通过；仓库测试零失败、零错误、零跳过。任何 conflict 都必须明确列出，不能声称全量安装完成。

最终报告必须包含：release/tag、临时下载路径、实际 skills 安装路径、每个 skill 的 installed/identical/conflict 状态、相对文件清单和 SHA-256 比较、Python 与临时虚拟环境、校验和测试结果、two-way-academic-fit 状态，以及“新建 Codex 任务后生效”的提示。
```

## 先选入口

| 你的情况 | 使用的 skill | 结果 |
|---|---|---|
| 只有零散材料、冲突旧稿，或要从要求核验一路做到草稿和 QA | [`evidence-first-graduate-personal-statement`](./skills/evidence-first-graduate-personal-statement/SKILL.md) | 按表逐问、校准主张并形成中文证据大纲；获批后再起草与排版 |
| 不确定题目到底要求什么，或 PS/SOP 标签与 prompt 冲突 | [`graduate-ps-prompt-calibration`](./skills/graduate-ps-prompt-calibration/SKILL.md) | 生成带来源的任务、体裁、语气、开头和硬约束简报 |
| 经历很散、跨专业，或不知道怎样连接过去—现在—未来 | [`graduate-ps-trajectory-bridge`](./skills/graduate-ps-trajectory-bridge/SKILL.md) | 用未来方向过滤经历，建立具体但非绑定的发展轨迹 |

> [!NOTE]
> 只修 why programme / why department 段时，优先使用仓库外的 `two-way-academic-fit`。它不随本仓库分发；缺失时，编排器只做最小的当期官方来源核验。

<details>
<summary><strong>三个常用调用示例</strong></summary>

从原始材料端到端完成一篇文书：

```text
请用 $evidence-first-graduate-personal-statement，忽略我已成型的 PS/CV，只读取我允许的成绩、项目记录和官方要求；按我给定的栏目顺序每轮问一个问题，先形成中文证据大纲。我明确确认该版本后，再起草英文 SOP，并按需交付 LaTeX/PDF 与最终 QA 报告。
```

先校准一个名称含混的题目：

```text
请用 $graduate-ps-prompt-calibration。学校把文件叫 Personal Statement，但题目主要问研究准备、未来目标和 programme fit。请按当期官方要求输出写作约束，不要先套 PS 模板。
```

连接跨专业经历，但不虚构终身承诺：

```text
请用 $graduate-ps-trajectory-bridge，把我从社会学、用户研究到 HCI 的真实经历筛成一条可信轨迹；不要编造“从小就想做”，也不要把未来职业说死。
```

</details>

## Evidence-first 概览

```text
来源审计与官方要求 → 事实地图与主张校准 → 按序一次一问 → readiness gate
        → 中文证据大纲 → 用户确认 → 英文草稿 → LaTeX/PDF 与最终 QA
```

编排器维护五份可恢复产物：

| 产物 | 记录什么 |
|---|---|
| `PS_PROJECT_STATE.md` | 当前阶段、目标、已确认决定、开放问题、质询分数和用户 override |
| `PS_REQUIREMENTS.md` | 官方链接、核验日期、原始 prompt、字数与格式约束 |
| `PS_EVIDENCE_MAP.yaml` | 回答状态、证据来源、本人归因、修改范围、验证阶段、指标口径、主张上限与发布状态 |
| `PS_CHINESE_OUTLINE.md` | 各栏目已确认事实、拟用主张、证据等级、禁用内容、风险和批准版本 |
| `PS_QA_REPORT.md` | prompt 覆盖、事实追溯、轨迹、fit、语言、格式、隐私与遗留风险 |

质询每轮只有一个问题，并固定使用 `CURRENT READ / FRAMING RECOMMENDATION / QUESTION`。五维 readiness 为 Target、Evidence、Trajectory、Fit、Boundaries：平均值不高于 `0.20` 且每个维度不高于 `0.25` 才通过证据门禁。通过后仍须让申请人明确批准某个中文大纲版本；风险 override 不能静默跳过内容所有权门禁，agent 也不得猜测事实。

## 来源方法与产品组合

两个原子 skill 来自对 Carnegie Mellon University handout 的 RIA-TV++ 蒸馏，并通过本项目的 V1 跨情境、V2 预测力和 V3 独特性门禁：

- `graduate-ps-prompt-calibration`：以具体 prompt 与当期官方说明裁决 PS/SOP 标签冲突。
- `graduate-ps-trajectory-bridge`：用有界的未来方向过滤经历，并按论证重要性建立轨迹。

`evidence-first-graduate-personal-statement` 在 `v0.2.0` 标记为 `product-composite+user-conversation-derived`。它把上述两项方法、证据地图、内部证据段落检查表、项目契合路由、QA，以及对 `max4c/skills` 中 `grill-me` 的一次一问交互适配组合成端到端流程；顺序保持、答案状态机、主张校准、大纲批准和排版发布规则只来自匿名访谈中可观察的决策协议，不记录或声称模型隐藏思维链，也不冒充 CMU handout 独有或已单独验证的方法。

## 手动安装与验证

<details>
<summary><strong>安全安装全部 3 个 skills</strong></summary>

需要 Git 和 Python 3.10+。以下命令固定到 `v0.2.0`，安装器不会覆盖或混装冲突目录：

```bash
git clone --branch v0.2.0 --depth 1 \
  https://github.com/ThreeBodyMonitor1379/Academic-application-PS.git
cd Academic-application-PS

python3 -m venv /tmp/personal-statement-skills-venv
/tmp/personal-statement-skills-venv/bin/python -m pip install \
  -r requirements-dev.txt

/tmp/personal-statement-skills-venv/bin/python scripts/validate_release.py
for skill_dir in skills/*; do
  /tmp/personal-statement-skills-venv/bin/python \
    scripts/quick_validate.py "$skill_dir"
done

/tmp/personal-statement-skills-venv/bin/python \
  scripts/install_skills.py
```

默认安装目标为 `$CODEX_HOME/skills`（若已设置），否则为当前用户的 `.codex/skills`。可用 `--target-dir /绝对路径` 显式指定。安装后请新建一个 Codex 任务。

</details>

<details>
<summary><strong>验证范围与限制</strong></summary>

`scripts/validate_release.py` 检查发布文件、frontmatter、agents 配置、JSON/YAML、链接、测试集分布、许可证、第三方声明和禁止发布内容。`scripts/quick_validate.py` 对单个 skill 执行紧凑结构校验。

这些脚本能检查结构和静态约束，不能证明申请者事实真实、某种写法提高录取率、项目网页仍然有效，或一篇文书已经适合提交。官方要求核验、事实确认和人工审阅仍然不可替代。

</details>

## 质量、隐私与文档

当前固定路由集共 38 条：升级后的编排器为 5 条应触发、6 条不应触发和 11 条边界场景，两个聚焦 skill 各保留 3/3/2。编排器通过两轮独立 `17/17` 路由盲测，诱饵误触发均为 `0/6`；另有五项边界回归和一次完全虚构的端到端 LaTeX/PDF smoke test。结果只说明当前测试集内的路由与流程符合预期，不代表录取率。详见 [测试说明](./docs/TESTING.md)。

隐私硬规则：

- 不把真实申请材料、联系方式或敏感经历放入测试、日志、公开仓库或审计样例。
- 不强迫披露健康、家庭、创伤、身份、财务或成绩弱项的原因。
- 申请材料只在用户指定的本地项目范围内处理；完成文书不等于获得上传、提交或联系教师的授权。
- 来源中的人物、学校、教师、研究和结果只是教学示例，不是当前用户事实。

进一步阅读：[术语词典](./docs/GLOSSARY.md) · [测试说明](./docs/TESTING.md) · [更新日志](./CHANGELOG.md) · [第三方声明](./THIRD_PARTY_NOTICES.md)

## 来源与许可证

本仓库采用 [`cangjie-skill`](https://github.com/kangarooking/cangjie-skill) 的 RIA-TV++ 结构、蒸馏流程与 Darwin-compatible 测试格式。核心内容来源为 Carnegie Mellon University Student Academic Success Center, Communication Support 的 [*Writing Your Graduate School Application Essay*](https://www.cmu.edu/student-success/other-resources/handouts/comm-supp-pdfs/grad-app-sop.pdf)；本仓库只发布方法蒸馏，不分发原 PDF、截图、完整范例或申请人材料。

一次一问、先检查已有信息、给出当前判断与推荐、保留退出风险报告的交互层，改编自 [`max4c/skills` 的 `grill-me`](https://github.com/max4c/skills/blob/main/skills/grill-me/SKILL.md)，其原项目采用 MIT License。`v0.2.0` 新增方法只保存匿名对话中可观察的访谈与发布协议，不保存隐藏思维链或申请人事实。完整归属见 [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md)。

本仓库依照 [GNU Affero General Public License v3.0](./LICENSE) 发布；该许可证不覆盖 CMU handout、`max4c/skills` 或其他第三方材料。
