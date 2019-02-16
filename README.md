# BA3-SNPS-autotune
## Description:
This program will automatically tune mixing parameters for BA3-SNPs by implementing a binary search algorithm and conducting short exploratory runs of BA3-SNPS.  

## Citation:
An article describing this program and BA3-SNPS is currently in prep. For now, please cite this github repository if you use this program.

## Installation & Setup:

This program now requires Python 3.3 or greater. BA3-SNPS-autotune was designed to work on Unix based operating systems, such as various Linux distributions and Mac OS X.  To get started, clone this project to the desired location on your computer.  

You may have to modify the first line of the BA3-SNPS-autotune.py file, which by default reads:
```
#!/usr/bin/env python3
```
To find the location of your Python installation, you can type the following at the bash command prompt:
```
which python3
```
Then modify the first line of BA3-SNPS-autotune.py to reflect the location of your Python installation.

You must also install my modified version of BayesAss (BayesAss3-SNPS: https://github.com/stevemussmann/BayesAss3-SNPs). This program must be installed so that an executable named either **BA3-SNPS** or **ba3-snps** is present in your path. The autotune program will test for the presence of BA3-SNPS and report if it is not found. Please note that the autotune program is not compatible with Dr. Bruce Rannala's version of BA3 because I have altered some command line options. 

## Python 2.7.x Support

Future development of this program will no longer support Python 2.7.x. However, I have made the source code available as version 1.0.0 on the "releases" page of this repository.

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
* **-o / --out:** Specify a bayesass output file name.  (Default = "output.txt")
* **-r / --reps:** Specify the maximum number of sequential BA3-SNPS runs to be conducted. The program will exit early if suitable mixing parameters are detected by the program before conducting all of the specified runs. (Default = 15)

## Example:

The following command will perform 10 repetitions of the program, each time discarding 10,000 generations as burnin and running for 100,000 generations.  The input file is reported to contain 1,000 SNPs:

```
BA3-SNPS-autotune.py -i infile.immanc -l 1000 -b 10000 -g 100000 -r 10
```

While running, the commands directed to BA3-SNPS will be printed to stdout, as well as the repetition number currently in progress.

## Outputs:

For the example line of code above, the following outputs will be produced:
* **output.txt**: The output produced by the final run of BA3-SNPS.
* **infile.immanc.N.stdout**: One file will be produced for each run of BA3-SNPS, where N is replaced by the repetition number.  This file contains all information that BA3-SNPS would have printed to stdout.  For example, if suitable mixing parameters are found in the 3rd run of the program, the files infile.immanc.1.stdout, infile.immanc.2.stdout, and infile.immanc.3.stdout will be produced.
* **infile.immanc.finalParams.txt**: This file contains the final values for the m, a, and f mixing parameters needed to run BA3-SNPS.
* **infile.indiv.txt**: This is the indiv file produced by the final run of BA3-SNPS.
* **infile.trace.txt**: This is the trace file produced by the final run of BA3-SNPS.

## Development History and Bug Fixes:
2019-02-16:
* Converted the program to support Python3
* Added a function to check for a BA3-SNPS installation
