<div align="center">
  <img src="./images/profile.jpg" alt="Profile photo" width="168" />
  <h1>Shuai Hao | Sergio Termann</h1>
  <p><strong>Algorithm Engineer | LLM Agents / Multimodal Post-training / Multi-Agent Reinforcement Learning</strong></p>
  <p>PhD Candidate, Beihang University · AI Team Lead</p>
  <p>
    <a href="mailto:shuaihao@buaa.edu.cn">Email</a> ·
    Beijing, China ·
    <a href="https://sergiotermann.github.io/SergioTermann/">Homepage</a> ·
    <a href="https://github.com/SergioTermann?tab=repositories">Repositories</a>
  </p>
</div>

## About

I build and evaluate learning agents, from reward design and model post-training to production inference. My work connects multimodal reinforcement learning, coding-agent value models, and deployed operations agents with reproducible training systems. I lead AI development at a startup while pursuing a PhD at Beihang University.

**Seeking an LLM agent post-training algorithm internship in Beijing. Available five days per week for six months.**

## Key Results

| Metric | Result |
| --- | --- |
| Production agent ticket-closure rate | +12.4% |
| Coding-agent Best-of-N selection | 0.926, approaching verifier oracle 0.931 |
| Inference-time early abandonment compute savings | ~15% with near-zero accuracy loss |
| Geo-RL Semantic Volume Score vs. LLaVA-1.5 7B MLE | 2.20 to 3.55 (+61%) |
| Air-combat reinforcement-learning kill rate | 2.3× over SOTA |

## Technical Stack

| Area | Methods & Tools |
| --- | --- |
| LLM & VLM post-training | RLVR / GRPO / GSPO, PPO, SFT / DPO, reward engineering, PRM / PVM, Best-of-N, set-level RL |
| Agent systems | Planner-Executor, hybrid RAG, function calling, MCP / A2A, context engineering, SWE-bench |
| Reinforcement learning | PPO / SAC / GAIL, multi-agent RL, Ray / RLlib, AReaL, TRL, LoRA |
| Inference & deployment | vLLM, Ollama, Xinference, Dify, GPU clusters, Isaac Sim / Isaac Lab, Harfang DogFight |

## Selected Projects

### Production Agent for Intelligent Operations · 2025 - Present

**Beijing Fengqi Shiyu Technology Co., Ltd. · Partner / AI Team Lead / Project Owner**

- Led a Planner-Executor architecture with hybrid RAG, function-calling tooling, and automatic failure-case recycling to build a data flywheel across collection, training, evaluation, deployment, and feedback.
- Trained a Qwen3-8B LoRA model with TRL GRPOTrainer + vLLM using RLVR/GRPO; built field-level reward scoring, Chinese-English equivalence checks, and reduced 9,215 training samples to 2,310 high-value examples.
- Improved slot extraction from 0.914 to 0.961 (+4.7 percentage points), with an 11-hour training run.
- Online impact: ticket closure rate +12.4%, first-fix success +8.7%, self-service diagnosis closure +18.5%; tool hallucination 6.8%→2.9%, TTFT P50 860ms→810ms; supported an investment from Tsinghua Lihe at an approximately RMB 40 million valuation.
- Decoupled volatile knowledge from model weights, introduced five data gates, DAPO dynamic sampling, and an SFT→GRPO curriculum, reducing iteration time from 1-2 days to under half a day.

### Process Value Modeling for Long-Horizon Coding Agents · 2026 - Present

**Prefix Value Model · First author · TNNLS under review**

- Learned success probabilities over observable process states using terminal outcome supervision only, supporting Best-of-N selection, inference-time early abandonment, and outcome predictability analysis.
- Achieved SWE-bench-Lite selection performance of 0.926±0.049, approaching a verifier oracle of 0.931 and exceeding majority voting at 0.826 and trajectory-level PRM at 0.901, with no extra test execution overhead.
- Early abandonment of low-success rollouts saved roughly 15% end-to-end inference compute with near-zero accuracy loss; terminal outcomes became reliably predictable by round 3, with AUC improving from 0.73 to 0.95.
- Built a vLLM trajectory-collection and tensor-parallel inference system for controllable 72B evaluation on dual 48GB GPUs; LoRA rejection-sampling fine-tuning improved single-pass repair success from 0.375 to 0.800.

### Geo-RL for Long-Form Image Captioning · 2024 - 2026

**ICML 2026 · Second author**

- Contributed to problem formulation, reward and credit-assignment design, implementation, set-level evaluation, and ablations for *Escaping the Likelihood Trap: Geometric Diversity Optimization for Long-Form Image Captioning*.
- Combined a CLIP-weighted RBF-DPP log-determinant reward with pairwise repulsion, image-text alignment, hallucination penalties, and a KL trust region. PPO balances semantic diversity with visual fidelity.
- Derived leave-one-out marginal advantages using a single Cholesky factorization to avoid repeated determinant computation.
- On DeCapBench, relative to LLaVA-1.5 7B MLE: **Distinct-2 0.66 to 0.84 (+27%)**, **Semantic Volume Score 2.20 to 3.55 (+61%)**, Self-BLEU 0.77 to 0.53, CLIPScore 0.74 to 0.81, and CHAIRi 8.3% to 7.1%.
- Evaluated component ablations, sampling and data scaling, and model sizes of 7B, 13B, and 34B parameters.

### Human-Guided Autonomous UAV Air Combat · Jan 2024 - Mar 2025

**Aerospace Science and Industry Intelligent Research Institute · Algorithm Intern · IEEE SMC Magazine first author accepted**

- Built a Harfang 3D + Dogfight2 human-machine combat platform from scratch, including aerodynamics/collision solving, OpenAI Gym wrappers, a PyQt5 experiment interface, and PPO/SAC training with TensorBoard monitoring across 1v1 to 25v25 scenarios.
- Collected 2.7 hours of expert demonstrations (~100k timesteps), used GAIL for cold-start imitation and PPO for real-reward fine-tuning, improving kill rate by 2.3x over SOTA and reducing engagement time by 30%.
- Built Isaac Lab attack-defense scenarios, vectorized parallel environments, a Blender→USD asset pipeline, ACMI 2.2 telemetry bridging, and Tacview replay.

### Multi-Agent RL Training Infrastructure · Mar 2020 - Mar 2022

**Institute of Automation, Chinese Academy of Sciences · Zhao Dongbin Group · Algorithm Intern**

- Designed QIARL representation learning with Q-irrelevance state abstraction and validated it across multiple Procgen environments and settings in both PyTorch and TensorFlow.
- Built a learner-actor parallel sampling architecture and migrated it to Ray/RLlib, increasing parallel sampling throughput by an order of magnitude over single-machine training.
- Reproduced and adapted SMAC, pymarl/pymarl2, RLlib×SC2, and MADDPG×MPE training and evaluation baselines.

## Publications

- **[First author · accepted]** IEEE Systems, Man, and Cybernetics Magazine, 2026: *Human-Guided Autonomous Learning for UAV Air Combat Decision Optimization*
- **[First author · under review]** TNNLS: *Outcome-Supervised Prefix Value Models for Best-of-N Selection and Early Abandonment in Long-Horizon Coding Agents*
- **[Second author]** ICML 2026: *Escaping the Likelihood Trap: Geometric Diversity Optimization for Long-Form Image Captioning*
- **[First author]** ICICIP 2021: *Learning Representation with Q-irrelevance Abstraction for Reinforcement Learning*
- **[Co-author]** IEEE Transactions on Cognitive and Developmental Systems, 2023: SCQRL; additional publications in Aerospace Science and Technology and Guidance, Navigation and Control

## Competitions & Honors

- **NeurIPS 2020 AIcrowd Procgen Reinforcement Learning Challenge**: led algorithm development, Ray/RLlib trainer modification, data augmentation, and hyperparameter search over 12 Procgen environments; 7th of 82 teams in Round 1 and first among universities.
- **2023 Air Force "Unmanned Swarm" Challenge, 2v2 simulation track**: Excellence Award, first among non-military universities.

## Education

- **Beihang University**, School of Automation Science and Electrical Engineering, PhD Candidate, Sep 2022 - Present
- **Beihang University**, School of Software, MEng, Sep 2019 - Dec 2021  
  Outstanding Graduate of Beijing · Outstanding Graduate Student of Beihang University
- **Beijing Institute of Technology**, School of Optics and Photonics, BEng, Sep 2014 - Jun 2018  
  Outstanding Undergraduate Thesis · Three first prizes in university science and technology competitions as first author

<div align="center">
  <sub>Focused on LLM agents, RL post-training, multi-agent reinforcement learning, and production inference systems.</sub>
</div>
