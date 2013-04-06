from abjad.tools import stringtools
from scf.wranglers.PackageWrangler import PackageWrangler
from scf.proxies.ScorePackageProxy import ScorePackageProxy
import os


class ScorePackageWrangler(PackageWrangler):

    def __init__(self, session=None):
        PackageWrangler.__init__(self,
            score_external_asset_container_importable_names=[],
            score_internal_asset_container_importable_name_infix=None,
            session=session)

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def asset_class(self):
        return ScorePackageProxy

    @property
    def breadcrumb(self):
        return 'scores'

    @property
    def current_asset_container_path_name(self):
        return self.scores_directory_name

    @property
    def visible_score_titles_with_years(self):
        result = []
        for score_package_proxy in self.list_visible_asset_proxies():
            result.append(score_package_proxy.title_with_year or '(untitled score)')
        return result

    ### PUBLIC METHODS ###

    def handle_main_menu_result(self):
        self.print_not_yet_implemented()

    def list_visible_asset_path_names(self, head=None):
        result = []
        for visible_asset_proxy in self.list_visible_asset_proxies(head=head):
            result.append(visible_asset_proxy.path_name)
        return result

    def list_visible_asset_proxies(self, head=None):
        result = []
        scores_to_show = self.session.scores_to_show
        for asset_proxy in PackageWrangler.list_asset_proxies(self, head=head):
            is_mothballed = asset_proxy.get_tag('is_mothballed')
            if scores_to_show == 'all':
                result.append(asset_proxy)
            elif scores_to_show == 'active' and not is_mothballed:
                result.append(asset_proxy)
            elif scores_to_show == 'mothballed' and is_mothballed:
                result.append(asset_proxy)
        return result

    def list_visible_asset_short_names(self, head=None):
        result = []
        for path_name in self.list_visible_asset_path_names(head=head):
            result.append(os.path.basename(path_name))
        return result

    def make_asset_interactively(self, rollback=False):
        breadcrumb = self.pop_breadcrumb(rollback=rollback)
        getter = self.make_getter(where=self.where())
        getter.indent_level = 1
        getter.prompt_character = ':'
        getter.capitalize_prompts = False
        getter.include_newlines = False
        getter.number_prompts = True
        getter.append_string('score title')
        getter.append_underscore_delimited_lowercase_package_name('package name')
        getter.append_integer_in_range('year', start=1, allow_none=True)
        result = getter.run()
        if self.backtrack():
            return
        title, score_package_short_name, year = result
        self.make_asset(score_package_short_name)
        score_package_proxy = self.get_asset_proxy(score_package_short_name)
        score_package_proxy.add_tag('title', title)
        score_package_proxy.year_of_completion = year
        self.push_breadcrumb(breadcrumb=breadcrumb, rollback=rollback)

    def make_main_menu(self):
        self.print_not_yet_implemented()

    def make_visible_asset_menu_tokens(self, head=None):
        keys = self.list_visible_asset_importable_names()
        bodies = self.visible_score_titles_with_years
        menuing_pairs = zip(keys, bodies)
        tmp = stringtools.strip_diacritics_from_binary_string
        menuing_pairs.sort(lambda x, y: cmp(tmp(x[1]), tmp(y[1])))
        return menuing_pairs