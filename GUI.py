import gradio as gr
import torch
import numpy as np

from PIL import Image

from Models.generator import Generator

LATENT_DIM = 100

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


G = Generator(LATENT_DIM, 5).to(device)

checkpoint = torch.load(
    "checkpoints/cgan_epoch_020.pth",
    map_location=device
)

G.load_state_dict(checkpoint['G_state'])

G.eval()

print("Generator loaded successfully.")


@torch.no_grad()
def generate_face(
    bangs,
    eyeglasses,
    no_beard,
    smiling,
    young,
    num_samples
):

    attrs = torch.tensor(
        [[
            bangs,
            eyeglasses,
            no_beard,
            smiling,
            young
        ]] * num_samples,

        dtype=torch.float32,
        device=device
    )

    noise = torch.randn(
        num_samples,
        LATENT_DIM,
        device=device
    )

    fake_imgs = G(noise, attrs)

    fake_imgs = ((fake_imgs + 1) / 2).clamp(0, 1)

    fake_imgs = (
        fake_imgs
        .cpu()
        .permute(0, 2, 3, 1)
        .numpy()
    )

    images = []

    for img in fake_imgs:

        img = (img * 255).astype(np.uint8)

        pil_img = Image.fromarray(img)

        images.append(pil_img)

    return images

# =====================================================
# GUI
# =====================================================

with gr.Blocks() as demo:

    gr.Markdown("# NeuralFace AI")

    with gr.Row():

        with gr.Column():

            bangs = gr.Slider(
                0, 1,
                value=0,
                step=0.1,
                label="Bangs"
            )

            eyeglasses = gr.Slider(
                0, 1,
                value=0,
                step=0.1,
                label="Eyeglasses"
            )

            no_beard = gr.Slider(
                0, 1,
                value=1,
                step=0.1,
                label="No Beard"
            )

            smiling = gr.Slider(
                0, 1,
                value=1,
                step=0.1,
                label="Smiling"
            )

            young = gr.Slider(
                0, 1,
                value=1,
                step=0.1,
                label="Young"
            )

            num_samples = gr.Slider(
                1, 8,
                value=4,
                step=1,
                label="Images"
            )

            generate_btn = gr.Button(
                "Generate Faces"
            )

        with gr.Column():

            gallery = gr.Gallery(
                label="Generated Faces",
                columns=2
            )

    generate_btn.click(
        fn=generate_face,

        inputs=[
            bangs,
            eyeglasses,
            no_beard,
            smiling,
            young,
            num_samples
        ],

        outputs=gallery
    )

# LAUNCH
demo.launch(
    inbrowser=True,
    share=True
)