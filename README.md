# UFCFUR-15-3-Advanced-Artificial-Intelligence
## Bristol Regional Food Network (BRFN)

Project designed and developed by Zoe Haines (21033821) for the UFCFUR-15-3 Advanced Artificial Intelligence Module.
The system is an AI powered quality recognition system with a custom trained convolutional neural network (CNN) for
assessing the quality of fruits and vegetables.

## Getting Started

### Prerequisites
- Python 3.12.13
- Jupyter Notebook and/or JupyterLab
- Git LFS

#### Storage Space
This repository uses Git LFS to store a model trained using the jupyter notebook in this repo which is downloaded to be used as a default model for predictions
because of that it requires **~200MB of Storage Space** or you can train your own model by following the '**Building CNN**'
instructions in this README which requires **~5-6GB** for the dataset.  

### Github LFS
This repo exceeds Github max file size limiters and therefore it requires use of the Github LFS to pull the pre-trained model, either setup LFS or follow the '**Building CNN**' instructions.
For more information on Git LFS visit: https://git-lfs.com/. For Git LFS there is a preprovided ``.gitattributes`` file which automatically flags the correct files for LFS when pushing.

#### LFS first time setup
- Download Git LFS from your package manager (pacman, apt, etc) or from https://git-lfs.com/
- run ``git lfs install``

You can now pull (and push) the full contents of this repo.

If you're having issues with installing Git LFS I recommend the Github guide on the topic: https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage

### Installation

```bash
git clone https://github.com/goetic-zoe/UFCFUR-15-3-Advanced-Artificial-Intelligence.git
cd UFCFUR-15-3-Advanced-Artificial-Intelligence
pip install -r requirements.txt
```

### Running
#### Single Command
```bash
python prediction.py -m models/trained_fruit_cnn.keras <path-to-image>
```
``-m/--models`` can be used to point towards a different model using the same classes just replace ``models/trained_fruit_cnn.keras``
with your own model. To see the relevant classes open
``prediction.py`` in your editor and find variable ``dataset_classes``

#### Building CNN
From within the UFCFUR-15-3-Advanced-Artificial-Intelligence directory.
```bash
cd notebooks
jupyter notebook Fruit_CNN.ipynb
```
