**NeMo Text Processing**
==========================

Introduction
------------

`nemo-text-processing` is a Python package for text normalization and inverse text normalization.

Documentation
-------------

[NeMo-text-processing (text normalization and inverse text normalization)](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/nlp/text_normalization/intro.html).

Tutorials
-----------------

| Google Collab Notebook      | Description |
| ----------- | ----------- |
| [Text_(Inverse)_Normalization.ipynb](https://github.com/NVIDIA/NeMo-text-processing/blob/main/tutorials/Text_(Inverse)_Normalization.ipynb)     | Quick-start guide       |
| [WFST_Tutorial](https://github.com/NVIDIA/NeMo-text-processing/blob/main/tutorials/WFST_Tutorial.ipynb)   | In-depth tutorial on grammar customization        |


Getting help
--------------
If you have a question which is not answered in the [Github discussions](https://github.com/NVIDIA/NeMo-text-processing/discussions), encounter a bug or have a feature request, please create a [Github issue](https://github.com/NVIDIA/NeMo-text-processing/issues). We also welcome you to directly open a [pull request](https://github.com/NVIDIA/NeMo-text-processing/pulls) to fix a bug or add a feature.


Installation
------------

### Conda virtual environment

We recommend setting up a fresh Conda environment to install NeMo-text-processing.

```bash
conda create --name nemo_tn python==3.10
conda activate nemo_tn
```

(Optional) To use [hybrid text normalization](nemo_text_processing/hybrid/README.md) install PyTorch using their [configurator](https://pytorch.org/get-started/locally/). 

```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```
**_NOTE:_** The command used to install PyTorch may depend on your system.


###  Pip

Use this installation mode if you want the latest released version.
```
pip install nemo_text_processing
```

**_NOTE:_** This should work on any Linux OS with x86_64. Pip installation on MacOS and Windows are not supported due to the dependency [Pynini](https://www.openfst.org/twiki/bin/view/GRM/Pynini). On a platform other than Linux x86_64, installing from Pip tries to compile Pynini from scratch, and requires OpenFst headers and libraries to be in the expected place. So if it's working for you, it's because you happen to have installed OpenFst in the right way in the right place. So if you want to Pip install Pynini on MacOS, you have to have pre-compiled and pre-installed OpenFst. The Pynini README for that version should tell you which version it needs and what `--enable-foo` flags to use.
Instead, we recommend you to use conda-forge to install Pynini on MacOS or Windows:
`conda install -c conda-forge pynini=2.1.6.post1`.


###  Pip from source

Use this installation mode if you want the a version from particular GitHub branch (e.g main).

```
pip install Cython
python -m pip install git+https://github.com/NVIDIA/NeMo-text-processing.git@{BRANCH}#egg=nemo_text_processing
```


### From source

Use this installation mode if you are contributing to NeMo-text-processing.

```
git clone https://github.com/NVIDIA/NeMo-text-processing
cd NeMo-text-processing
./reinstall.sh
```

**_NOTE:_** If you only want the toolkit without additional conda-based dependencies, you may replace ``reinstall.sh`` with ``pip install -e .`` with the NeMo-text-processing root directory as your current working director.


### Using uv from source

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then create and activate a virtual environment from the repository root:

```bash
uv venv --python 3.10
source .venv/bin/activate
```

#### Run the package

Install the package and its runtime dependencies in editable mode, then normalize a sample input:

```bash
uv pip install -e .
python -m nemo_text_processing.text_normalization.normalize --text "12 kg"
```

Editable mode picks up changes to the Python source without reinstalling the package.

By default, the command without setting `cache_dir` option indicates `cache_dir=None`, the grammar far files are BUILT IN MEMORY AND DISCARDED when the command finishes.

##### Run with cache
```
python -m nemo_text_processing.text_normalization.normalize \
  --language en \
  --input_case cased \
  --cache_dir .cache/nemo_grammars \
  --text 'the price is $1,234.'
```

The first run will save the grammar `.far` files under the `.cache.nemo_grammars` folder; later runs load matching files from that directory. 

> After changing the grammar code or the `related .tsv` data,  
> we can add `--overwrite_cache` option to overwrite the stale grammar.
> ```
> python -m nemo_text_processing.text_normalization.normalize \
>   --language en \
>   --input_case cased \
>   --cache_dir .cache/nemo_grammars \
>   --overwrite_cache \
>   --text 'the price is $1,234.'
> ```


#### Run the tests

Install the package with its `test` extra, then run the suite on CPU:

```bash
uv pip install -e ".[test]"
# run all the testings
python -m pytest --cpu --tn_cache_dir=.cache/nemo_grammars
# run a single testing
python -m pytest --cpu --tn_cache_dir=.cache/nemo_grammars tests/nemo_text_processing/en/test_whitelist.py
```

Installing `.[test]` installs the runtime dependencies plus the packages in `requirements/requirements_test.txt`, so you can use this command directly after creating the environment.

Both commands use the same cache, and `.cache` is ignored by Git. Different languages and input settings need their own grammar files, so the full suite may still take time on its first run.

#### Why `uv pip install`?

`setup.py` reads the runtime and test dependencies from the files in `requirements/`. The current `pyproject.toml` only selects setuptools as the build backend. `uv pip install -e` installs the package through this EXISTING SETUP. `uv add` writes dependencies into `pyproject.toml` and updates a uv lockfile and environment. Using `uv add -r` here would copy the requirements into `pyproject.toml`, leaving two places to maintain them. Use `uv add` when migrating the project's dependency declarations to uv.

The Pynini platform requirements described in the Pip section apply to uv installs as well.


Contributing
------------
We welcome community contributions! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.



Citation
--------

```
@inproceedings{zhang21ja_interspeech,
  author={Yang Zhang and Evelina Bakhturina and Boris Ginsburg},
  title={{NeMo (Inverse) Text Normalization: From Development to Production}},
  year=2021,
  booktitle={Proc. Interspeech 2021},
  pages={4857--4859}
}

@inproceedings{bakhturina22_interspeech,
  author={Evelina Bakhturina and Yang Zhang and Boris Ginsburg},
  title={{Shallow Fusion of Weighted Finite-State Transducer and Language Model for
Text Normalization}},
  year=2022,
  booktitle={Proc. Interspeech 2022}
}
```

License
-------
NeMo-text-processing is under [Apache 2.0 license](LICENSE).
