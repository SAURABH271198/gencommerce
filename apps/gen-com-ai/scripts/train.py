import torch

def train():
    model = torch.nn.Linear(10, 1)  # Example model
    torch.save(model, "models/model.pth")

if __name__ == "__main__":
    train()
