```text
project_name/
│
├── configs/                      # Hydra config files
│   ├── config.yaml               # Main config entry point
│   ├── model.yaml                # Model-related configs
│   ├── data.yaml                 # Dataset-related configs
│   ├── train.yaml                # Training args
│   └── logging.yaml              # W&B and logging config
│
├── src/                         # Core source code
│   ├── __init__.py
│   ├── data.py                  # Dataset loading & preprocessing
│   ├── model.py                 # Model logic or integration
│   ├── trainer.py               # Training loop 
│   ├── eval.py                  # Evaluation logic
│   └── utils.py                 # Helper functions (seed, logging, etc)
│
├── scripts/                     # Run scripts
│   ├── train.sh
│   └── evaluate.sh
│
├── run.py                       # Main training entrypoint (Hydra powered)
├── pyproject.toml               # Poetry-based dependency manager
├── .env                         # W&B keys, etc.
└── README.md                    # Project overview
```

# README.md

## 📘 Project Overview
This template provides a clean, modular starting point for **researchers** looking to train, finetune, or run ML experiments using Hydra, and Weights & Biases for configuration management.

It is framework-agnostic and works equally well for NLP, vision, tabular, or reinforcement learning tasks, can be integrated with Sklearn, PyTorch, Tensorflow or HuggingFace pipelines. 

---

## 📂 Directory Structure

- `configs/` – YAML config files managed by Hydra
- `src/` – Your actual code (data loading, model logic, training loop, etc.)
- `scripts/` – Shell scripts to launch training/evaluation easily
- `run.py` – Entrypoint to your training job
- `.env` – W&B and private environment variables

---

## 🔧 Features

- ✅ Modular Hydra configs (switch model/data/train settings easily)
- ✅ Native Weights & Biases logging integration
- ✅ Customizable training loop for any ML task (NLP, CV, tabular, etc.)
- ✅ Clean separation between data, model, and training logic
- ✅ Poetry-powered reproducible environment

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone <this-template-url> my_project
cd my_project
```

### 2. Install dependencies
```bash
poetry install
```

### 3. Set up environment variables
Add your W&B API key to `.env`:
```bash
WANDB_API_KEY=your-key-here
```

### 4. Run training
```bash
python run.py
```

To override a config:
```bash
python run.py train.batch_size=8 model.name=my_model_v1
```

---

## 🛠️ Todo (for you to implement)
- Fill in `src/data.py` with your dataset logic
- Define your model architecture in `src/model.py`
- Implement training steps inside `src/trainer.py`
- Add evaluation code in `src/eval.py`

---

## ✍️ Author
Built for individual ML researchers who want structure without boilerplate.

Feel free to fork and adapt!
