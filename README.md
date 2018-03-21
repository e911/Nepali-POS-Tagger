# Nepali-POS-Tagger
# A part-of-speech tagger for Nepali language in python using Trigram'n Tags (TNT) . A second order HMM.
[Read about TNT](http://www.coli.uni-saarland.de/~thorsten/publications/Brants-ANLP00.pdf)

## Running the pos tagger
python3 main.py
(the input sentence must be in Nepali unicode font)
(any other fonts/languages input will be wrongly tagged)

Remove the dictionary/ folder and its components first after cloning the project. It contains the trained dataset 
trained form a sample put in the folder tagset/cs
The training dataset format/example is given in tagset/cs folder.  It is a .xml file
The sample was obtained from database of NELRAREC.

For full dataset contact NELRAREC and Bhasa Sansar authorities.
The obtaines files are to be put into the tagset/cs drectories.
OR as per you want so as along as you give the correct path for the
dataset folder in the file get_data.py
    NEPALI_CORPUS_DIR = './tagset/cs' (currently)
or  NEPALI_CORPUS_DIR = '(the path for the dataset folder)'

## Running the tagger after obtaining full dataset
(Important: Delete the dictionary/ folder and its components. As of now it has the trained set of the current sample of tagset/cs file
in the repo)
(The dictionary/ folder will itself be created later on)
Run in command line:
   python main.py
(The dictionary folder will be created automatically)
(If you have a new dataset, delete the previously created dictionary/ folder)

## Testing the tagger
python3 test.py
(You can chose a specific tagged file form the dataset to test)

## Training the tagger
pip install -r requirements.txt

python3 train_tagger.py
(This is still on todo list . It is for training the dataset using the given HMM algorithn(tnt_tagger) defined in nltk package)


A brief description about Neplai POS and tags definition as given by NELRAREC is given in the .pdf document.
 
