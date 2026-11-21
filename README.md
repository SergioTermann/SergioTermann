<div align="center">
  <img src="./images/profile.jpg" alt="郝帅的个人照片" width="128">
  <h1>郝帅 · Shuai Hao</h1>
  <p><strong>北京航空航天大学博士研究生 · 大模型 Agent 后训练与多模态强化学习</strong></p>
  <p>
    <a href="https://sergiotermann.github.io/SergioTermann/">个人网站</a> ·
    <a href="mailto:by2203054@buaa.edu.cn">邮箱</a> ·
    <a href="https://github.com/SergioTermann?tab=repositories">代码仓库</a> ·
    <a href="./README_EN.md">English</a> ·
    <a href="./README_DE.md">Deutsch</a>
  </p>
</div>

我研究长链路 Coding Agent 的前缀价值建模，以及视觉语言模型的集合级强化学习。此前在北京风起时域科技担任合伙人及 AI 团队负责人，主导智能运维 Agent 的架构、训练和生产交付。

**实习意向** · 北京，大模型 Agent 后训练算法，每周 5 天，可实习 6 个月。

## 代表工作

### Geo-RL · 长文本图像描述的集合级强化学习

**ICML 2026 · 学生一作**

参与方法建模、奖励设计与实验验证。Geo-RL 用 CLIP 质量加权的 DPP 衡量一组描述的语义覆盖，并用留一边际奖励把集合收益分配给单条描述。在 DeCapBench 上，相比 LLaVA-1.5 7B MLE，**语义体积（SVS）从 2.20 提升至 3.55**，Distinct-2 从 0.66 提升至 0.84，物体幻觉率从 8.3% 降至 7.1%。

### PVM · 长链路 Coding Agent 的前缀价值模型

**IEEE TNNLS 在审 · 第一作者 · 独立完成**

以任务终局成败监督中间状态的成功概率估计，用于 Best-of-N 选择和推理早停。在信息预算对齐的实验中，**Best-of-N 选择性能为 0.926 ± 0.049**，接近 verifier oracle 的 0.931，无需额外执行测试。早停节省约 **15% 的端到端推理算力**，精度损失接近零。基于 vLLM 构建轨迹采集和张量并行评测流程，覆盖 Qwen2.5-Coder 7B–72B 与 SWE-bench-Lite。

### 智能运维 Agent · 后训练与生产部署

**北京风起时域科技 · 前 AI 团队负责人 · 2024.09–2026.10**

主导 Planner–Executor、混合 RAG、工具调用与失败样本回流。基于 TRL 和 vLLM 对 Qwen3-8B 进行 LoRA / GRPO 后训练，通过字段级奖励和样本筛选将槽位提取指标从 0.914 提升至 0.961。上线后，**工单闭环率提升 12.4%**，工具幻觉率从 6.8% 降至 2.9%。

## 论文与研究经历

- **ICML 2026 · 学生一作** — *Escaping the Likelihood Trap: Geometric Diversity Optimization for Long-Form Image Captioning*
- **IEEE TNNLS · 第一作者，在审** — *Outcome-Supervised Prefix Value Models for Best-of-N Selection and Early Abandonment in Long-Horizon Coding Agents*
- **IEEE SMC Magazine · 第一作者，已录用** — *Human-Guided Autonomous Learning for UAV Air Combat Decision Optimization*
- **ICICIP 2021 · 第一作者** — *Learning Representation with Q-irrelevance Abstraction for Reinforcement Learning*
- **IEEE TCDS 2023 · 合著** — SCQRL，QIARL 的扩展工作

曾在中国科学院自动化研究所赵冬斌团队实习，研究强化学习状态抽象，并将自研的 learner–actor 采样系统迁移至 Ray / RLlib。参与 NeurIPS 2020 AIcrowd Procgen 强化学习挑战赛，第一轮排名 **7/82，高校第一**。

## 教育背景

- **北京航空航天大学** · 自动化科学与电气工程学院 · 博士在读，2022.09 至今
- **北京航空航天大学** · 软件学院 · 硕士，2019.09–2021.12，北京市优秀毕业生
- **北京理工大学** · 光电学院 · 本科，2014.09–2018.06，优秀毕业论文

研究之外，我是北航乒乓球校队成员，北京市积分 1650。
