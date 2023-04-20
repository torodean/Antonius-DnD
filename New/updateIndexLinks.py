import os

for dirpath, dirnames, filenames in os.walk("."):
    # find all html files in the current directory
    html_files = [f for f in filenames if f.endswith('.html') and f != 'index.html']
    if not html_files:
        continue

    # create a list of existing links in the index file, if it exists
    index_file_path = os.path.join(dirpath, 'index.html')
    if os.path.exists(index_file_path):
        with open(index_file_path, 'r') as index_file:
            existing_links = [line.strip() for line in index_file.readlines() if line.strip().startswith('<li>')]
    else:
        existing_links = []

    # create a list of new links to add to the index file
    new_links = []
    for html_file in html_files:
        if html_file not in existing_links:
            new_links.append(f'<li><a href="{html_file}">{html_file}</a></li>')

    # append the new links to the index file
    if new_links:
        with open(index_file_path, 'a') as index_file:
            index_file.write('<ul>')
            for link in new_links:
                index_file.write(f'{link}\n')
            index_file.write('</ul>')
            print(f'Added {len(new_links)} links to {index_file_path}')
    else:
        print(f'No new links to add to {index_file_path}')
