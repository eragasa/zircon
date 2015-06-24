#!/opt/moose/miniconda/bin/python

import os
import os.path
from pymatgen.io.cifio import CifParser
from pymatgen.io.vaspio import Poscar

cif_directory_name    = "cif_files"
poscar_directory_name = "poscar_files"

def GetFilenamesInDirectory(directoryName):
  filenames = [ f for f in os.listdir(directoryName) \
                        if os.path.isfile(os.path.join(directoryName,f))]
  return filenames


def EnsureDirectoryExists(directoryName):
  print(directoryName)
  d = os.path.dirname(directoryName)
  if not os.path.exists(directoryName):
    os.mkdir(directoryName)   

def ConvertCifFileToPoscarFile(cifFilename,poscarFilename):
  parser = CifParser(cifFilename)
  structure = parser.get_structures()[0]
  structure_name = cif_file.split('.')[0]

  poscar_obj      = Poscar(structure=structure,comment=structure_name)
  poscar_string   = poscar_obj.to_string()
  poscar_filename = '{}/{}.poscar'.format(poscar_directory_name,structure_name)

  with open(poscar_filename,'w') as f:
    f.write(poscar_string)

#------------------------------------------------------------------------------
cif_filenames = GetFilenamesInDirectory(directoryName=cif_directory_name)
crystal_system_names = [cif_filename.split('.')[0] for cif_filename in cif_filenames]

EnsureDirectoryExists(directoryName=poscar_directory_name)
for cif_file in cif_filenames:
  cif_filename   = "{}/{}".format(cif_directory_name,cif_file)
  structure_name = cif_file.split('.')[0]

  # Parse .cif file into a pymatgen structure file
  parser    = CifParser(cif_filename)
  structure = parser.get_structures()[0]

  # Create the poscar object and write it to file
  poscar_obj      = Poscar(structure=structure,comment=structure_name)
  poscar_string   = poscar_obj.get_string()
  poscar_filename = '{}/{}.poscar'.format(poscar_directory_name,structure_name)
  with open(poscar_filename,'w') as f:
    f.write(poscar_string)

