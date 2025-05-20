import hydra
from omegaconf import DictConfig
from src.utils import init_wandb
from src import trainer, eval

@hydra.main(config_path="configs", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
    if cfg.logging.enable_wandb:
        init_wandb(cfg)

    if cfg.mode == "train":
        ## TODO: Add training loop here
        print("Training...")
    elif cfg.mode == "eval":
        ## TODO: Add evaluation loop here
        print("Evaluating...")
    else:
        raise ValueError(f"Unsupported mode: {cfg.mode}")

if __name__ == "__main__":
    main()