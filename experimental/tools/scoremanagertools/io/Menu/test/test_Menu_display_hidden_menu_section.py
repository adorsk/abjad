from experimental import *



def test_Menu_display_hidden_menu_section_01():

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    score_manager._run(pending_user_input='hidden q')
    assert score_manager._session.transcript[-2][1] == \
        ['     back (b)',
         '     exec statement (exec)',
         '     grep directories (grep)',
         '     edit client source (here)',
         '     display hidden menu section (hidden)',
         '     home (home)',
         '     next score (next)',
         '     prev score (prev)',
         '     quit (q)',
         '     redraw (r)',
         '     current score (score)',
         '     toggle menu commands (tmc)',
         '     toggle where-tracking (twt)',
         '     display calling code line number (where)',
         '',
         '     show active scores only (active)',
         '     show all scores (all)',
         '     fix all score package structures (fix)',
         '     show mothballed scores only (mb)',
         '     profile packages (profile)',
         '     run py.test on all scores (py.test)',
         '     work with repository (svn)',
         '     write cache (wc)',
         '']


def test_Menu_display_hidden_menu_section_02():

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    score_manager._run(pending_user_input='red~example~score hidden q')

    assert score_manager._session.transcript[-2][1] == \
        ['     back (b)',
        '     exec statement (exec)',
        '     grep directories (grep)',
        '     edit client source (here)',
        '     display hidden menu section (hidden)',
        '     home (home)',
        '     next score (next)',
        '     prev score (prev)',
        '     quit (q)',
        '     redraw (r)',
        '     current score (score)',
        '     toggle menu commands (tmc)',
        '     toggle where-tracking (twt)',
        '     display calling code line number (where)',
        '',
        '     fix package structure (fix)',
        '     list directory contents (ls)',
        '     profile package structure (profile)',
        '     run py.test (py.test)',
        '     remove score package (removescore)',
        '     manage repository (svn)',
        '     manage tags (tags)',
        '']