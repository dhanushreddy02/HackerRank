import sys
import xml.etree.ElementTree as etree
sys.stdin.readline()
xml = sys.stdin.read()
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
print(xml)
print(tree)
print(root)
