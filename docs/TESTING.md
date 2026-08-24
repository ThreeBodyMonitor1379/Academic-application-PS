# 测试说明

本页记录 `v0.1.0` 的可复现测试范围。测试只验证 skill 路由、书面流程约束、发布包结构与安装器的非覆盖行为，不验证申请者事实、实时项目网页、文书的录取效果或任何录取概率。

## 环境

- 日期：2026-08-24
- 系统：Darwin arm64
- Python：3.12.13；项目支持 Python 3.10+
- 依赖：在仓库外的临时虚拟环境安装 `PyYAML==6.0.2`
- 申请素材：仅使用虚构、匿名 prompt；未读取或复制真实申请材料

## 固定路由集

每个 skill 的 [`test-prompts.json`](../skills/) 固定 8 条 Darwin-compatible 用例：

| Skill | 应触发 | 不应触发 | 边界 | 合计 |
|---|---:|---:|---:|---:|
| `evidence-first-graduate-personal-statement` | 3 | 3 | 2 | 8 |
| `graduate-ps-prompt-calibration` | 3 | 3 | 2 | 8 |
| `graduate-ps-trajectory-bridge` | 3 | 3 | 2 | 8 |
| **总计** | **9** | **9** | **6** | **24** |

不应触发用例包含兄弟 skill 与外部相邻能力诱饵：`two-way-academic-fit`、`field-role-audience-calibration` 和 `academic-cover-letter-evidence-map`。

## 双轮独立盲测

两名 clean-context 评测 agent 各自只收到完整的 skill name/description 路由表和 24 条匿名 prompt。它们未收到 case type、expected behavior、notes、workspace 文件、先前结果或来源文档，并须为每条 prompt 选择一个 primary route。

| 轮次 | 唯一用例 | 正确路由 | 错误 | 跳过 | 诱饵误触发 |
|---|---:|---:|---:|---:|---:|
| Final round A | 24 | 24 | 0 | 0 | 0/9 |
| Final round B | 24 | 24 | 0 | 0 | 0/9 |
| **合计判断** | **48** | **48** | **0** | **0** | **0/18** |

因此每个 skill 在两轮中均为 **8/8、100%**；完整结果分别保存在各 skill 的 `test-results.md`。

预终版诊断没有被隐藏：两名最初评测者都把两条 prompt-calibration 边界用例路由到其他能力。一条同时要求“校准”和“完整起草”，另一条只有通用 SOP 标签却要求固定比例，测试文本本身超出了 skill 描述。两条用例被收紧为目标特定的校准任务后，换用两名新的 clean-context 评测者重跑全部 24 条，才得到上表的最终结果。

## 质询协议与匿名前向场景

独立评测者完整读取产品编排器及其四份 references，使用虚构材料执行 9 个 instruction-conformance 场景，结果为 **9/9、100%**：

| ID | 场景 | 关键验收 |
|---|---|---|
| M1 | 已有材料可发现信息 | 不重复询问，转向最高价值未知项 |
| M2 | 空泛回答 | 使用固定三段格式，每轮只追问一个最早且重要的缺口 |
| M3 | 敏感经历 | 停止施压，记录 `do_not_disclose`，改用非敏感证据 |
| M4 | 用户提前退出 | 保留五维分数、风险与 `user_override: true`，不标 submission-ready |
| M5 | 官方要求与 handout 冲突 | 当前具体官方规则优先；不硬编码旧默认值 |
| M6 | readiness 未过门 | 无 override 时禁止正式完整草稿 |
| F1 | 授课型硕士 | 服从实践导向 prompt，不假设研究或导师 fit |
| F2 | 研究型硕士／博士 | 区分团队结果与本人贡献，闭合官方 fit 双向链 |
| F3 | 跨专业＋学业弱项 | 尊重隐私，以恢复证据和真实方法迁移连接，不编造因果 hook |

同一评测还核对：`CURRENT READ → FRAMING RECOMMENDATION → QUESTION` 每轮只有一个问题；评分仅使用 `0 / 0.25 / 0.5 / 0.75 / 1`；五维算术平均值不高于 `0.2` 才通过；四份项目工件名称固定；`two-way-academic-fit` 缺失时只执行最小官方来源 fallback。

## 结构、发布与安装测试

结构测试包括：

- 3/3 `scripts/quick_validate.py` 通过；
- `scripts/validate_release.py` 全部检查通过；
- frontmatter 只使用支持字段，目录名与 `name` 一致；
- `agents/openai.yaml` 均启用隐式调用；
- JSON/YAML 可解析，所有相对链接有效；
- 无符号链接、源 PDF、截图、真实材料、未完成标记或未声明的 skill；
- AGPL-3.0 正文、CMU 来源说明与 `grill-me` MIT 归属完整。

安装器使用 Python 标准库 `unittest` 执行 4 条测试，结果 **4/4、100%**，`failures=0`、`errors=0`、`skipped=0`：

1. 目标不存在：复制完整目录并返回 `installed`，源/目标 manifest 相同。
2. 内容完全相同：返回 `identical`，不改写目标。
3. 已有目录内容不同：返回 `conflict`，目标 manifest 前后不变。
4. 同名目标是普通文件：返回 `conflict`，文件内容不变。

manifest 比较包含相对文件清单和每个文件的 SHA-256。安装器禁止符号链接；发生冲突时不会覆盖、删除或把两个版本混装。

此外，使用本发布包的三个真实 skill 目录完成集成模拟：第一次全部返回 `installed`，第二次全部返回 `identical`；随后只改动临时目标中的一个 `SKILL.md`，第三次该项返回 `conflict`、另外两项保持 `identical`。冲突文件执行前后的 SHA-256 相同，证明安装器没有覆盖本地改动。

## 复现命令

在仓库根目录、仓库外的临时虚拟环境中运行：

```bash
python3 -m venv /tmp/personal-statement-test-venv
/tmp/personal-statement-test-venv/bin/python -m pip install \
  -r requirements-dev.txt

for skill_dir in skills/*; do
  /tmp/personal-statement-test-venv/bin/python \
    scripts/quick_validate.py "$skill_dir"
done

/tmp/personal-statement-test-venv/bin/python scripts/validate_release.py
/tmp/personal-statement-test-venv/bin/python -m unittest discover \
  -s tests -p 'test_*.py' -v
```

盲测和多轮模拟是独立 agent 评测，不由本地 Python 脚本伪装重放。公开 `test-results.md` 记录最终判断和测试边界；完整抽取候选、淘汰记录与评测工作底稿只保留在本地审计树，不随发布包分发。

## 解释限制

- 100% 只表示固定测试集内全部判断符合预先声明的边界。
- 静态校验不能发现所有自然语言误路由，也不能替代真实任务中的人工复核。
- 匿名模拟不能证明某种文书策略带来录取优势。
- 项目要求和教师信息会变化，使用 skill 时仍必须重新核验当期官方来源。
