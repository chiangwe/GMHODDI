# GMHODDI
Paper is accepted in ICIBM 2018.

# Datasets:
Datasets used for this project are from FDA Adverse Event Reporting System. 
(FAERS https://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm)
Final drug combinations after our data preparation protocols are available in the folder "Dataset."
In all the dataset, each row represents a drug combination and each number in a given row represents the ID of the drug that the combination contains. The mapping of drug IDs and drug names can be found in "GMHODDI/Dataset/FAERS_Dataset/drug_maps.txt."  

Dataset descriptions as follows:
  1. "GMHODDI/Dataset/FAERS_Dataset/" contains the extracted adverse events including those that are reported to have myopathy (myopathy_ho_events.txt) and those that are not (nonmyopathy_ho_events.txt).
  2. "GMHODDI/Dataset/D_FAERS/" contains the extracted drug combinations, where the label can be found in "DFaers_label.csr."
  3. "GMHODDI/Dataset/D_star/" contains the drug combinations after being selected by our training data preparation protocols for model training and cross-validation.
  4. "GMHODDI/Dataset/D_star/CoMed_Feature/" contains the features used to calculate the single drug similarities based on co-medications. Note that there are five set of features corresponding to five cross-validation. 
  5. "GMHODDI/Dataset/D_star/Tesing/" and "GMHODDI/Dataset/D_star/Training/" contain the split drug combination for five cross-validation.
  
# SDS
"GMHODDI/SDS/Sim_2d/" and "GMHODDI/SDS/Sim_cm/" contain the single drug similarities that we used to calculate different kernels.
"Sim_2d" is the SDSs based on 2d structures and "Sim_cm" is the proposed SDSs based on co-medications. 

# Framework 
We used SVMlight as the framework for our binary classification problem. 
Specifically, we proposed a graph matching based kernel based on co-medication information and we use SVMlight to conduct the experiments.
Detailed explanations of how to use this method are available at SVMlight homepage.
(SVMlight http://svmlight.joachims.org/)

Pre-compiled binary files (svm_learn and svm_classify) with self-defined kernel are available in folder "SVM_light_file." 
Instructions on usage are available at the original author's homepage. 
You are also free to use other kernels. Instructions are also available at the original author's homepage. 

# Implementation 

##########################
Drug-Drug Interaction Prediction based on Co-Medication Patterns and Graph Matching
Last modify: 04/18/2018
Author: Wen-Hao Chiang
##########################

##########################
General information
##########################
This code provides how to calculate the proposed kernels based on graph matching and other kernels for baseline methods.
For probabilistic drug combination kernels, please visit the original author's website at https://sites.google.com/site/skevinzhou/codes.
For usage of svm_learn and svm_classify, please visit the original author's website at http://svmlight.joachims.org.

##########################
Code Information
##########################

"Kernel_GraphMatching.py" is to calculate the similarity between drug combinations based on graph matching (K_gm). 
"Kernel_DrugSimilarity.py" is a baseline method to calculate the similarity between drug combinations based on drug similarity (K_ds).
"Kernel_CommonDrugs.py" is a baseline method to calculate the similarity between drug combinations based on common drugs (K_cd).
"SDS_CoMed.py" is to calculate the single drug similarity base on co-medication information. 

##########################
Input
##########################

There three types of inputs.
1). Single drug similarity: it is provided as a dense matrix. Each line is a row in the matrix and each number in a line corresponds to each column in the matrix.
2). Drug combination: it is provided as a CSR format. Each line is a drug combination and each number in a line corresponds to drugs that the combination contains.
3). Co-medication features: it is provided as a dense matrix. Each line is a row in the matrix and each number in a line corresponds to each column in the matrix.

"Kernel_GraphMatching.py", "Kernel_DrugSimilarity.py" and "Kernel_CommonDrugs.py" take inputs of single drug similarity and drug combianation.
"SDS_CoMed.py" takes the input of co-medication features.

##########################
Usage
##########################

Please download all files in the code directory, including all *.py files, two executables (svm_learn and svm_classify) and kernel.h.
For the executables, we have provided a pre-compiled version with Tanimoto kernel. 
You are free to compile with your preferred kernel from the original author's website at http://svmlight.joachims.org.

The kernels used in the paper is provided in the following link due to the space limits of Github. 
https://cs.iupui.edu/~chiangwe/GMHODDI/Kernel/
The single drug similarities used in the paper is also provided in the folder "/GMHODDI."
The co-medication features used in the paper is also provided in the folder "/GMHODDI/Dataset/D_star/CoMed_Feature/."

The following *.py return the similarities between drug combinations by different methods. 
The following instructions explain the usage of code: 
- Kernel_GraphMatching.py:
-- Graph matching similarity: calculate drug combination similarities by graph matching and given single drug similarity.
--- command:
---- python Kernel_GraphMatching.py ./SDS_path ./DrugComb_path ./Output_path
--- parameters:
---- ./SDS_path: (string) path to file of single drug similarities 
---- ./DrugComb_path: (string) path to file of durg combinations
---- ./Output_path: (string) path to output locations
        
  - Kernel_DrugSimilarity.py:
        - Convolutional kernels: calculate drug combination similarities from average pairwise single drug similarities.
            - command:
                python Kernel_DrugSimilarity.py ./SDS_path ./DrugComb_path ./Output_path
            - parameters:
                - ./SDS_path: (string) path to file of single drug similarities 
                - ./DrugComb_path: (string) path to file of durg combinations
        - ./Output_path: (string) path to output locations
        
   - Kernel_CommonDrugs.py:
        - Common drugs: calculate drug combination similarities from Tanimoto coefficients.
              - command:
                python Kernel_CommonDrugs.py order ./DrugComb_path ./Output_path
              - parameters:
                - ./SDS_path: (string) path to file of single drug similarities 
                - ./DrugComb_path: (string) path to file of durg combinations
              - ./Output_path: (string) path to output locations
        
   - SDS_CoMed.py:
        - Common drugs: calculate single drug similarities from co-medication features.
              - command:
                python SDS_CoMed.py ./CoMed_Feature_Plus_path ./CoMed_Feature_Minus_path ./Output_path
              - parameters:
                - ./CoMed_Feature_Plus_path: (string) path to file of co-medication features calculated from case events.
                - ./CoMed_Feature_Minus_path: (string) path to file of co-medication features calculated from control events.
              - ./Output_path: (string) path to output locations
    

##########################
Comments and Bug Reports
##########################

Any kind of comments, suggestions, or bug reports are welcome and appreciated.
Please feel free to contact the author: chiangwe AT iupui DOT edu.


# Paper availability 
The paper is accepted in ICIBM 2018 and will be published in a special issue at International Journal of Computational Biology and Drug Design.
