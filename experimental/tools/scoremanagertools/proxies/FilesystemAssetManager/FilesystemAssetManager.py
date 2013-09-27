# -*- encoding: utf-8 -*-
import abc
import os
import shutil
import subprocess
from abjad.tools import stringtools
from experimental.tools.scoremanagertools.scoremanager.ScoreManagerObject \
    import ScoreManagerObject


class FilesystemAssetManager(ScoreManagerObject):
    r'''Filesystem asset proxy.
    '''

    ### CLASS VARIABLES ###

    __metaclass__ = abc.ABCMeta

    _generic_class_name = 'filesystem asset'

    boilerplate_directory_path = os.path.join(
        ScoreManagerObject.configuration.score_manager_tools_directory_path,
        'boilerplate')

    ### INITIALIZER ###

    def __init__(self, filesystem_path=None, session=None):
        assert filesystem_path is None or os.path.sep in filesystem_path
        self._filesystem_path = filesystem_path
        ScoreManagerObject.__init__(self, session=session)

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        r'''True when filesystem path properties are equal.
        Otherwise false.

        Return boolean.
        '''
        if isinstance(expr, type(self)):
            if self.filesystem_path == expr.filesystem_path:
                return True
        return False

    def __repr__(self):
        r'''Interpreter representation of filesystem assset proxy.

        Return string.
        '''
        return '{}({!r})'.format(self._class_name, self.filesystem_path)

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        return self.filesystem_basename or \
            self._space_delimited_lowercase_class_name

    @property
    def _plural_generic_class_name(self):
        return stringtools.pluralize_string(self._generic_class_name)

    @property
    def _space_delimited_lowercase_name(self):
        return self.filesystem_basename

    @property
    def _repository_add_command(self):
        if self.filesystem_path:
            return 'svn add {}'.format(self.filesystem_path)

    ### PRIVATE METHODS ###

    def _initialize_file_name_getter(self):
        getter = self.session.io_manager.make_getter()
        getter.append_snake_case_file_name('new name')
        return getter

    def _run(self, cache=False, clear=True, pending_user_input=None):
        self.session.io_manager.assign_user_input(pending_user_input)
        self.session.cache_breadcrumbs(cache=cache)
        while True:
            self.session.push_breadcrumb(self._breadcrumb)
            menu = self._make_main_menu()
            result = menu._run(clear=clear)
            if self.session.backtrack(source=self._backtracking_source):
                break
            elif not result:
                self.session.pop_breadcrumb()
                continue
            self._handle_main_menu_result(result)
            if self.session.backtrack(source=self._backtracking_source):
                break
            self.session.pop_breadcrumb()
        self.session.pop_breadcrumb()
        self.session.restore_breadcrumbs(cache=cache)

    @staticmethod
    def _safe_import(
        target_namespace,
        source_module_name,
        source_attribute_name,
        source_parent_package_path=None,
        ):

        #print repr(target_namespace.keys())
        #print repr(source_module_name)
        #print repr(source_attribute_name)
        #print repr(source_parent_package_path)

        if source_parent_package_path is None:
            try:
                source_parent_package_path = target_namespace['__name__']
            except KeyError:
                pass

        if source_parent_package_path:
            source_module_path = '{}.{}'.format(
                source_parent_package_path, source_module_name)
        else:
            source_module_path = source_module_name

        try:
            source_module = __import__(source_module_path, fromlist=['*'])
        except:
            message = 'Error importing {!r}.'.format(source_module_path)
            print message
            return

        try:
            source_attribute_value = source_module.__dict__[
                source_attribute_name]
        except:
            message = 'Can not import {!r} from {!r}.'.format(
                source_attribute_name, source_module_path)
            print message
            return

        target_namespace[source_attribute_name] = source_attribute_value
        return source_attribute_value

    def _space_delimited_lowercase_name_to_asset_name(
        self, space_delimited_lowercase_name):
        space_delimited_lowercase_name = space_delimited_lowercase_name.lower()
        asset_name = space_delimited_lowercase_name.replace(' ', '_')
        return asset_name

    ### PUBLIC PROPERTIES ###

    @property
    def filesystem_basename(self):
        r'''Filesystem basename of filesystem asset proxy.

        Returns string or none.
        '''
        if self.filesystem_path:
            return os.path.basename(self.filesystem_path)

    @property
    def filesystem_path(self):
        r'''Filesystem path of filesystem asset proxy.

        Returns string.
        '''
        return self._filesystem_path

    @property
    def parent_directory_filesystem_path(self):
        r'''Filesystem path of filesystem asset proxy parent directory.

        Returns string.
        '''
        if self.filesystem_path:
            return os.path.dirname(self.filesystem_path)

    ### PUBLIC METHODS ###

    def copy(self, new_filesystem_path):
        r'''Copies filesystem asset to `new_filesystem_path`.

        Return none.
        '''
        shutil.copyfile(self.filesystem_path, new_filesystem_path)

    def exists(self):
        r'''True when filesystem path of filesystem asset proxy exists.
        False otherwise.

        Returns boolean.
        '''
        if self.filesystem_path:
            return os.path.exists(self.filesystem_path)
        return False

    def interactively_copy(
        self, 
        pending_user_input=None,
        ):
        r'''Interactively copies filesystem asset.

        Returns none.
        '''
        self.session.io_manager.assign_user_input(pending_user_input)
        getter = self._initialize_file_name_getter()
        result = getter._run()
        if self.session.backtrack():
            return
        new_asset_name = \
            self._space_delimited_lowercase_name_to_asset_name(result)
        new_path = \
            os.path.join(self.parent_directory_filesystem_path, new_asset_name)
        self.session.io_manager.display('new path will be {}'.format(new_path))
        if not self.session.io_manager.confirm():
            return
        self.copy(new_path)
        self.session.io_manager.proceed('asset copied.')

    def interactively_remove(
        self, 
        pending_user_input=None,
        ):
        r'''Interactively removes filesystem asset.

        Returns none.
        '''
        self.session.io_manager.assign_user_input(pending_user_input)
        message = '{} will be removed.'.format(self.filesystem_path)
        self.session.io_manager.display([message, ''])
        getter = self.session.io_manager.make_getter(where=self._where)
        getter.append_string("type 'remove' to proceed")
        result = getter._run()
        if self.session.backtrack():
            return
        if not result == 'remove':
            return
        if self.remove():
            message = '{} removed.'.format(self.filesystem_path)
            self.session.io_manager.proceed(message)

    def interactively_remove_and_backtrack_locally(self):
        r'''Interactively removes filesystem asset and backtracks locally.

        Returns none.
        '''
        self.interactively_remove()
        self.session.is_backtracking_locally = True

    def interactively_rename(
        self, 
        pending_user_input=None,
        ):
        r'''Interactively renames filesystem asset.

        Returns none.
        '''
        self.session.io_manager.assign_user_input(pending_user_input)
        getter = self._initialize_file_name_getter()
        getter.include_newlines = False
        result = getter._run()
        if self.session.backtrack():
            return
        new_path = os.path.join(self.parent_directory_filesystem_path, result)
        message = 'new path name will be: "{}"'.format(new_path)
        self.session.io_manager.display([message, ''])
        if not self.session.io_manager.confirm():
            return
        if self.rename(new_path):
            self.session.io_manager.proceed('asset renamed.')

    def interactively_write_boilerplate(
        self, 
        pending_user_input=None,
        ):
        r'''Interactively writes filesystem asset boilerplate.

        Returns none.
        '''
        self.session.io_manager.assign_user_input(pending_user_input)
        getter = self.session.io_manager.make_getter(where=self._where)
        getter.append_snake_case_file_name('name of boilerplate asset')
        with self.backtracking:
            boilerplate_filebuilt_in_asset_name = getter._run()
        if self.session.backtrack():
            return
        if self.write_boilerplate(boilerplate_filebuilt_in_asset_name):
            self.session.io_manager.proceed('boilerplate asset copied.')
        else:
            message = 'boilerplate asset {!r} does not exist.'
            message = message.format(boilerplate_filebuilt_in_asset_name)
            self.session.io_manager.proceed(message)

    def is_versioned(self):
        r'''True when filesystem asset is versioned.
        Otherwise false.

        Returns boolean.
        '''
        if self.filesystem_path is None:
            return False
        if not os.path.exists(self.filesystem_path):
            return False
        command = 'svn st {}'.format(self.filesystem_path)
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            )
        first_line = process.stdout.readline()
        if first_line.startswith(('?', 'svn: warning:')):
            return False
        else:
            return True

    @abc.abstractmethod
    def make_empty_asset(self, is_interactive=False):
        r'''Makes empty filesystem asset.

        Returns none.
        '''
        pass

    def remove(self):
        r'''Removes filesystem asset.

        Returns none.
        '''
        if self.is_versioned():
            command = 'svn --force rm {}'.format(self.filesystem_path)
            proc = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                )
            proc.stdout.readline()
            return True
        else:
            command = 'rm -rf {}'.format(self.filesystem_path)
            proc = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                )
            proc.stdout.readline()
            return True

    def rename(self, new_path):
        r'''Renames filesystem asset.

        Returns none.
        '''
        if self.is_versioned():
            command = 'svn --force mv {} {}'.format(
                self.filesystem_path, new_path)
            proc = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                )
            proc.stdout.readline()
            self._filesystem_path = new_path
        else:
            command = 'mv {} {}'.format(
                self.filesystem_path, new_path)
            proc = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                )
            proc.stdout.readline()
            self._filesystem_path = new_path

    def repository_add(self, is_interactive=False):
        r'''Adds unversioned filesystem assets to repository.

        Returns none.
        '''
        if is_interactive:
            self.session.io_manager.display(self.filesystem_path)
        proc = subprocess.Popen(
            self._repository_add_command,
            shell=True,
            stdout=subprocess.PIPE,
            )
        lines = [line.strip() for line in proc.stdout.readlines()]
        lines.append('')
        if is_interactive:
            self.session.io_manager.display(lines)
        self.session.io_manager.proceed(is_interactive=is_interactive)

    def repository_ci(self, commit_message=None, is_interactive=True):
        r'''Commits unversioned filesystem assets to repository.

        Returns none.
        '''
        if commit_message is None:
            getter = self.session.io_manager.make_getter(where=self._where)
            getter.append_string('commit message')
            commit_message = getter._run(clear_terminal=False)
            if self.session.backtrack():
                return
            line = 'commit message will be: "{}"\n'.format(commit_message)
            self.session.io_manager.display(line)
            if not self.session.io_manager.confirm():
                return
        lines = []
        lines.append(self.filesystem_path)
        command = 'svn commit -m "{}" {}'
        command = command.format(commit_message, self.filesystem_path)
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            )
        lines.extend([line.strip() for line in process.stdout.readlines()])
        lines.append('')
        self.session.io_manager.display(lines)
        self.session.io_manager.proceed(is_interactive=is_interactive)

    def repository_st(self, is_interactive=True):
        r'''Displays repository status of filesystem assets.
    
        Returns none.
        '''
        command = 'svn st -u {}'.format(self.filesystem_path)
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            )
        path = self.filesystem_path
        path = path + os.path.sep
        clean_lines = []
        for line in process.stdout.readlines():
            clean_line = line.strip()
            clean_line = clean_line.replace(path, '')
            clean_lines.append(clean_line)
        clean_lines.append('')
        self.session.io_manager.display(clean_lines)
        self.session.io_manager.proceed(is_interactive=is_interactive)

    def repository_up(self, is_interactive=True):
        r'''Updates versioned filesystem assets.

        Returns none.
        '''
        if is_interactive:
            self.session.io_manager.display(self.filesystem_path)
        command = 'svn up {}'.format(self.filesystem_path)
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            )
        lines = [line.strip() for line in proc.stdout.readlines()]
        lines.append('')
        self.session.io_manager.display(lines)
        self.session.io_manager.proceed(is_interactive=is_interactive)

    def write_boilerplate(self, boilerplate_filebuilt_in_asset_name):
        r'''Writes filesystem asset boilerplate.

        Returns none.
        '''
        if not os.path.exists(boilerplate_filebuilt_in_asset_name):
            boilerplate_filebuilt_in_asset_name = os.path.join(
                self.boilerplate_directory_path,
                boilerplate_filebuilt_in_asset_name)
        if os.path.exists(boilerplate_filebuilt_in_asset_name):
            shutil.copyfile(
                boilerplate_filebuilt_in_asset_name,
                self.filesystem_path)
            return True

    ### UI MANIFEST ###

    user_input_to_action = {
        'cp': interactively_copy,
        'rm': interactively_remove_and_backtrack_locally,
        'ren': interactively_rename,
        }