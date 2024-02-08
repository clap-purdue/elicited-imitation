# Tutorial

**Prepare the dataset:**

- The dataset should be one folder that contains the audio files and a csv file that has two columns `audio` and `transcript`. Of course, the csv file can contain any other columns, but the `audio` and `transcript` columns should be present.

```bash
data/
   audio1.mp3
   audio2.mp3
   .
   .
   metadata.csv
```

```python
from ei.config import Config
from ei.japanese import ElicitedImitation
from ei.utils import plot
import os
```

**Prepare the configuration:**

- path to the audio dataset.
- name of the `csv` file.
- name of whisper checkpoint.
- name of the language.
- path to the output folder

```python
config = Config(path="~/Desktop/japanese", tsv_file="japanese-data.csv", checkpoint="openai/whisper-large-v3", language="ja", save_dir="~/Desktop")
```

**Intialize the `ElicitedImitation` class:**

```python
x = ElicitedImitation(config)
```

**Get the results:**

```python
z = x.get_ei_results()
```

**Plot results:**

```python
plot(z, config.save_dir)
```

**Save result to Excel file:**

```python
z.to_excel(os.path.join(config.save_dir, "NAME..xlsx"))
```
