import os


def package_path_to_directory_path(package_path, configuration):
    '''Change `package_path` to directory path.

    Return string.
    '''
    if package_path is None:
        return
    package_path_parts = package_path.split('.')
    if package_path_parts[0] == \
        configuration.score_manager_tools_package_name:
        directory_parts = [configuration.score_manager_tools_directory_path] + \
            package_path_parts[1:]
    elif package_path_parts[0] == \
        configuration.score_external_materials_package_path:
        directory_parts = \
            [configuration.score_external_materials_directory_path] + \
            package_path_parts[1:]
    elif package_path_parts[0] == \
        configuration.score_external_segments_package_path:
        directory_parts = \
            [configuration.score_external_segments_directory_path] + \
            package_path_parts[1:]
    elif package_path_parts[0] == \
        configuration.score_external_specifiers_package_path:
        directory_parts = \
            [configuration.score_external_specifiers_directory_path] + \
            package_path_parts[1:]
    else:
        directory_parts = [configuration.scores_directory_path] + package_path_parts[:]
    directory_path = os.path.join(*directory_parts)
    return directory_path