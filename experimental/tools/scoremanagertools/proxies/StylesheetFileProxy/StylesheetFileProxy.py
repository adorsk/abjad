from experimental.tools.scoremanagertools.proxies.FileProxy import FileProxy


class StylesheetFileProxy(FileProxy):

    ### CLASS ATTRIBUTES ###

    _generic_class_name = 'stylesheet'
    _temporary_asset_name = 'temporary_stylesheet.ly'

    ### PRIVATE METHODS ###

    def _handle_main_menu_result(self, result):
        assert isinstance(result, str)
        if result == 'cp':
            self.copy_interactively()
        elif result == 'pr':
            self.profile()
        elif result == 'rm':
            self.remove_interactively()
            self._session.is_backtracking_locally = True
        elif result == 'ren':
            self.rename_interactively()
        elif result == 'vi':
            self.edit()
        else:
            raise ValueError

    def _make_main_menu(self):
        menu, section = self._io.make_menu(where=self.where)
        section.append(('cp', 'copy stylesheet'))
        section.append(('pr', 'profile stylesheet'))
        section.append(('rm', 'delete stylesheet'))
        section.append(('ren', 'rename stylesheet'))
        section.append(('vi', 'vi stylesheet'))
        return menu

    def _space_delimited_lowercase_name_to_asset_name(self, space_delimited_lowercase_name):
        asset_name = FileProxy._space_delimited_lowercase_name_to_asset_name(
            self, space_delimited_lowercase_name)
        if not asset_name.endswith(self.extension):
            asset_name += self.extension
        return asset_name

    ### READ-ONLY PUBLIC PROPERTIES ###

    # TODO: change to class attribute
    @property
    def extension(self):
        return '.ly'
