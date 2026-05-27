import torch
import torch.nn as nn

LATENT_DIM = 100


def weights_init(m):

    classname = m.__class__.__name__
    if 'Conv' in classname:
        nn.init.normal_(m.weight.data, 0.0, 0.02)
    elif 'BatchNorm' in classname:
        nn.init.normal_(m.weight.data, 1.0, 0.02)
        nn.init.constant_(m.bias.data, 0)


class Generator(nn.Module):
    
    def __init__(self, latent_dim, num_attributes):
        super().__init__()
        self.project = nn.Linear(latent_dim + num_attributes, 512 * 4 * 4)

        self.conv_blocks = nn.Sequential(
            nn.BatchNorm2d(512),

            # 4 → 8
            nn.ConvTranspose2d(512, 256, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(True),

            # 8 → 16
            nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(True),

            # 16 → 32
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(True),

            # 32 → 64  (output)
            nn.ConvTranspose2d(64, 3, kernel_size=4, stride=2, padding=1, bias=False),
            nn.Tanh()   # output in [-1, 1], matches Normalize([0.5],[0.5]) inversion
        )

    def forward(self, noise, attributes):
        x = torch.cat([noise, attributes], dim=1)  # (B, 105)
        x = self.project(x).view(-1, 512, 4, 4)    # (B, 512, 4, 4)
        return self.conv_blocks(x)                  # (B, 3, 64, 64)