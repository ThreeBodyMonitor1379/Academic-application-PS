# 中文大纲确认、英文起草与排版发布

在生成 `PS_CHINESE_OUTLINE.md`、判断能否进入英文起草，或交付 LaTeX/PDF 时读取本文件。核心不变量是：证据 gate 与申请人内容所有权是两道不同的门。

## 1. 生成中文证据大纲

大纲首先是事实和主张接口，其次才是文章结构。按官方 prompt 与用户 schema 建立以下内容：

```text
Target and prompt:
Outline version:
Source scope:
Readiness status:

[Section / proposed paragraph]
- Purpose in the argument:
- Confirmed applicant facts:
- Maximum defensible claim:
- Personal action vs team outcome:
- Evidence and verification status:
- Capability supported:
- Future or programme connection:
- Allowed wording / verbs:
- Excluded or future-only content:
- Open risk:

Approval:
- outline_approved: false
- approved_at: null
- approval_locator: null
```

没有足够证据的栏目可以保留为风险或删除，不用空泛句子填满。若用户给定的访谈顺序与最终文章顺序不同，记录“素材栏目 → 正文段落”的映射，不擅自改变素材含义。

若此前误读了 `excluded_sources`，先执行污染处置：在 source audit 记录发生过访问与受影响工件，隔离由该来源产生的措辞、动机、因果和引导问题，从活动大纲/草稿删除派生内容，并用允许来源重新建立。把被污染的大纲或稿件版本写入 `invalidated_versions`；先让 outline 的 `active_version` 指向只用允许来源重建的未批准版本，同时把 draft 的 `active_version` 设为 `null`。旧文件仅作隔离审计记录，未获用户授权不得删除。受影响的承重大纲必须增版并重新批准；只有该版本获批后才可生成新的英文稿，不得因为“已经看见”就继续使用或越过批准门禁。

完成标准：一个未参与访谈的写作者只看大纲，也不会需要猜动机、因果、贡献、数字或 programme fit。

## 2. 取得明确批准

向用户展示或交付具体版本的大纲，并只要求确认内容边界。有效批准必须能回查到用户对该版本的明确表达，例如“认可这个大纲”“按 v2 起草”。以下不构成批准：

- readiness gate 通过。
- 用户继续回答问题或讨论措辞。
- 用户曾在更早阶段说“以后可以直接写”。
- Agent 认为内容已经足够。

`user_override` 可以接受未解决证据风险，但不能代替大纲批准。用户要求跳过质询或“直接写”时，先根据已知事实生成风险大纲，再等待明确确认。

修改承重事实、动机、因果、职业目标、fit 或禁用边界后，增加版本并重新批准。仅改语法、拼写或不改变含义的排版不需要重开内容审批。

完成标准：`PS_PROJECT_STATE.md` 和大纲都记录 `outline_approved: true`、版本、时间与 approval locator。

## 3. 起草英文正文

1. 只使用获批大纲中的主张和来源；未获批的新内容退回用户确认。
2. 先满足当期官方 prompt，再决定个人化或直接开头、段落数量和经历次序。
3. 每段只证明一个主要判断，使用 evidence paragraph 协议展开。
4. 对 `bounded` 主张严格使用允许动词；`future-only` 只能写成希望学习、研究或验证的方向；`exclude` 不得出现。
5. 采用目标项目要求的语言与变体；没有要求时遵循用户偏好，不把英式或美式英语设成跨项目规则。
6. 字数统计口径与官方字段一致；标题、页眉或引用是否计入要明确记录。

完成标准：正文每个承重句都能映射到大纲和 evidence map；没有从旧 PS/CV 借来的未经确认措辞、占位符或跨项目资源。

## 4. 核验格式要求

先查当期官方 programme 页面、申请入口说明、FAQ 或官方书面回复，并记录：

- 是否必交、上传还是文本框。
- 字数/字符/页数限制及计数口径。
- 允许文件类型、大小、命名和匿名要求。
- 字体、字号、边距、行距、纸张或模板要求。
- 主文书与 additional information/short answers 的分工。

若官方没有明确字体或版式：

- 允许使用用户指定或可读的保守工作格式。
- 在 `PS_QA_REPORT.md` 写明 `format_status: working_default_not_official`。
- 不得称 Times New Roman、固定字号、页边距或两页为学校要求。
- 网申开放、要求更新或上传前重新核验高漂移字段。

完成标准：每条硬约束都有官方来源和核验日期；未知项显式保留。

## 5. LaTeX/PDF 分支

仅在用户要求或上传形式适合时生成 `.tex` 和 PDF；文本框任务优先交付纯文本，不为了形式强制 LaTeX。

1. 若环境提供 LaTeX 编译 skill，先读取并使用；否则探测可用编译器。没有成功编译时不得声称已生成有效 PDF。
2. 字体设置服从官方要求或用户选择。使用系统字体时选择匹配的 XeLaTeX/LuaLaTeX 路径；不要静默用近似字体冒充指定字体。
3. 编译后检查日志中的 error、missing font、overfull/underfull box 和未解析引用。
4. 若环境提供 PDF 检查 skill，渲染每页并进行视觉检查；否则明确报告未执行视觉 QA。
5. 记录编译器、页数、词数/字符数、PDF 大小、字体嵌入、纸张、边距、行距、断页和视觉结果。
6. 检查孤立标题、接近空白页、过密段落、页眉页脚污染、裁切、溢出和不可读字符。

完成标准：源文件和 PDF 都存在，编译成功，所有页面经过视觉检查，且文件符合已核验上传限制；否则发布状态保持 `hold` 或 `draft-with-risk`。

## 6. 发布状态

- `hold`：证据、批准、官方约束或文件质量仍阻止交付。
- `outline-awaiting-approval`：中文大纲已生成但尚未获得明确批准。
- `draft-with-risk`：用户知情接受 readiness 风险且批准大纲；草稿可审阅但不能标为 submission-ready。
- `ready-for-user-review`：内容与格式 QA 已完成，供申请人最终确认；不等于授权提交或录取保证。

交付说明必须分别列出：内容状态、官方格式状态、编译状态、视觉 QA 状态、仍需用户确认的事实和门户开放后需复核的项目。

## 边界

- 不因用户批准大纲而推断其批准最终英文措辞、敏感表达或提交行为。
- 不用排版精致掩盖证据 gate、claim ceiling 或 programme facts 的风险。
- 不把“PDF 能打开”当作视觉 QA；也不把无错误编译等同符合官方上传要求。
- 不在同一目录混放不同学校的 prompt、fit 来源、批准大纲或最终稿而不做清晰隔离。
