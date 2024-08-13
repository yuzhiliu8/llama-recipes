import fire
import os
from datasets import load_dataset



def main(DATASET="yuzhiliu8/Multilingual-orig", config_name="train", split="sw_train", lang="sw", save_path="data"):
    print(DATASET, split, lang)
    dataset = load_dataset(DATASET, config_name, split='sw_train', streaming=True)
    os.makedirs(save_path, exist_ok=True)
    with open(os.path.join(save_path, f"{lang}.txt"), "w") as file:
        count = 0
        for row in dataset:
            if (row['Text'] is None):
                count += 1
            else:
                file.write(row['Text'] + '\n')
        print("bad rows:", count)

        


if __name__ == "__main__":
    fire.Fire(main)