import argparse
import os
import sys
import traceback
from abjad.tools.developerscripttools.DeveloperScript import DeveloperScript


class AbjadBookScript(DeveloperScript):

    ### PUBLIC PROPERTIES ###

    @property
    def alias(self):
        return 'book'

    @property
    def long_description(self):
        return '''DESCRIPTION

    abjad-book processes Abjad snippets embedded in HTML, LaTeX, or ReST
    documents. All Abjad code placed between the <abjad> </abjad> tags in 
    either HTML, LaTeX or ReST type documents is executed and replaced with 
    tags appropriate to the given file type. All output generated by the 
    code snippet is captured and inserted in the output file.

    Apart from the special opening and closing Abjad tags, abjad-book also
    has a special line-level suffix tag: `<hide`. All lines ending with the
    `<hide` tag will be interpreted by Abjad but will not be displayed in the
    OUTPUT document.

    The opening <abjad> tag can also be followed by a list of 
    `attribute=value` pair.

    You can make all of an Abjad code block invisible in the output file with
    the following opening tag:

    <abjad>[hide=true]

    This is useful for generating and embedding rendered score images without
    showing any of the Abjad code.

    You can also remove all of the prompts from a code block with the 
    following opening tag:

    <abjad>[strip_prompt=true]

    Simply use Abjad's show() function to have Abjad call LilyPond on the 
    Abjad snippet and embed the rendered image in the document.

    All Abjad snippets *must* start with no indentation in the document.

EXAMPLES

    1.  Create an HTML, LaTex or ReST document with embedded Abjad code
        between <abjad></abjad> tags. The code *must* be fully flushed
        to the left, with no tabs or spaces. The content of an HTML file
        with embedded Abjad might look like this:

        This is an <b>HTML</b> document. Here is Abjad code:

        <abjad>
        v = Voice("c'4 d'4 e'4 f'4")
        beamtools.BeamSpanner(v)
        show(v)
        </abjad>

        More ordinary <b>HTML</b> text here.

   2.  Call `abjad-book` on the file just created:

        $ abjad-book file.htm.raw
    '''

    ### PRIVATE METHODS ###

    def _collect_filenames(self, args):
        filenames = []
        if os.path.isdir(args.path):
            for root, dirs, files in os.walk(args.path):
                for file in files:
                    path = os.path.join(root, file)
                    if self._is_valid_path(path):
                        filenames.append(path)
        else:
            filenames.append(args.path)
        return filenames

    def _is_valid_path(self, path):
        if not os.path.exists(path):
            return False
        if os.path.isfile(path) and \
            path.endswith('.raw') and \
            path.rpartition('.raw')[0].rpartition('.')[-1] in \
            self.output_formats:
            return True
        if os.path.isdir(path):
            return True
        return False

    def _process_filename(self, args, filename):
        from abjad.tools import abjadbooktools
        input_filename = filename
        print 'Processing {!r}...'.format(os.path.relpath(input_filename))
        try:
            directory = os.path.dirname(input_filename)
            output_filename = input_filename.rpartition('.raw')[0]
            file_extension = output_filename.rpartition('.')[-1]
            image_prefix = os.path.basename(output_filename).rpartition('.')[0]
            with open(input_filename, 'r') as f:
                lines = f.read().split('\n')
            output_format = self.output_formats[file_extension]()
            abjad_book_processor = abjadbooktools.AbjadBookProcessor(
                directory, lines, output_format,
                skip_rendering=args.skip_rendering, image_prefix=image_prefix,
                verbose=args.verbose)
            processed_lines = abjad_book_processor(verbose=args.verbose)
            print '\tWriting output to {!r}...'.format(
                os.path.relpath(output_filename))
            with open(output_filename, 'w') as f:
                f.write(processed_lines)
            print '\t...Done!'
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exc()

    def _validate_path(self, path):
        message = '{!r} is not a valid path.'.format(path)
        error = argparse.ArgumentTypeError(message)
        path = os.path.abspath(path)
        if not self._is_valid_path(path):
            raise error
        return path

    ### PUBLIC PROPERTIES ###

    @property
    def output_formats(self):
        from abjad.tools import abjadbooktools
        return {
            'htm': abjadbooktools.HTMLOutputFormat,
            'html': abjadbooktools.HTMLOutputFormat,
            'rst': abjadbooktools.ReSTOutputFormat,
            'tex': abjadbooktools.LaTeXOutputFormat,
        }

    @property
    def short_description(self):
        return 'Preprocess HTML, LaTeX or ReST source with Abjad.'

    @property
    def version(self):
        return 2.0

    ### PUBLIC METHODS ###

    def process_args(self, args):
        for filename in self._collect_filenames(args):
            self._process_filename(args, filename)
        flags = []
        if args.mainline:
            flags.append('-M')
        if args.experimental:
            flags.append('-X')
        if flags:
            developerscripttools.BuildApiScript()(flags)

    def setup_argument_parser(self, parser):

        parser.add_argument('path',
            type=self._validate_path,
            help='the path to process: a filename ending in ".raw" or '
            'an arbitrarily-deep directory tree to be recursed over'
            )

        parser.add_argument('--skip-rendering',
            action='store_true',
            help='skip all image rendering and simply execute the code',
            )

        parser.add_argument('--verbose',
            action='store_true',
            dest='verbose',
            help='run in verbose mode, printing all LilyPond output',
            )

        parser.add_argument('-X', '--experimental',
            action='store_true',
            help='rebuild abjad.tools docs after processing',
            )

        parser.add_argument('-M', '--mainline',
            action='store_true',
            help='rebuild mainline docs after processing',
            )
