# BA3-SNPS-autotune
## Description:
This program will automatically tune mixing parameters for BA3-SNPs by conducting a 

## Installation & Setup:

This pipeline was written to be run on Unix based operating systems, such as the various Linux distributions and Mac OS X.  To get started, clone this project to the desired location on your computer.  

You may have to modify the first line of the BA3-SNPS-autotune.py file, which by default reads:
```
#!/usr/bin/env Python
```
To find the location of your Python installation, you can type the following at the bash command prompt:
```
which python
```
Then modify the first line of BA3-SNPS-autotune.py to reflect the location of your Python installation.

## Running the program:

You can run the program to print help options with the following command:

```
./BA3-SNPS-autotune.py -h
```

List of current required options:
* **-i / --immanc:** Specify an immanc-formatted file that will be passed by the program to BA3-SNPS.
* **-l / --loci:** Specify the number of loci in the input file.

Optional arguments:
* **-b / --burnin:** Specify the number of generations to be discarded as burnin by BA3-SNPS.  (Default = 1,000 generations)
* **-g / --generations:** Specify the number of generations for each BA3-SNPS run.  (Default = 10,000 generations)
* **-o / --out:** Specify an output file name.  (Default = "output.txt")
* **-r / --reps:** Specify the maximum number of sequential BA3-SNPS runs to be conducted. (Default = 15)

## Example:

The following command will run the program from K values 1 through 10, conducting 10 repetitions at each K value.  Admixture will use all 16 processors available on the hypothetical machine, VCFtools will filter SNPs at an interval of 100bp, and the minor allele frequency filter in PLINK will drop any loci with a minor allele frequency less than 0.05:

```
admixturePipeline.py -m popmap.txt -v input.vcf -k 1 -K 10 -n 16 -t 100 -a 5
```

## Outputs:

For the example line of code above, the following outputs will be produced:
* **input.ped**, **input.map**: output of plink
