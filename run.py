import hydra
from omegaconf import DictConfig
from src.utils import init_wandb

@hydra.main(config_path="configs", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
    if cfg.logging.enable_wandb:
        init_wandb(cfg)

    print("Hydra config loaded successfully.")
    print(cfg)

    # TODO: Add call to training loop here (e.g., train(cfg))

if __name__ == "__main__":
    main()