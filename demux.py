#!/usr/bin/python3.11

import samshee

# mockup to see:
#   how the samshee library handles our SampleSheet
#   if it allows adding collumns 
#   possible validation checks the library has
#       i think it only has schema checks, but one can hope
#
#   These are the six seqenced runs i got on disk . Found the path
# using `find /data -iname \*samplesheet\*`
#   The plan is to import all six files from disk to see if the
#   parser chokes on any one of them.
#   Then try to extend them
# /data/rawdata/201218_M06578_0041_000000000-JF7TM/SampleSheet.csv
# /data/rawdata/220603_M06578_0105_000000000-KB7MY/SampleSheet.csv
# /data/rawdata/240118_NB552450_0019_AHTYVCAFX5/SampleSheet.csv
# /data/rawdata/241104_M09180_0005_000000000-LP6KT/SampleSheet.csv
# /data/rawdata/241114_M09180_0007_000000000-LP35F/SampleSheet.csv
# /data/rawdata/241202_M06578_0219_000000000-LT29R/SampleSheet.csv
#
# then see if i can assign this new samplesheet object to a superclass
#   this will knock off 100 lines of parsing in my own code, just for 
#   parsing in the demux script
#       we will need to tweek demux to look into the subclass
#       and then assign the relative values
#           but we can worry about that later.

# The current fields in Magnus' sample sheet            # fields name here might be tentative
nvi_sample_sheet_fields = [
    'Sample_ID',            # string # we care          # demux.sample_sheet.sampleID
    'Sample_Plate',         # string # we no not care   #
    'Sample_Well',          # string # we do not care   #
    'Index_Plate_Well',     # string # we do not care   #
    'I7_Index_ID',          # string # we do not care   #
    'index',                # string # we do not care   #
    'I5_Index_ID',          # string # we do not care   #
    'index2',               # string # we do not care   #
    'Sample_Project',       # string # we care          # demux.sample_sheet.projectID[number_of_project].project_name
    'Transfer_VIGAS',       # bool   # we care          # demux.sample_sheet.projectID[number_of_project].transfer_to_vigas ( needs conversion from 'Yes'/'No' to True/False )
    'VIGASP_ID',            # int    # we care          # demux.sample_sheet.projectID[number_of_project].vigasID
    'Transfer_NIRD',        # bool   # we care          # demux.sample_sheet.projectID[number_of_project].transfer_to_nird ( needs conversion from 'Yes'/'No' to True/False )
    'NIRD_Location',        # string # we care          # demux.sample_sheet.projectID[number_of_project].nird_location
    'Genome_size'           # long   # we care          # demux.sample_sheet.projectID[number_of_project].genome
]
# we need demux.sample_sheet.project_length to get number_of_project

#  we also care for 
#   [Reads]
#       151
#       151
#
# which should be
#   sample_sheet.forward_reads
#   sample_sheet.reverse_reads
#
#   with logic
#       if sample_sheet.reverse_reads != sample_sheet.forward_reads:
#           sys.exit( "Exiting! Forward and reverse reads are not equal:\n" + "Forward reads: " + sample_sheet.forward_reads + "\n" + "Reverse reads: " + sample_sheet.reverse_reads )
#

# Also, 
#   if !demux.sample_sheet.projectID[number_of_project].vigasID && !demux.sample_sheet.projectID[number_of_project].transfer_to_nird
#       print( "Control project found, not uploading!" )
#


# make sure the library also has accessors for the following
# Investigator Name
# Experiment Name
# Date
# Workflow
# Application
# Instrument Type
# Assay
# Index Adapters
# Chemistry



# before we go forward, create a git repo and upload to my personal so we make sure we can 
# recover from fuckups.




samplesheets = [
    '/data/rawdata/201218_M06578_0041_000000000-JF7TM/SampleSheet.csv',
    '/data/rawdata/220603_M06578_0105_000000000-KB7MY/SampleSheet.csv',
    '/data/rawdata/240118_NB552450_0019_AHTYVCAFX5/SampleSheet.csv',
    '/data/rawdata/241104_M09180_0005_000000000-LP6KT/SampleSheet.csv',
    '/data/rawdata/241114_M09180_0007_000000000-LP35F/SampleSheet.csv',
    '/data/rawdata/241202_M06578_0219_000000000-LT29R/SampleSheet.csv'
]

for sheet_path in samplesheets:
    print( sheet_path )