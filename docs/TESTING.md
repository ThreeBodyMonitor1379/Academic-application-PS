# 测试说明

本页记录 `v0.2.0` 发布包的可复现测试范围。测试只验证 skill 路由、可观察流程约束、发布包结构与安装器的非覆盖行为，不验证申请者事实、实时项目网页、文书的录取效果或任何录取概率。

## 环境

- 日期：2026-08-26
- 系统：Darwin arm64
- Python：3.12.13；项目支持 Python 3.10+
- 依赖：在仓库外的临时虚拟环境安装 `PyYAML==6.0.2`
- 申请素材：仅使用虚构、匿名 prompt；未读取或复制真实申请材料

## 固定路由集

三个 skill 的 [`test-prompts.json`](../skills/) 共包含 38 条 Darwin-compatible 用例。编排器在 `v0.2.0` 扩展了路由与边界集；两个聚焦 skill 的 `v0.1.0` 用例保持不变：

| Skill | 组件版本 | 应触发 | 不应触发 | 边界 | 合计 |
|---|---:|---:|---:|---:|---:|
| `evidence-first-graduate-personal-statement` | 0.2.0 | 5 | 6 | 11 | 22 |
| `graduate-ps-prompt-calibration` | 0.1.0 | 3 | 3 | 2 | 8 |
| `graduate-ps-trajectory-bridge` | 0.1.0 | 3 | 3 | 2 | 8 |
| **总计** |  | **11** | **12** | **15** | **38** |

不应触发用例包含兄弟 skill 与外部相邻能力诱饵：`two-way-academic-fit`、`field-role-audience-calibration` 和 `academic-cover-letter-evidence-map`。

## 双轮独立盲测

升级后的编排器先以 17 条核心路由用例进行两轮 clean-context 盲测。评测 agent 只收到完整的 skill name/description 路由表和匿名 prompt，没有收到 case type、expected behavior、notes、workspace 文件、先前结果或来源文档，并须为每条 prompt 选择一个 primary route。

| 轮次 | 唯一用例 | 正确路由 | 错误 | 诱饵误触发 |
|---|---:|---:|---:|---:|
| Round A | 17 | 17 | 0 | 0/6 |
| Round B | 17 | 17 | 0 | 0/6 |

随后新增的 `edge-07` 至 `edge-11` 作为聚焦盲测，覆盖 readiness hard cap、排除来源污染、无日志证据状态、只读权限和受污染版本失效。最终回归未发现绕过中文大纲批准的路径。

两个未修改的聚焦 skill 仍保留 `v0.1.0` 的双轮 **8/8、100%** 结果。各组件的完整结果和限制分别记录在自身 `test-results.md`。

## 行为压力测试与端到端 smoke test

独立评测覆盖了按用户栏目保序、混合否定回答、公开代码兼容适配、吞吐率与时延区分、团队成果与个人职责分离、大纲批准、风险 override、排除来源和工作格式 LaTeX。首轮识别出的原子主张拆分、readiness 单项上限、未受控量化阶段和来源污染处置缺口均已修正并重新盲测。

完全虚构的端到端 fixture 通过以下门禁：

- 在大纲批准前只生成五份项目工件，不生成英文、TeX 或 PDF。
- 排除的旧 PS/CV 未被读取、搜索、引用或转述。
- 单独的批准记录明确授权大纲 `v1` 后，才生成 717 词英文稿和对应 TeX。
- 公开算法只写兼容适配；运行界面吞吐率未被转换成单帧时延；团队资产未个人化。
- XeLaTeX 成功生成 2 页、50,293 字节 PDF；Times New Roman 字体嵌入，并逐页渲染检查裁切、溢出、密度与断页。
- 第一版出现近空白第二页后完成一次版式修订，再通过视觉 QA。

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
