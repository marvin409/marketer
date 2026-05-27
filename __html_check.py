from bs4 import BeautifulSoup
from pathlib import Path

path = Path(r'c:\Users\ochie\OneDrive\Desktop\marketer\marvin.html')
html = path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
print('Parsed title:', soup.title.string if soup.title else 'None')
print('Total tags:', len(soup.find_all()))
print('Duplicate IDs count:', len([id for id in [tag.get('id') for tag in soup.find_all() if tag.get('id')] if [tag_id for tag_id in [tag.get('id') for tag in soup.find_all() if tag.get('id')] if tag_id].count(id) > 1]) )
