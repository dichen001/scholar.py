import os, csv
cwd = os.getcwd()


file_name = 'output0.txt'
file_path = os.path.join(cwd, file_name)

count = 0
all_info = {}


with open('infos.csv', 'w') as csvfile:
    fieldnames = ['Cluster_ID', 'Title', 'Year', 'Citations', 'Versions', 'URLs', 'PDF_links', 'Citations_list', 'PDF_urls']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    item = {}
    seen = False
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('getting: '):
                count += 1
                item_cnt = 1
                item['Cluster_ID'] = line[len('getting: '):].strip()
                print '~~~~~~~ processing article: ' + str(count) + ' ~~~~~~~'
                print '~~~~~~~ Source: ' + str(item_cnt) + ' ~~~~~~~'
                continue

            if line.lstrip().startswith('Excerpt') or line.lstrip().startswith('Cluster ID'):
                continue

            if line.lstrip().startswith('Year'):
                if 'Year' in item:
                    continue
                item['Year'] = line.lstrip()[len('Year '):].strip()
                continue

            if line.lstrip().startswith('Title'):
                if 'Title' in item:
                    continue
                item['Title'] = line.lstrip()[len('Title '):].strip()
                continue

            if line.lstrip().startswith('Citations'):
                if 'Citations' in item:
                    continue
                item['Citations'] = line.lstrip()[len('Citations '):].strip()
                continue

            if line.lstrip().startswith('Versions'):
                if 'Versions' in item:
                    continue
                item['Versions'] = line.lstrip()[len('Versions '):].strip()
                continue


            if line.lstrip().startswith('URL '):
                if 'URLs' not in item:
                    item['URLs'] = []
                item['URLs'] += [line.lstrip()[len('URL '):].strip()]
                continue

            if line.lstrip().startswith('PDF link '):
                if 'PDF_links' not in item:
                    item['PDF_links'] = []
                item['PDF_links'] += [line.lstrip()[len('PDF link '):].strip()]
                continue

            if line.strip() == '':
                item_cnt += 1
                seen = True
                print '~~~~~~~ Source: ' + str(item_cnt) + ' ~~~~~~~'
                continue

            if line.startswith('^^^'):
                writer.writerow(item)
                item = {}
