import os
import gzip
import urllib.request
import ftplib
import tarfile

# OS type
linux = True
win = False

if os.name == 'nt':
    linux = False
    win = True
elif os.name == 'posix':
    linux = True
    win = False
else:
    raise Exception("Unsupported OS detected! Please use Linux or Windows.")


# Functions

def extractGZ(gzFile,outFile=None):
    if type(outFile) == type(None):
            ipspl = gzFile.split('.')[:-1]
            outFile = '.'.join(ipspl)
    ip = gzFile
    op = open(outFile,"w")
    with gzip.open(ip,"rb") as ip_byte:
            op.write(ip_byte.read().decode("utf-8"))
            op.close()


# exRNA data download

import ftplib
import tarfile
import os

ftp = ftplib.FTP('ftp.ncbi.nlm.nih.gov')
ftp.login("", "")
ftp.cwd('/geo/series/GSE106nnn/GSE106817/soft/')
filename = 'GSE106817_family.soft.gz'
try:
    ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
except:
    print("Error")

extractGZ("GSE106817_family.soft.gz")

urllib.request.urlretrieve("https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE106817&format=file", "GSE106817_RAW.tar")
tar = tarfile.open('./GSE106817_RAW.tar')
tar.extractall(path='./GSE106817_RAW',filter='data')

for root, dirs, files in os.walk("GSE106817_RAW"):
    for file in files:
        if file.endswith(".gz"):
             # print(file,os.path.join(root, file))
             # print(os.path.split(os.path.join(root, file)))
             extractGZ(os.path.join(root, file))
             os.remove(os.path.join(root, file))

# LC data

if linux:
    os.system('./gdc-client download -m ./LC_allcodes/lc_data/MANIFEST.txt -d ./LC_allcodes/LC_tcga/')
else:
    os.system('gdc-client download -m ./LC_allcodes/lc_data/MANIFEST.txt -d ./LC_allcodes/LC_tcga/')

## GTEX Healthy Control

urllib.request.urlretrieve("https://storage.googleapis.com/adult-gtex/bulk-gex/v8/rna-seq/counts-by-tissue/gene_reads_2017-06-05_v8_lung.gct.gz", "gene_reads_2017-06-05_v8_lung.gct.gz")
extractGZ("gene_reads_2017-06-05_v8_lung.gct.gz","./LC_allcodes/gene_reads_lung.gct")

## HomoSapiens Gene Length

urllib.request.urlretrieve("https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.gff.gz", "GRCh38_latest_genomic.gff.gz")
extractGZ("GRCh38_latest_genomic.gff.gz","./LC_allcodes/GRCh38_latest_genomic.gff")



# BC data

if linux:
    os.system('./gdc-client download -m ./BC_allcodes/bc_data/MANIFEST.txt -d ./BC_allcodes/BC_tcga/')
else:
    os.system('gdc-client download -m ./BC_allcodes/bc_data/MANIFEST.txt -d ./BC_allcodes/BC_tcga/')

## GTEX Healthy Control

urllib.request.urlretrieve("https://storage.googleapis.com/adult-gtex/bulk-gex/v8/rna-seq/counts-by-tissue/gene_reads_2017-06-05_v8_breast_mammary_tissue.gct.gz", "gene_reads_2017-06-05_v8_breast_mammary_tissue.gct.gz")
extractGZ("gene_reads_2017-06-05_v8_breast_mammary_tissue.gct.gz","./BC_allcodes/gene_reads_breast_mammary_tissue.gct")

## HomoSapiens Gene Length

urllib.request.urlretrieve("https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.gff.gz", "GRCh38_latest_genomic.gff.gz")
extractGZ("GRCh38_latest_genomic.gff.gz","./BC_allcodes/GRCh38_latest_genomic.gff")



# GC data

if linux:
    os.system('./gdc-client download -m ./GC_allcodes/gc_data/MANIFEST.txt -d ./GC_allcodes/GC_tcga/')
else:
    os.system('gdc-client download -m ./GC_allcodes/gc_data/MANIFEST.txt -d ./GC_allcodes/GC_tcga/')

## GTEX Healthy Control

urllib.request.urlretrieve("https://storage.googleapis.com/adult-gtex/bulk-gex/v8/rna-seq/counts-by-tissue/gene_reads_2017-06-05_v8_stomach.gct.gz", "gene_reads_2017-06-05_v8_stomach.gct.gz")
extractGZ("gene_reads_2017-06-05_v8_stomach.gct.gz","./GC_allcodes/gene_reads_stomach.gct")

## HomoSapiens Gene Length

urllib.request.urlretrieve("https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.gff.gz", "GRCh38_latest_genomic.gff.gz")
extractGZ("GRCh38_latest_genomic.gff.gz","./GC_allcodes/GRCh38_latest_genomic.gff")
