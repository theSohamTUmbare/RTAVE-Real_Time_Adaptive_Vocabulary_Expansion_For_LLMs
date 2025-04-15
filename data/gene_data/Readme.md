### Dataset Introduction

The dataset contains 18,092 samples in total. Each sample contains a term ID, term name, the related genes with alias and descriptions.  We randomly shuffled all the term. And split them into 14474 training, 1809 validation and 1809 test samples with rate of 8:1:1. 

**term_gene_map.txt** are already shuffled. Line 1-14474, line 14475-16283 and line 16284-18092 are training set, validation set, and test set respectively. 



File **term_gene_map.txt** contains term ID and related gene ID,

Format: [term ID] \t [gene ID 1] \t [gene ID 2] \t …

Sample: 0031981	INSR	MLIP	NARF	SYNE2



File **term_id_name.txt** contains term ID and term name,

Format: [term ID] \t [term name]

Sample: 0031981  nuclear lumen



File **gene_alias_description.txt** contains gene ID, gene alias and gene description,

Format: [gene ID] \t [gene alias] \t [gene description]

Sample: 

INSR	Insulin Receptor	This gene encodes a member of the receptor  ......

MLIP	Muscular LMNA Interacting Protein	Required for precocious cardiac adaptation to ......

NARF	Nuclear Prelamin A Recognition Factor	Several proteins have been found to be ......

SYNE2	Spectrin Repeat Containing Nuclear Envelope Protein 2	The protein encoded by this gene is a nuclear  ......



According to the above sample of GO term 0031981, we would use those four gene aliases and four gene descriptions to predict the GO term name: nuclear lumen.





