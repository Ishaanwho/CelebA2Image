# 🎭 CelebA Conditional DCGAN

## Attribute-Guided AI Face Generation using PyTorch + Gradio

<div align="center">

Generate synthetic human faces using **semantic facial attributes** and natural language prompts.

Built with a **Conditional DCGAN**, trained on the **CelebA dataset**, and deployed through a futuristic interactive Gradio interface.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?style=for-the-badge\&logo=pytorch)
![Gradio](https://img.shields.io/badge/Gradio-WebUI-orange?style=for-the-badge)
![GAN](https://img.shields.io/badge/Model-Conditional%20DCGAN-purple?style=for-the-badge)

</div>

---

# 🌐 Live Demo

## 🚀 Hugging Face Space

👉 [Try the Live Demo](https://huggingface.co/spaces/isxhxan/CelebA?utm_source=chatgpt.com)

---

# 🧠 What This Project Actually Is

This project is **NOT** a large-scale diffusion-based text-to-image model like:

* Stable Diffusion
* Midjourney
* DALL·E

Instead, this is an:

# ✨ Attribute-Conditioned Face Synthesis System

Natural language prompts are first analyzed and converted into **facial attribute vectors**.

The GAN then generates faces conditioned on those extracted attributes.

---

# ⚙️ Example Workflow

### Input Prompt

```text
"young smiling person with glasses"
```

↓

### Parsed Attribute Vector

```python
[bangs=0, eyeglasses=1, no_beard=1, smiling=1, young=1]
```

↓

### Conditional DCGAN Generation

↓

### Synthetic Human Face Output

---

# 🎯 Why This Matters

Unlike unrestricted text-to-image systems, this approach:

* is lightweight
* interpretable
* controllable
* computationally cheaper
* easier to train
* easier to condition

The textual component acts as a **semantic interface** for attribute manipulation rather than open-domain image generation.

---

# ✨ Features

* 🧠 Natural language attribute parsing
* 🎭 Attribute-guided face synthesis
* ⚡ GPU accelerated inference
* 🖼️ Modern Gradio web GUI
* 🎨 Futuristic glassmorphism UI
* 🎲 Random seed reproducibility
* 📦 Batch generation support
* 💾 Download generated images
* 🔍 Attribute sliders and controls
* 🧩 Modular PyTorch architecture
* 🚀 Hugging Face Spaces deployment
* 📈 Future-ready semantic synthesis pipeline

---

# 🖼️ Example Prompts

```text
young smiling woman with bangs
man with glasses and no beard
happy young person
smiling person wearing glasses
elderly man with beard
```

---

# 🏗️ Model Architecture

## Conditional DCGAN

The generator receives:

* Random latent noise vector `z`
* Facial attribute conditioning vector

and outputs:

* Synthetic RGB facial image

---

# 🎭 Conditioning Attributes

| Attribute  | Description            |
| ---------- | ---------------------- |
| Bangs      | Hair/fringe visibility |
| Eyeglasses | Presence of eyewear    |
| No_Beard   | Beard intensity        |
| Smiling    | Smile intensity        |
| Young      | Age appearance         |

---

# 📊 Attribute Annotation Scale

## 🎀 Bangs

| Value | Description            |
| ----- | ---------------------- |
| 0     | No bangs               |
| 1     | Very short bangs       |
| 2     | Medium-short bangs     |
| 3     | Medium bangs           |
| 4     | Long bangs             |
| 5     | Full forehead coverage |

---

## 👓 Eyeglasses

| Value | Description           |
| ----- | --------------------- |
| 0     | No glasses            |
| 1     | Rimless / thin frames |
| 2     | Medium frames         |
| 3     | Thick plastic frames  |
| 4     | Thin sunglasses       |
| 5     | Thick sunglasses      |

---

## 🧔 No_Beard

| Value | Description        |
| ----- | ------------------ |
| 0     | Clean shave        |
| 1     | Light stubble      |
| 2     | Medium-short beard |
| 3     | Medium beard       |
| 4     | Groomed beard      |
| 5     | Large bushy beard  |

---

## 😄 Smiling

| Value | Description           |
| ----- | --------------------- |
| 0     | Neutral               |
| 1     | Slight smile          |
| 2     | Partial teeth visible |
| 3     | Full smile            |
| 4     | Large smile           |
| 5     | Wide open smile       |

---

## 🧑 Young

| Value | Description |
| ----- | ----------- |
| 0     | Child       |
| 1     | Teenager    |
| 2     | Young adult |
| 3     | Middle-aged |
| 4     | Aged        |
| 5     | Elderly     |

---

# 🧠 Prompt Parsing System

The application includes a lightweight semantic parser that maps language into attributes.

### Example mappings

| Keywords                 | Attribute    |
| ------------------------ | ------------ |
| bangs, fringe            | Bangs        |
| glasses, specs, eyewear  | Eyeglasses   |
| smiling, happy, grinning | Smiling      |
| young, youthful          | Young        |
| beard, facial hair       | No_Beard = 0 |

This creates an intuitive natural-language interface for controllable generation.

---

# ⚡ Inference Pipeline

```text
Text Prompt
      ↓
Semantic Attribute Parser
      ↓
Attribute Conditioning Vector
      ↓
Latent Noise Sampling
      ↓
Conditional DCGAN Generator
      ↓
64x64 Synthetic Face
      ↓
Optional Enhancement/Upscaling
      ↓
Final Output
```

---

# 🖥️ GUI Features

The Gradio interface includes:

* Prompt textbox
* Attribute sliders
* Batch generation
* Seed control
* Checkpoint selector
* GPU/CPU detection
* Image gallery
* Download support
* Modern animations
* Dark futuristic UI

---

# 📂 Dataset Structure

```bash
CelebA/
│
├── captions.json
├── request_annotated.json
├── request.json
├── request.txt
├── combined_annotation.txt
├── train_attr_list.txt
├── val_attr_list.txt
├── test_attr_list.txt
```

---

# 📁 Dataset Files

| File                      | Description                         |
| ------------------------- | ----------------------------------- |
| `captions.json`           | Image captions                      |
| `request_annotated.json`  | Editing requests with annotations   |
| `request.json`            | Editing requests in dictionary form |
| `request.txt`             | Plain text editing requests         |
| `combined_annotation.txt` | Full annotation dataset             |
| `train_attr_list.txt`     | Training annotations                |
| `val_attr_list.txt`       | Validation annotations              |
| `test_attr_list.txt`      | Test annotations                    |

---

# 🧪 Training Details

| Parameter     | Value             |
| ------------- | ----------------- |
| Architecture  | Conditional DCGAN |
| Framework     | PyTorch           |
| Dataset       | CelebA            |
| Resolution    | 64×64             |
| Optimizer     | Adam              |
| Loss Function | BCE Loss          |
| Conditioning  | Attribute vectors |

---

# 🚀 Running Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Launch Application

```bash
python app.py
```

---

# 📦 Example Requirements

```txt
torch
torchvision
gradio
numpy
pillow
matplotlib
```

---

# 🧪 Example Usage

```python
generate_face(
    prompt="young smiling woman with bangs",
    seed=42,
    batch_size=4
)
```

---

# 📈 Future Improvements

* Higher resolution synthesis
* Diffusion-assisted refinement
* Better semantic parsing
* Identity consistency
* Facial editing support
* Multi-attribute blending
* Real-ESRGAN integration
* GFPGAN enhancement pipeline
* LoRA fine-tuning
* Advanced textual synthesis analysis
* Improved semantic attribute extraction
* Full multimodal conditioning

---

# ⚠️ Current Limitations

* Limited attribute vocabulary
* 64×64 native output resolution
* Not open-domain text-to-image
* Dependent on CelebA attribute space
* Can struggle with uncommon combinations

---

# 🤝 Contributing

Contributions are welcome.

Feel free to:

* improve the architecture
* add new attributes
* enhance prompt understanding
* improve UI/UX
* optimize inference

---

# 📜 License

This project is intended for:

* AI research
* Educational purposes
* GAN experimentation
* Portfolio projects
* Deep learning demonstrations

---

# 👨‍💻 Author

Built by **Ishaan Singh**

---

<div align="center">

## ⭐ If you enjoyed this project, consider starring the repository!

</div>
