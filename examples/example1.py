from ei.config import Config
from ei.japanese import ElicitedImitation
from ei.utils import plot
import os


if __name__ == '__main__':
    # Configure the pipeline by choosing the following:
    # 1) path to the dataset directory
    # 2) name of the csv file
    # 3) name of the whisper speech model
    # 4) name of the language(i.e., "ja")
    # 5) path to the output directory
    config = Config(
        path="~/Desktop/japanese", 
        tsv_file="japanese-data.csv", 
        checkpoint="openai/whisper-large-v3", 
        language="ja", 
        save_dir="~/Desktop"
        )
    # Declare the elicited imitation class
    x = ElicitedImitation(config)
    # Get results(if the data is big, you will need to wait until the speech engine gets the transcripts)
    z = x.get_ei_results()
    # plot your results (Optional step)
    plot(z, config.save_dir)
    # Save to an excel file
    z.to_excel(os.path.join(config.save_dir, "NAME..xlsx"))
