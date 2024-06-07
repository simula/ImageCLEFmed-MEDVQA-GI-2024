# ImageCLEFmed-MEDVQA-GI-2024
The MEDVQA-GI challenge is held for the second time this year with a new goal. One of the new frontiers in AI-driven medical diagnosis is the application of text-to-image generative models. This area integrates language processing and image synthesis to enhance diagnostic capability in the medical field. In this task, we aim to direct the power of artificial intelligence to generate medical images based on text input, along with optimal prompts for off-the-shelf generative models building up on the dataset collected in the first edition of MEDVQA-GI. The objective is to improve the diagnosis and classification of real medical images using AI-generated imagery. The task is divided into two main subtasks


## Task Descriptions

### Image Synthesis (IS)
The first subtask, Image Synthesis (IS), requires participants to leverage text-to-image generative models to create a rich dataset of medical images derived from textual prompts. Examples include creating images of different pathologies based on text descriptions. For instance, given a textual description like "An early-stage colorectal polyp”, the participants should generate an image that closely represents the textual description.

### Optimal Prompt Generation (OPG)
The second subtask, Optimal Prompt Generation (OPG), requires generating optimal textual prompts that could guide an off-the-shelf generative model in creating realistic medical images. These images can range from imaging modalities such as magnetic resonance imaging, CT scans, to endoscopic images of various medical conditions. Given an off-the-shelf generative model and a medical condition, such as "late stage stomach ulcer," participants must generate an optimal textual prompt that would guide the model to produce the most accurate and realistic image of the condition.

## Data
* The development dataset can be found here: https://drive.google.com/file/d/1bZ27-A3RLTYot65swbtu0A3p4O9Asp0-/view?u...
* The testing dataset containing the prompts that should be used to generate the dataset for Task 1 can be found here: https://drive.google.com/file/d/1WGmSUHog2-vTlu0hKx97jVL8VZwQI06J

## Evaluation methodology
The evaluation of these subtasks will be based on a subjective evaluation done by a committee and how accurately a model trained on these AI-generated images can classify real medical images. This will further be analyzed on both single-center and multi-center datasets, providing a comprehensive analysis of the model's performance. Metrics we will use for the task are Fréchet Inception Distance (FID) and standard classification metrics like accuracy, precision, recall, and F1 score on both single-center and multi-center datasets. In addition, the robustness of the model across different centers, representing the model's generalisation capabilities, will also be evaluated.

## Participant registration
Please refer to the general ImageCLEF registration instructions: [https://www.imageclef.org/2024](https://www.imageclef.org/2024).

# Submission Instructions

**Task 1: Image Synthesis**
Please submit the images you have generated based on the prompts we provided.

**Task 2: Optimal Prompt Generation**
For this task, you are required to submit both the prompts and the models you have used to generate images. Please organize your submissions by category for our ease of evaluation. 

**Submission Instructions:**
Please email your submissions directly to steven@simula.no.

# Paper Submission
Working note papers should describe your aproach and results. Below you will find submission instructiosn, a Latex template for the working notes, and CEUR-WS Copyright form that is **required** if your paper is to get published.

* [Instructions for Authors (PDF)](https://clef2024.imag.fr/publication_instructions/07-working-notes-instructions.pdf)
* [Latex Template (download .zip)](https://clef2024.imag.fr/publication_instructions/CLEF2024-CEUR-template-latex.zip)
* [CEUR-WS Copyright Form](https://clef2024.imag.fr/publication_instructions/AUTHOR-AGREEMENT.pdf)

## Citation
Please add these citations to you paper:

```
@inproceedings{ImageCLEFmedicalVQAOverview2023,
	title = {Overview of ImageCLEFmedical 2024 – Medical Visual Question Answering for Gastrointestinal Tract},
	author = {Hicks, Steven A. and Storås, Andrea and Halvorsen, Pål and Riegler, Michael A. and Thambawita, Vajira},
	year = 2024,
	month = {September},
	booktitle = {CLEF2024 Working Notes},
	publisher = {CEUR-WS.org},
	address = {Grenoble, France},
	series = {{CEUR} Workshop Proceedings}
}
@inproceedings{ImageCLEFmedicalVQAOverview2023,
	title = {Overview of ImageCLEFmedical 2023 – Medical Visual Question Answering for Gastrointestinal Tract},
	author = {Hicks, Steven A. and Storås, Andrea and Halvorsen, Pål and de Lange, Thomas and Riegler, Michael A. and Thambawita, Vajira},
	year = 2023,
	month = {September},
	booktitle = {CLEF2023 Working Notes},
	publisher = {CEUR-WS.org},
	address = {Thessaloniki, Greece},
	series = {{CEUR} Workshop Proceedings}
}
@article{borgli2020hyperkvasir,
	title = {HyperKvasir, a comprehensive multi-class image and video dataset for gastrointestinal endoscopy},
	author = {Borgli, Hanna and Thambawita, Vajira and Smedsrud, Pia H and Hicks, Steven and Jha, Debesh and Eskeland, Sigrun L and Randel, Kristin Ranheim and Pogorelov, Konstantin and Lux, Mathias and Nguyen, Duc Tien Dang and others},
	year = 2020,
	journal = {Scientific data},
	volume = 7,
	number = 1,
	doi = {10.1038/s41597-020-00622-y}
}
@inproceedings{kvasir-instruments,
	title = {{Kvasir-Instrument: Diagnostic and Therapeutic Tool Segmentation Dataset in Gastrointestinal Endoscopy}},
	author = {Jha, Debesh and Ali, Sharib and Emanuelsen, Krister and Hicks, Steven A. and Thambawita, Vajira and Garcia-Ceja, Enrique and Riegler, Michael A. and de Lange, Thomas and Schmidt, Peter T. and Johansen, H{\aa}vard D. and Johansen, Dag and Halvorsen, P{\aa}l},
	year = 2021,
	booktitle = {Proceedings of the International Conference on MultiMedia Modeling (MMM)},
	pages = {218--229},
	url = {https://doi.org/10.1007/978-3-030-67835-7_19}
}
@inproceedings{jha2023gastrovision,
	title = {GastroVision: A Multi-class Endoscopy Image Dataset for Computer Aided Gastrointestinal Disease Detection},
	author = {Debesh Jha*, Vanshali Sharma*, Neethi Dasu, Nikhil Kumar Tomar, Steven Hicks, M.K. Bhuyan, Pradip K. Das, Michael A. Riegler, P{\aa}l Halvorsen, Thomas de Lange, Ulas Bagci},
	year = 2023,
	booktitle = {ICML Workshop on Machine Learning for Multimodal Healthcare Data (ML4MHD 2023)}
}
```

## Preliminary Schedule
* 30.11.2023: registration opens for all ImageCLEF tasks
* 22.04.2024: registration closes for all ImageCLEF tasks
* 01.02.2024: Release of the training and validation sets
* 03.04.2024: Release of the test sets
* 06.05.2024 : deadline for submitting the participants runs
* 13.05.2024 : release of the processed results by the task organizers
* 31.05.2024 : deadline for submission of working notes papers by the participants
* 21.06.2024: notification of acceptance of the working notes papers
* 08.07.2024 : camera ready working notes papers
* 09-12.09.2024: CLEF 2024, Grenoble, France

## Organizers
* Steven A. Hicks <steven(at)simula.no>, SimulaMet, Norway
* Michael A. Riegler <michael(at)simula.no>, SimulaMet, Norway
* Vajira Thambawita  <vajira(at)simula.no>, SimulaMet, Norway
* Andrea Storås <andrea(at)simula.no>, SimulaMet, Norway
* Pål Halvorsen <paalh(at)simula.no>, SimulaMet, Norway
