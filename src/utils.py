import wandb

def init_wandb(cfg):
    wandb.init(
        project=cfg.logging.project,
        name=cfg.logging.run_name,
        config=cfg,
        mode="online" if cfg.logging.enable_wandb else "disabled"
    )
