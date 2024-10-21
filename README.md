<div align=center>
RESEARCH ASSIGNMENT #2:  <br>
A WEB FRAMEWORK BENCHMARK ANALYSIS
</div>
<br>

<div align=center>

Kevin Geidel <br>
MSDS 436: Analytics Systems Engineering <br>
Northwestern University <br>
October 27, 2024 <br>
</div>
<br>
</p>

### Experimental objectives

<hr>

* Design and conduct a benchmark study comparing two popular web frameworks: Django (Python) and Gin (Go)
* Test throughput and latency during a Monte Carlo performance benchmark with controlled queries using SQLite
* Control for the use of ORMs in each framework
* n=100 for each query task
* Generate reponse distributions and averages for each task
* Display and summarize results

### Included directories and files

<hr>



### Experimental design

<hr>

According to Quora's AI bot (Assistant 2024) a Monte Carlo performance benchmark must have a defined problem, model, reference data and established metrics. Each framework must answer ....

(INCLUDE "TREATMENT CONDITIONS" AND DATA)

The dataset used for the benchmark is a collection of every tic-tac-toe endstate (van Rijn 2014). There are 958 records and 10 attributes (the state of each of the nine squares plus a boolean representing if 'X', who moves first, is victorious or not.) 

QUERY TASKS:


* Nested conditionals: return all endstates in which either side is victorious using a diagonal
* Subquery: return all endstates in which the top-left square is 'X' and the bottom-right and middle-right squares are 'O'
* Aggregation: calculate the percentage of endstates in which 'X' is victorious.
* Aggregation: given each square a point value based on its position (top-left is 1 and bottom-right is 9) sum each side's total "score" over all records.


### Installing and running the benchmark

<hr>

```shell
# Clone and enter the repo
git clone git@github.com:kgeidel/MSDS-436-Research-Assignment-2.git
cd MSDS-436-Research-Assignment-2

# Obtain the dataset
wget https://www.openml.org/data/download/50/dataset_50_tic-tac-toe.arff -P data
```


### Experimental results

<hr>

(TABLES AND FIGURES)

### Conclusions

<hr>

(RECOMMENDATIONS FOR MANAGEMENT- WHICH FRAMEWORK TO USE?)

### References

<hr>

<div style="padding-left: 1.5em; text-indent: -1.5em">
Assistant. “How Do You Create a Benchmark for Testing Monte Carlo Simulation Against?” Quora, August 16, 2024. https://www.quora.com/How-do-you-create-a-benchmark-for-testing-Monte-Carlo-simulation-against. 

<br>

Rijn, Jan van. “Tic-Tac-Toe.” OpenML, April 6, 2014. https://www.openml.org/search?type=data&status=active&id=50. 


</div>