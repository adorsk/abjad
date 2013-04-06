import os
import py
import scf


studio = scf.studio.Studio()
wrangler = studio.material_package_wrangler
assert not wrangler.session.is_in_score


def test_MaterialPackageWrangler_iteration_01():
    '''Assets (all).
    '''

    assert 'red sargasso measures' in wrangler.list_asset_human_readable_names()
    assert 'red sargasso measures' not in wrangler.list_asset_human_readable_names(head='example_score_1')


def test_MaterialPackageWrangler_iteration_02():

    assert 'materials.red_sargasso_measures' in \
        wrangler.list_asset_importable_names()
    assert 'materials.red_sargasso_measures' not in \
        wrangler.list_asset_importable_names(head='example_score_1')


def test_MaterialPackageWrangler_iteration_03():

    assert os.path.join(os.environ.get('SCFMATERIALSPATH'), 'red_notes') in \
        wrangler.list_asset_path_names()
    assert os.path.join(os.environ.get('SCFMATERIALSPATH'), 'red_notes') not in \
        wrangler.list_asset_path_names(head='example_score_1')
    assert wrangler.list_asset_path_names(head='asdf') == []


def test_MaterialPackageWrangler_iteration_04():

    # wrangler.list_asset_proxies()
    pass


def test_MaterialPackageWrangler_iteration_05():
    '''Score-internal asset containers.
    '''

    assert 'example_score_1.mus.materials' in \
        wrangler.list_score_internal_asset_container_importable_names()
    assert 'example_score_2.mus.materials' in \
        wrangler.list_score_internal_asset_container_importable_names()
    assert 'example_score_1.mus.materials' not in \
        wrangler.list_score_internal_asset_container_importable_names(head='example_score_2')
    assert 'example_score_2.mus.materials' not in \
        wrangler.list_score_internal_asset_container_importable_names(head='example_score_1')
    assert wrangler.list_score_internal_asset_container_importable_names(head='asdf') == []


def test_MaterialPackageWrangler_iteration_06():

    assert os.path.join(os.environ.get('SCORES'), 'example_score_1', 'mus', 'materials') in \
        wrangler.list_score_internal_asset_container_path_names()
    assert os.path.join(os.environ.get('SCORES'), 'example_score_1', 'mus', 'materials') not in \
        wrangler.list_score_internal_asset_container_path_names(head='example_score_2')
    assert wrangler.list_score_internal_asset_container_path_names(head='asdf') == []


def test_MaterialPackageWrangler_iteration_07():
    '''Score-internal assets.
    '''
    py.test.skip('TODO: add time_signatures package to Example Score I.')

    assert 'example_score_1.mus.materials.time_signatures' in \
        wrangler.list_score_internal_asset_importable_names()
    assert 'example_score_1.mus.materials.time_signatures' not in \
        wrangler.list_score_internal_asset_importable_names(head='example_score_2')
    assert wrangler.list_score_internal_asset_importable_names(head='asdf') == []


def test_MaterialPackageWrangler_iteration_08():
    py.test.skip('TODO: add time_signatures package to Example Score I.')

    assert os.path.join(os.environ.get('SCORES'), 'example_score_1', 'mus', 'materials', 'time_signatures') in \
        wrangler.list_score_internal_asset_path_names()
    assert os.path.join(os.environ.get('SCORES'), 'example_score_1', 'mus', 'materials', 'time_signatures') in \
        wrangler.list_score_internal_asset_path_names(head='example_score_2')
    assert wrangler.list_score_internal_asset_path_names(head='asdf') == []


def test_MaterialPackageWrangler_iteration_09():
    '''Visible assets.
    '''

    assert 'red sargasso measures' in wrangler.list_visible_asset_human_readable_names()
    assert 'red sargasso measures' not in wrangler.list_visible_asset_human_readable_names(head='example_score_1')
    assert wrangler.list_visible_asset_human_readable_names(head='asdf') == []


def test_MaterialPackageWrangler_iteration_10():
   py.test.skip('TODO: add time_signatures package to Example Score I.')

   assert 'example_score_1.mus.materials.time_signatures' in \
        wrangler.list_visible_asset_importable_names()
   assert 'example_score_1.mus.materials.time_signatures' not in \
        wrangler.list_visible_asset_importable_names(head='example_score_2')
   assert wrangler.list_visible_asset_importable_names(head='asdf') == []


def test_MaterialPackageWrangler_iteration_11():
    py.test.skip('TODO: add time_signatures package to Example Score I.')

    assert ('materials.red_sargasso_measures', 'red sargasso measures') in \
        wrangler.make_visible_asset_menu_tokens()
    assert ('example_score_1.mus.materials.time_signatures', 'time signatures') in \
        wrangler.make_visible_asset_menu_tokens()
    assert ('materials.red_sargasso_measures', 'red sargasso measures') not in \
        wrangler.make_visible_asset_menu_tokens(head='example_score_1')
    assert ('example_score_1.mus.materials.time_signatures', 'time signatures') not in \
        wrangler.make_visible_asset_menu_tokens(head='example_score_2')


def test_MaterialPackageWrangler_iteration_12():

    # wrangler.list_visible_asset_proxies()
    pass