# Title: A Deep Learning Method to Integrate extra-celluar miRNA with mRNA for cancer studies

## Initial Environment Setup (Python, R)

0. Linux and Windows systems are supported. Linux is recommended.
1. Install Python 3. We have tested with Python 3.12.3, 3.11.3, and 3.10.12. Python 2 is not supported.
2. Install R 4.4.0. We strongly recommend using version 4.4.0 only.
3. Make sure you can call python (using 'python', 'python3', or 'py' aliases) and Rscript from your terminal or command line.
4. Run setup_environment.sh (on linux) or setup_environment.bat (on Windows). Run setup_environment.sh using the following command on bash from the current directory.

```bash
    sh ./setup_environment.sh
```
5. Now you can run the model test codes or model training codes from the terminal/command line. The test and training codes include three cancer types: LC (Lung Cancer), BC (Breast Cancer), and GC (Gastric Cancer).

## Run: Model test codes

These test codes include all the result metrics and figures used in the manuscript. We have provided trained models and required data for the test codes to run independently. After running these test scripts, please look at the newly created html file for the results. 

If you require to run the training codes, please follow the ["Run: Model training codes"](#run-model-training-codes) section.

#### On linux: 
To run the test code type the following commands on a terminal.

##### LC test:
```bash
    source ./pythonEnv/bin/activate
    cd ./LC_allcodes
    runnb -t ./Output/LC_Test_Models.ipynb -a ./LC_Test_Models.ipynb
    jupyter nbconvert --to html ./Output/LC_Test_Models.ipynb
```
##### BC test:
```bash
    source ./pythonEnv/bin/activate
    cd ./BC_allcodes
    runnb -t ./Output/BC_Test_Models.ipynb -a ./BC_Test_Models.ipynb
    jupyter nbconvert --to html ./Output/BC_Test_Models.ipynb
```
##### GC test:
```bash
    source ./pythonEnv/bin/activate
    cd ./GC_allcodes
    runnb -t ./Output/GC_Test_Models.ipynb -a ./GC_Test_Models.ipynb
    jupyter nbconvert --to html ./Output/GC_Test_Models.ipynb
```

#### On Windows:
To run the test code type the following commands on a command line or CMD.

##### LC test:
```batch
    pythonEnv\Scripts\activate.bat
    cd LC_allcodes
    jupyter nbconvert --execute LC_Test_Models.ipynb --to html --output .\Output\LC_Test_Models.html
```
##### BC test:
```batch
    pythonEnv\Scripts\activate.bat
    cd BC_allcodes
    jupyter nbconvert --execute BC_Test_Models.ipynb --to html --output .\Output\BC_Test_Models.html
```
##### GC test:
```batch
    pythonEnv\Scripts\activate.bat
    cd GC_allcodes
    jupyter nbconvert --execute GC_Test_Models.ipynb --to html --output .\Output\GC_Test_Models.html
```

## Run: Model training codes

These training codes automatically download the datasets and generate the model checkpoint files for the test codes to run. Running these codes will overwrite the model checkpoint files and data required for the test codes to run.

First all the data needs to be downloaded. To download the data the following command should be run - 

```bash
    python setup_data.py
```


#### On linux: 
To run the test code type the following command on a terminal.

##### LC train:
```bash
    source ./pythonEnv/bin/activate
    cd ./LC_allcodes
    runnb -a ./LC_data_preprocess.ipynb
    runnb -a ./LC_Train_Models.ipynb
```
##### BC train:
```bash
    source ./pythonEnv/bin/activate
    cd ./BC_allcodes
    runnb -a ./BC_data_preprocess.ipynb
    runnb -a ./BC_Train_Models.ipynb
```
##### GC train:
```bash
    source ./pythonEnv/bin/activate
    cd ./GC_allcodes
    runnb -a ./GC_data_preprocess.ipynb
    runnb -a ./GC_Train_Models.ipynb
```

#### On Windows:
To run the test code type the following command on a command line or CMD.

##### LC train:
```batch
    pythonEnv\Scripts\activate.bat
    cd LC_allcodes
    jupyter nbconvert --execute LC_data_preprocess.ipynb --to html --output .\Output\LC_data_preprocess.html
    jupyter nbconvert --execute LC_Train_Models.ipynb --to html --output .\Output\LC_Train_Models.html
```
##### BC train:
```batch
    pythonEnv\Scripts\activate.bat
    cd BC_allcodes
    jupyter nbconvert --execute BC_data_preprocess.ipynb --to html --output .\Output\BC_data_preprocess.html
    jupyter nbconvert --execute BC_Train_Models.ipynb --to html --output .\Output\BC_Train_Models.html
```
##### GC train:
```batch
    pythonEnv\Scripts\activate.bat
    cd GC_allcodes
    jupyter nbconvert --execute GC_data_preprocess.ipynb --to html --output .\Output\GC_data_preprocess.html
    jupyter nbconvert --execute GC_Train_Models.ipynb --to html --output .\Output\GC_Train_Models.html
```
