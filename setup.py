from distutils.core import setup
setup(name='patho_pdb_domain',
		version='0.0.1',
		py_modules=['MOAD_PDBBIND','extracts','ligand_from_pdb'],
		scripts=['MOAD_PDBBIND/MOAD.py','MOAD_PDBBIND/filter_MOAD.py', 'MOAD_PDBBIND/toMolar.py', 'MOAD_PDBBIND/PDBBIND.py', 'extracts/extract_ligand_from_pdb.py'
			 ,'extracts/extract_pdb_from_domain.py','extracts/protein_id_extract_to_uniprot.py'
			 ,'ligand_from_pdb/domain_pdb_ligand.py','ligand_from_pdb/request_ligand_from_PDBe.py'],

		requires=['requests','argparse','sys'],

		author='Federico Serral',
		license='MIT license',
		author_email='fedeserral92@gmail.com',
		description='Extract true ligands',
		url='https://github.com/fedeserral/patho_pdb_domain',
		long_description='',
		)
