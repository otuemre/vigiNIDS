# UNSW-NB15 Dataset Documentation

## **What is the Data About?**
The UNSW-NB15 dataset is a benchmark dataset for network intrusion detection. It includes a mix of real-world normal activities and synthetic attack behaviors, making it suitable for developing and testing intrusion detection systems (IDS).

---

## **Brief Explanation About the Data**
- **Purpose**: Designed for evaluating and improving the performance of IDS models by providing realistic network traffic.
- **Source**: Created in the **Cyber Range Lab**, UNSW Canberra.
- **Details**:
  - Raw network packets were generated using the **IXIA PerfectStorm** tool.
  - Packets were captured using **tcpdump** and processed to produce structured data.
  - Contains **49 features** and labels for normal or attack traffic.
  - Includes **9 attack families**: Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode, and Worms.
  - Total records: **2,540,044**, divided into:
    - **Training set**: 175,341 records.
    - **Testing set**: 82,332 records.

---

## **Owner of the Data**
- The dataset was created and maintained by **Nour Moustafa** and the Cyber Range Lab at UNSW Canberra.

---

## **Source of the Data**
- Official dataset page: [UNSW-NB15 Dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset)

---

## **File Structure**
This folder does not contain the actual `.csv` files of the dataset but serves as a reference for the dataset. It includes:
- `README.md`: This documentation file.
- `The_UNSW-NB15_description.pdf`: A detailed description of the dataset, including its features, structure, and usage.

---

## **Contact for More Information**
For inquiries or access to additional data files (e.g., PCAP files), contact:
- **Nour Moustafa**  
  Email: [nour.moustafa@unsw.edu.au](mailto:nour.moustafa@unsw.edu.au)  
