# CS341_Final-Report

## **About**
This repository contains the Python implementation and experimental results of the GDLRU (Greedy Dual Least Recently Used) algorithm, designed for flash memory-aware page replacement systems. GDLRU incorporates two key mechanisms:
1. **Clean-aware Victim Page Selection (CPS)**: Prioritizes clean page eviction to minimize write operations.
2. **Clean-aware Victim Page Update (CPU)**: Optimizes write-back by only writing the modified portions of dirty pages.

The implemented algorithm has been evaluated against the traditional LRU algorithm under various workloads and configurations. The experiments demonstrate that GDLRU significantly reduces page write operations, achieving higher efficiency in flash memory systems.

### **Group Members**
- **ZHANG RUIHAO**, 1220001110
- **CHEN YIJIA**, 1220005724
- **WANG ZHERAN**, 1220005681

This work represents our reproduction of the GDLRU algorithm described in the paper _"Greedy Page Replacement Algorithm for Flash-aware Swap System"_, with additional Python implementation and analysis.

---

## **Usage**
### Test
The code provides a simulation framework to evaluate the GDLRU algorithm against the traditional LRU algorithm. To run the main script:
```bash
python main.py
```

### Code Structure
`GDLRU.py`: Contains the implementation of the GDLRU algorithm.

`LRU.py`: Contains the implementation of the traditional LRU algorithm.

`main.py`: The main script for running the experiments and printing the results.

`random_pattern.py`: Defines the experimental framework and configurations.

---

## **Results**
Below are the key results from the experiments:

| Configuration       | GDLRU (Write Count) | LRU (Write Count) |
|---------------------|---------------------|-------------------|
| 10 pages, cache 5   | 1372               | 1421             |
| 50 pages, cache 10  | 2052               | 2073             |
| 100 pages, cache 50 | 1263               | 1291             |

For a detailed analysis, refer to the [project report](OS_Final_Report.pdf).

---

## **Acknowledgments**
Special thanks to the authors of the paper [_Greedy Page Replacement Algorithm for Flash-aware Swap System_](https://ieeexplore.ieee.org/document/6227444) for inspiring this implementation. For more details, refer to the original paper.
