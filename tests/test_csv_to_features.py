import sys

from networkml.featurizers.csv_to_features import CSVToFeatures
from networkml.parsers.pcap_to_csv import PCAPToCSV


def test_CSVToFeatures():
    sys.argv = ['pcap_to_csv.py', '-e', 'tshark', './tests/trace_ab12_2001-01-01_02_03-client-ip-1-2-3-4.pcap']
    instance = PCAPToCSV()
    instance.main()
    sys.argv = ['csv_to_features.py', '-g', 'tshark', './tests/trace_ab12_2001-01-01_02_03-client-ip-1-2-3-4.pcap.csv.gz']
    instance2 = CSVToFeatures()
    instance2.main()
