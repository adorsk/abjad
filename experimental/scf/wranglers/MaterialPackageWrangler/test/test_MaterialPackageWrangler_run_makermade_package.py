from abjad.tools import notetools
import scf
import py


def test_MaterialPackageWrangler_run_makermade_package_01():
    '''Make makermade package. Delete package.
    '''

    studio = scf.studio.Studio()
    assert not studio.package_exists('materials.testsargasso')

    try:
        studio.run(user_input='m m sargasso testsargasso default q')
        assert studio.package_exists('materials.testsargasso')
        mpp = scf.makers.SargassoMeasureMaterialPackageMaker(
            'materials.testsargasso')
        assert mpp.is_makermade
        assert mpp.directory_contents == ['__init__.py', 'tags.py', 'user_input.py']
        assert mpp.has_initializer
        assert not mpp.has_output_material_module
        assert mpp.has_user_input_module
        assert not mpp.initializer_has_output_material_safe_import_statement
        assert not mpp.parent_initializer_has_output_material_safe_import_statement
        assert mpp.output_material is None
    finally:
        studio.run(user_input='m testsargasso del remove default q')
        assert not studio.package_exists('materials.testsargasso')


def test_MaterialPackageWrangler_run_makermade_package_02():
    '''Make score-resident makermade package. Delete package.
    '''

    studio = scf.studio.Studio()
    assert not studio.package_exists('betoerung.mus.materials.testsargasso')

    try:
        studio.run(user_input='betörung m m sargasso testsargasso default q')
        assert studio.package_exists('betoerung.mus.materials.testsargasso')
        mpp = scf.makers.SargassoMeasureMaterialPackageMaker(
            'betoerung.mus.materials.testsargasso')
        assert mpp.is_makermade
        assert mpp.directory_contents == ['__init__.py', 'tags.py', 'user_input.py']
        assert mpp.has_initializer
        assert not mpp.has_output_material_module
        assert mpp.has_user_input_module
        assert not mpp.initializer_has_output_material_safe_import_statement
        assert not mpp.parent_initializer_has_output_material_safe_import_statement
        assert mpp.output_material is None
    finally:
        studio.run(user_input='betörung m testsargasso del remove default q')
        assert not studio.package_exists('betoerung.mus.materials.testsargasso')


#def test_MaterialPackageWrangler_run_makermade_package_03():
#    '''Make makermade package. Corrupt initializer.
#    Verify invalid initializer. Remove package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso incanned canned_exception.py default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py', 'material_definition.py']
#        assert not mpp.has_readable_initializer
#        assert mpp.has_readable_material_definition_module
#        assert not mpp.has_output_material_module
#        assert not mpp.has_illustration_builder_module
#        assert not mpp.initializer_has_output_material_safe_import_statement
#        assert not mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition is None
#        assert mpp.output_material is None
#        assert mpp.illustration is None
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_04():
#    '''Make makermade package. Corrupt initializer. Restore initializer.
#    Verify initializer. Remove package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso incanned canned_exception.py default '
#            'inr yes yes default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py', 'material_definition.py']
#        assert mpp.has_readable_initializer
#        assert mpp.has_readable_material_definition_module
#        assert not mpp.has_output_material_module
#        assert not mpp.has_illustration_builder_module
#        assert not mpp.initializer_has_output_material_safe_import_statement
#        assert not mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition is None
#        assert mpp.output_material is None
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_05():
#    '''Make makermade package. Create output material.
#    Delete package."
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso mdcanned canned_testsargasso_material_definition.py default '
#            'omm default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py',
#            'illustration_builder.py', 'material_definition.py', 'output_material.py']
#        assert mpp.has_readable_initializer
#        assert mpp.has_user_finalized_material_definition_module
#        assert mpp.has_readable_output_material_module
#        assert mpp.has_illustration_builder_module
#        assert mpp.initializer_has_output_material_safe_import_statement
#        assert mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition and notetools.all_are_notes(mpp.material_definition)
#        assert mpp.output_material and notetools.all_are_notes(mpp.output_material)
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_06():
#    '''Make makermade package. Delete material definition module.
#    Remove package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso mddelete default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py']
#        assert mpp.has_readable_initializer
#        assert not mpp.has_material_definition_module
#        assert not mpp.has_output_material_module
#        assert not mpp.has_illustration_builder_module
#        assert not mpp.initializer_has_output_material_safe_import_statement
#        assert not mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition is None
#        assert mpp.output_material is None
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_07():
#    '''Make makermade package. Overwrite material definition module with stub.
#    Delete package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso mdstub default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py', 'material_definition.py']
#        assert mpp.has_readable_initializer
#        assert mpp.has_readable_material_definition_module
#        assert not mpp.has_output_material_module
#        assert not mpp.has_illustration_builder_module
#        assert not mpp.initializer_has_output_material_safe_import_statement
#        assert not mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition is None
#        assert mpp.output_material is None
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_08():
#    '''Make makermade package. Copy canned material definition. Make output material. Remove output material.
#    Remove package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso mdcanned canned_testsargasso_material_definition.py default '
#            'omm default '
#            'omdelete default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py', 'material_definition.py']
#        assert mpp.has_readable_initializer
#        assert mpp.has_user_finalized_material_definition_module
#        assert not mpp.has_output_material_module
#        assert not mpp.has_illustration_builder_module
#        assert not mpp.initializer_has_output_material_safe_import_statement
#        assert not mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition and notetools.all_are_notes(mpp.material_definition)
#        assert mpp.output_material is None
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_09():
#    '''Make makermade package. Copy canned material definition with exception.
#    Examine package state. Remove package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso mdcanned canned_exception.py default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py', 'material_definition.py']
#        assert mpp.has_readable_initializer
#        assert not mpp.has_readable_material_definition_module
#        assert not mpp.has_output_material_module
#        assert not mpp.has_illustration_builder_module
#        assert not mpp.initializer_has_output_material_safe_import_statement
#        assert not mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition is None
#        assert mpp.output_material is None
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_10():
#    '''Make makermade package. Copy canned material definition module. Make output data. Corrupt output data.
#    Verify invalid output material module. Remove package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso mdcanned canned_testsargasso_material_definition.py default '
#            'omm default '
#            'omcanned canned_exception.py default q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == ['__init__.py',
#            'illustration_builder.py', 'material_definition.py', 'output_material.py']
#        assert mpp.has_readable_initializer
#        assert mpp.has_user_finalized_material_definition_module
#        assert not mpp.has_readable_output_material_module
#        assert mpp.has_illustration_builder_module
#        assert mpp.initializer_has_output_material_safe_import_statement
#        assert mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition and notetools.all_are_notes(mpp.material_definition)
#        assert mpp.output_material is None
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')
#
#
#def test_MaterialPackageWrangler_run_makermade_package_11():
#    '''Make makermade package. Copy canned material definition module.
#    Make output data. Make PDF. Remove package.
#    '''
#
#    studio = scf.studio.Studio()
#    assert not studio.package_exists('materials.testsargasso')
#
#    try:
#        studio.run(user_input=
#            'm m testsargasso default default '
#            'testsargasso mdcanned canned_testsargasso_material_definition.py default '
#            'omm default '
#            'pdfm default '
#            'q')
#        assert studio.package_exists('materials.testsargasso')
#        mpp = scf.makers.SargassoMeasureMaterialPackageMaker('materials.testsargasso')
#        assert mpp.is_makermade and not mpp.is_data_only
#        assert mpp.directory_contents == [
#            '__init__.py', 'illustration.ly', 'illustration.pdf',
#            'illustration_builder.py', 'material_definition.py', 'output_material.py']
#        assert mpp.has_readable_initializer
#        assert mpp.has_user_finalized_material_definition_module
#        assert mpp.has_readable_output_material_module
#        assert mpp.has_user_finalized_illustration_builder_module
#        assert mpp.has_illustration_ly
#        assert mpp.has_illustration_pdf
#        assert mpp.initializer_has_output_material_safe_import_statement
#        assert mpp.parent_initializer_has_output_material_safe_import_statement
#        assert mpp.material_definition and notetools.all_are_notes(mpp.material_definition)
#        assert mpp.output_material and notetools.all_are_notes(mpp.output_material)
#    finally:
#        studio.run(user_input='m testsargasso del remove default q')
#        assert not studio.package_exists('materials.testsargasso')