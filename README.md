# Usage
```
git clone https://github.com/brucewu-fly/es_test.git
cd es_test
pip install elasticsearch

python scan_demo_1.py <index> 10000
python scan_demo_1.py <index> 1000
python scan_demo_1.py <index> 100

mkdir tmp

python scan_demo_2.py <index> 10000
python scan_demo_2.py <index> 1000
python scan_demo_2.py <index> 100

python scan_demo_3.py <index> 1000 5
python scan_demo_3.py <index> 1000 10
python scan_demo_3.py <index> 1000 100
```