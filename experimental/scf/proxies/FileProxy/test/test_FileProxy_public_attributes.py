import os
import scf


def test_FileProxy_public_attributes_01():
    '''Without path.
    '''

    file_proxy = scf.proxies.FileProxy()

    assert not file_proxy.file_lines
    assert file_proxy.generic_class_name == 'file'
    assert file_proxy.human_readable_name is None
    assert not file_proxy.is_versioned
    assert file_proxy.parent_directory_name is None
    assert file_proxy.path_name is None
    assert file_proxy.plural_generic_class_name == 'files'
    assert file_proxy.short_name is None
    assert file_proxy.short_name_without_extension is None
    assert file_proxy.svn_add_command is None
    assert file_proxy.temporary_asset_short_name == 'temporary_file.txt'


def test_FileProxy_public_attributes_02():
    '''With path.
    '''

    short_name = 'clean_letter_14.ly'
    path_name = os.path.join(os.environ.get('SCFPATH'), 'stylesheets', short_name)
    file_proxy = scf.proxies.FileProxy(path_name)

    assert file_proxy.file_lines
    assert file_proxy.generic_class_name == 'file'
    assert file_proxy.human_readable_name == short_name
    assert file_proxy.is_versioned
    assert file_proxy.parent_directory_name == file_proxy.stylesheets_directory_name
    assert file_proxy.path_name == path_name
    assert file_proxy.plural_generic_class_name == 'files'
    assert file_proxy.short_name == short_name
    assert file_proxy.short_name_without_extension == short_name[:-3]
    assert file_proxy.svn_add_command == 'svn add {}'.format(file_proxy.path_name)
    assert file_proxy.temporary_asset_short_name == 'temporary_file.txt'