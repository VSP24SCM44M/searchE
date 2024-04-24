# Search Engine

Author: Vinay Kumar Moka\
ID: A20552044

## Abstract
Developing a full search engine system with an indexer, query processor, and web crawler is the project's main objective. The major objective is to enable users to search through a corpus of web documents using free text searches in an efficient manner. The scrapy-built crawler facilitates the retrieval of web content, while the indexer, powered by Scikit-Learn, organizes the web data into a searchable inverted index. To obtain relevant results, users can submit questions into the interface of the Flask-based processing.

## Overview
In this project, we are developing a search engine that uses the TF-IDF (Term Frequency-Inverse Document Frequency) score to retrieve and rank web content. In the provided system and solution outline, the web crawler, indexing engine, and query processor are the three main components. To ensure precise and potent search capabilities, the development process goes through several crucial stages. Information for this project comes from the Scikit-Learn manual, recent semantic search research, and KNN approaches.

## Design
The system has a number of impressive features:\
Web Crawling: It gathers web documents from given URLs using a Scrapy-based crawler while adhering to limitations such as maximum page count and traversal depth\
Indexing: Using advanced features like word embeddings and FAISS for increased similarity search, it builds an inverted index with TF-IDF scores using Scikit-Learn.\
Processing User Queries: The Flask processor processes user queries by using cosine similarity and TF-IDF scores to ensure validation and provide the best possible results. Additionally, it provides features for query expansion and spell checking.\

**Interactions:**\
Web Crawling to Indexing: An inverted index with TF-IDF scores is produced by the indexing engine using web content that has been crawled.\
Indexing to Query Processing: In order to make it easier for users to get pertinent content in response to queries, the indexing engine creates an inverted index.\
User Interaction: By entering queries and getting search results, users interact with the system using the Flask-based query processor.

**Integration:**\
Two APIs interface with the indexing engine and query processor to provide search through standard and enhanced indexing. Web crawling, indexing, and query processing are the stages in which data flows. Future feature improvements can be accommodated by the modular design, which guarantees an effective system with accurate search results.

## Architecture
Several essential elements make up the software architecture:\
**Web Crawler:** Designed with Scrapy, this part is in charge of obtaining web pages from given URLs.\
**Indexing Engine:** Based on Scikit-Learn, it can conduct TF-IDF indexing and provides extended indexing capabilities using word embeddings and FAISS, among other advanced techniques.\
**Query Processor:** This Flask-based module processes user queries, performs validation, and returns search results.\
**APIs:** The system has an API that provide search results according to advanced and traditional indexing techniques.

Interfaces:\
**API Interfaces:** The RESTful nature of the API enables users to effortlessly access search capability.\
**Data Interface:** Ensuring efficient data flow across the system, data pipelines facilitate communication between the crawler, indexing engine, and query processor. The architecture places an emphasis on the smooth operation of components, promoting unambiguous interfaces for effective data transfer. Scalability and extensibility are encouraged by its modular design, which makes it possible to integrate new features and functionalities to accommodate changing needs. 

## Operation
To guarantee a smooth project launch, do the following actions to get started:\
**a) Initial setup**\
Create and activate a python environment\
```python3 -m venv project-env```\
```source project-env/bin/activate```

**b) Installation of Libraries:**\
Run the following commands to install the necessary libraries:
```
pip install Scrapy
pip install jsonlib
pip install nltk
pip install scikit-learn
pip install flask
```
**c) Project Execution Instructions:**\
Step 1: Open your terminal, navigate to the folder web_scrapper, and type the below command. The command will crawl the web page.
```
cd web_scrapper
scrapy crawl bootstrap_spider
```

Step 2:
```
cd ../search-handler
python3 text_handler.py 
```
The TF-IDF scores and cosine similarity for the HTML documents are calculated by this command, which also starts the web crawling operation. The results are saved in an scikit.pkl file.

Step 3:
```
export FLASK_APP=query_handler
Flask run
```
This will launch a server\
Step 4:\
```curl -X POST -H "Content-Type: application/json" -d '{"query": "add columns dynamically"}' http://127.0.0.1:5000/search-scikit```

After running this command, the server will respond to you in JSON format with the document titles and cosine similarity scores of the top k results.

## Conclusion:
To sum up, the project has successfully implemented both APIs, and the output is the effective return of pertinent documents. Though it still needs to be refined, there is potential for development in the document rating system. Although the Scikit-learn API returns relevant documents with a fair degree of precision for the majority of queries, some questions may require additional optimization. Notwithstanding these factors, the system's dependability is demonstrated by the consistent outcomes in all three circumstances. 

## Test cases:
```curl -X POST -H "Content-Type: application/json" -d '{"query": "add columns dynamically"}' http://127.0.0.1:5000/search-scikit```

<img width="1440" alt="Screenshot 2024-04-23 at 5 02 58 PM" src="https://github.com/VSP24SCM44M/searchE/assets/164983146/d4fa773f-339c-4fa7-bff4-71bd4a5c5375">
Prettier Output
<img width="1000" alt="Screenshot 2024-04-23 at 5 04 16 PM" src="https://github.com/VSP24SCM44M/searchE/assets/164983146/ce187454-5293-4457-8982-c0fa93e0df9b">
<img width="878" alt="Screenshot 2024-04-23 at 5 10 34 PM" src="https://github.com/VSP24SCM44M/searchE/assets/164983146/6992d1f9-0f2f-4cbf-914a-80977412eef3">

```curl -X POST -H "Content-Type: application/json" -d '{"query": "enable dark mode"}' http://127.0.0.1:5000/search-scikit```
<img width="1438" alt="Screenshot 2024-04-23 at 5 06 22 PM" src="https://github.com/VSP24SCM44M/searchE/assets/164983146/91f950d7-94c0-4620-917e-063b0386ef6c">
Prettier Output
<img width="900" alt="Screenshot 2024-04-23 at 5 07 40 PM" src="https://github.com/VSP24SCM44M/searchE/assets/164983146/565c852b-8b47-4c7d-8ed8-c46bfd3159f6">
<img width="1440" alt="Screenshot 2024-04-23 at 5 08 44 PM" src="https://github.com/VSP24SCM44M/searchE/assets/164983146/2c8301c1-20f2-41ea-8448-f385f1b3bc2a">

## Data Sources:
The following essential libraries and tools are needed for the project:\
Scrapy (2.11.1) is a web crawling tool.\
Version 1.4.2 of Scikit-learn is used for advanced search functionalities and TF-IDF indexing.\
Flask 3.0.3 is used to construct the module for the query processor.

## Source Code
[Spider file](https://github.com/VSP24SCM44M/searchE/blob/main/processer/web_scrapper/web_scrapper/spiders/bootstrap_spider.py)\
[Sample Scrapped page](https://github.com/VSP24SCM44M/searchE/blob/main/processer/web_scrapper/bootstrap-1.json)\
[tf-IDF scoring logic](https://github.com/VSP24SCM44M/searchE/blob/main/processer/web_scrapper/search-handler/text_handler.py)
[Flask API](https://github.com/VSP24SCM44M/searchE/blob/main/processer/web_scrapper/search-handler/query_handler.py)

## Bibliography
1.)Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to Information Retrieval. Cambridge University Press.\
2.)Scrapy. (n.d.). Retrieved from https://scrapy.org/ \
3.)Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, & Vanderplas, J. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12(Oct), 2825-2830.







