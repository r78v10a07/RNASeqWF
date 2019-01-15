# RNASeqWF

This project was designed to evaluate a Differential Gene Expression Analysis workflow following the same approach published in [Empirical assessment of analysis workflows for differential expression analysis of human samples using RNA-Seq]( https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-1457-z) by Williams _at al_.

We tested five workflows for the DGA. All workflows used the same aligner (STAR) and quantification (TPMCalculator) tool but different DGA software: EdgeR, Deseq2, SAMSeq, the union and the intercept off all identified genes from all DGA tools. Recall and precision values were calculated using the same approach described in the paper using the expressions: 

<img src="https://latex.codecogs.com/gif.latex?Recall = \frac{G_{r} \cup G_{d}}{G_{d}}" />

<img src="https://latex.codecogs.com/gif.latex?Precision = \frac{G_{r} \cup G_{d}}{G_{r}}" />

<img src="https://latex.codecogs.com/gif.latex?G_r" /> genes in reference and <img src="https://latex.codecogs.com/gif.latex?G_d" /> genes identified

We used paper's figure 5a to plot our results for comparison with the paper published results. Although, we obtained recall values under the fitted line our precision is over the fitting line showing better results  than those published in the paper, see final plots [here](./notebooks/00%20-%20Project%20Notes.ipynb#8.-Correlation-with-published-results). 

This analysis is testing the whole workflow STAR-TPMCalculator-DGA tool. In our case, we use the same tools than in the paper for alignment (STAR) and DGA (EdgeR, Deseq2 and SAMSeq). The only difference is the quantification step using TPMCalculator. Additionally, we used their scripts and parameters for the DGA tools which all are R packages. 

We see an increment of the precision despite of using the same first and last steps published in the paper for the STAR-quantification-DGA based workflows. We concluded that the increment in precision is due to the introduction of the TPMCalculator tool.

Our workflow is based on a set of Jupyter Notebooks and [CWL workflows](https://gitlab.com/r78v10a07/cwl-workflow/). The workflows excuted the analysis using the following tools: 

 * FastQC, for pre-processing quality control
 * Trimmomatic, for reads trimming
 * STAR, for reads alignment
 * RSeQC, for alignment quality control
 * TPMCalculator, for mRNA abundance quantification
 * Deseq2, for DGA
 * EdgeR, for DGA
 * SAMseq, for DGA

### Workflow  steps

 1. [Sample retrieval from SRA database](./notebooks/00%20-%20Project%20Notes.ipynb#1.-Sample-retrieval-from-SRA-database)
 2. [Pre-processing QC](./notebooks/00%20-%20Project%20Notes.ipynb#2.-Pre-processing-QC)
 3. [Trimming](./notebooks/00%20-%20Project%20Notes.ipynb#3.-Trimming)
 4. [Alignment](./notebooks/00%20-%20Project%20Notes.ipynb#4.-Alignment)
 5. [Alignment Quality Control](./notebooks/00%20-%20Project%20Notes.ipynb#5.-Alignment-QC)
 6. [Quantification](./notebooks/00%20-%20Project%20Notes.ipynb#6.-Quantification)
 7. [Differential Gene Expression Analysis](./notebooks/00%20-%20Project%20Notes.ipynb#7.-Differential-Gene-Expression-Analysis)
 8. [Correlation with published results](./notebooks/00%20-%20Project%20Notes.ipynb#8.-Correlation-with-published-results)
 
### Requirements

 1. [Python 3.6](./requirements/python3.6.txt)
 2. CWL Tools definition files: [cwl-workflow](https://gitlab.com/r78v10a07/cwl-workflow/) 
 