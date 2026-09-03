<div align="center">
  <img src="./images/profile.jpg" alt="郝帅" width="168" />
  <h1>郝帅</h1>
  <p><strong>算法工程师 · 大模型 Agent / LLM 后训练 / 多智能体强化学习</strong></p>
  <p>北京航空航天大学自动化科学与电气工程学院博士研究生 · AI Team Lead</p>
  <p>
    <a href="mailto:shuaihao@buaa.edu.cn">邮箱</a> ·
    中国北京 ·
    <a href="https://github.com/SergioTermann">GitHub</a> ·
    <a href="./README.md">English</a> ·
    <a href="./README_DE.md">Deutsch</a>
  </p>
</div>

## 核心定位

面向大模型 Agent 与强化学习后训练的算法工程师，习惯按“问题定义、数据构造、模型训练、离线评测、在线推理、指标回流”的闭环推进。当前以 AI Team Lead 身份负责生产级 Agent 系统，同时在北京航空航天大学攻读博士学位。

主线能力集中在：Agentic RL 后训练、过程奖励模型与轨迹治理、多智能体强化学习、大规模训练与评测基础设施，以及 vLLM/GPU 集群上的本地化部署。

## 技术栈

| 方向 | 方法与工具 |
| --- | --- |
| LLM 后训练 | RLVR / GRPO / GSPO、SFT / DPO、Reward Engineering、PRM / PVM、Best-of-N |
| Agent 系统 | Planner-Executor、混合 RAG、Function Calling、MCP / A2A、Context Engineering、SWE-bench |
| 强化学习 | PPO / SAC / GAIL、多智能体 RL、Ray / RLlib、AReaL、TRL、LoRA |
| 推理与部署 | vLLM、Ollama、Xinference、Dify、GPU 集群、Isaac Sim / Isaac Lab、Harfang DogFight |

## 代表项目

### 智能运维 Agent 生产闭环 · 2025 - 至今

**北京风起时域科技有限公司 · 合伙人 / AI Team Lead / 项目 Owner**

- 主导 Planner-Executor 主链路，落地混合 RAG、Function Calling 工具层与失败 case 自动回流，形成“采集、训练、评测、部署、反馈”的数据飞轮。
- 基于 TRL GRPOTrainer + vLLM 对 Qwen3-8B LoRA 做 RLVR/GRPO 后训练；完成字段级奖励、中英等价判定与奖励误伤修复，并把训练样本从 9215 条治理到 2310 条高价值数据。
- 线上效果：工单闭环率 +12.4%，首修成功率 +8.7%，自助诊断闭环率 +18.5%；工具幻觉率 6.8%→2.9%，TTFT P50 860ms→810ms；项目获清华力合投资，估值约 4000 万元。
- 将易变知识外置到结构化检索底座，用五道数据门禁、DAPO 动态采样和 SFT→GRPO 课程组织训练，迭代周期从 1-2 天压缩到半天以内。

### 长链路 Coding Agent 的过程价值建模 · 2026 - 至今

**Prefix Value Model · 第一作者 · TNNLS Under Review**

- 以终局成败为唯一监督，在可观测过程状态上学习成功概率，统一支持 Best-of-N 选择、推理时早停和结局可预测性分析。
- 在 SWE-bench-Lite 上取得选择性能 0.926±0.049，逼近 verifier oracle 0.931，高于多数投票 0.826 与轨迹级 PRM 0.901，且零额外测试执行开销。
- 基于 PVM 阈值提前放弃低成功率 rollout，节省约 15% 端到端推理算力，精度近零损失；第 3 轮即可较可靠预判终局成败，AUC 0.73→0.95。
- 构建 vLLM 轨迹采集与多型号张量并行推理系统，在双卡 48GB 环境完成 72B 可控评测；LoRA 拒绝采样微调将单次修复成功率从 0.375 提升到 0.800。

### 多模态大模型强化学习 · 2024 - 2026

**ICML 2026 · 第二作者**

- 提出几何多样性优化目标，将表征空间散度纳入长文本图像描述训练，缓解输出趋同和细节覆盖不足。
- 参与设计覆盖细节、多样性与事实一致性的多维评测协议，完成多基准实验与消融分析；方法可迁移至多模态大模型 RL 后训练（GRPO / RLVR）。

### 人类经验引导的无人机空战决策 · 2024.01 - 2025.03

**航天科工集团智能研究院 · 算法实习生 · IEEE SMC Magazine 第一作者已录用**

- 从 0 到 1 搭建 Harfang 3D + Dogfight2 人机混合空战平台，完成气动/碰撞解算、OpenAI Gym 封装、PyQt5 实验平台与 PPO/SAC 训练监控，覆盖 1v1 至 25v25 想定。
- 采集 2.7 小时、约 10 万时间步专家演示数据，用 GAIL 解决冷启动、PPO 做真实奖励微调，击杀率较 SOTA 提升 2.3 倍，交战耗时缩短 30%。
- 搭建 Isaac Lab 攻防想定、向量化并行环境与 Blender→USD 资产管线，完成 ACMI 2.2 遥测桥接与 Tacview 回放。

### 多智能体强化学习训练基础设施 · 2020.03 - 2022.03

**中国科学院自动化研究所 · 赵冬斌团队 · 算法实习生**

- 基于 Q-π 无关状态抽象设计 QIARL 表征学习算法，在 Procgen 多环境、多设定下完成 PyTorch / TensorFlow 双框架验证。
- 自研 learner-actor 并行采样架构并迁移到 Ray / RLlib，并行采样吞吐较单机提升一个数量级。
- 复现并适配 SMAC、pymarl/pymarl2、RLlib×SC2 与 MADDPG×MPE 等训练评测底座。

## 论文

- **[一作·已录用]** IEEE Systems, Man, and Cybernetics Magazine, 2026：*Human-Guided Autonomous Learning for UAV Air Combat Decision Optimization*
- **[一作·Under Review]** TNNLS：*Outcome-Supervised Prefix Value Models for Best-of-N Selection and Early Abandonment in Long-Horizon Coding Agents*
- **[二作]** ICML 2026：*Escaping the Likelihood Trap: Geometric Diversity Optimization for Long-Form Image Captioning*
- **[一作]** ICICIP 2021：*Learning Representation with Q-irrelevance Abstraction for Reinforcement Learning*
- **[合著]** IEEE Transactions on Cognitive and Developmental Systems, 2023：SCQRL；另在 Aerospace Science and Technology、Guidance, Navigation and Control 等期刊发表论文

## 竞赛与荣誉

- **NeurIPS 2020 AIcrowd Procgen 强化学习挑战赛**：负责算法研发、Ray/RLlib 训练框架改造、数据增强与 12 个环境超参搜索；第一轮 7/82，高校第一。
- **2023 空军“无人争锋”挑战赛 2V2 仿真赛**：优胜奖，非军事高校第一。

## 教育背景

- **北京航空航天大学**，自动化科学与电气工程学院，博士研究生，2022.09 - 至今
- **北京航空航天大学**，软件学院，硕士，2019.09 - 2021.12  
  北京市优秀毕业生 · 北航优秀研究生
- **北京理工大学**，光电学院，本科，2014.09 - 2018.06  
  优秀毕业论文 · 校级科技竞赛一等奖三项（第一作者）

<div align="center">
  <sub>关注大模型 Agent、RL 后训练、多智能体强化学习与生产级推理系统。</sub>
</div>
