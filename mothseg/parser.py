from cvargparse import BaseParser
from cvargparse import Arg

def parse_args():
    parser = BaseParser([
        Arg("folder"),
        Arg("config"),

        Arg("--output", "-o"),

        Arg.flag("--yes", "-y"),
        Arg.flag("--force", "-f"),

        Arg.flag("--plot_interm"),
        Arg.flag("--use_timestamp", "-use_ts"),

        Arg.flag("--raise_on_error", "-raise"),

        Arg.int("--n_jobs", "-j", default=1),
    ])

    return parser.parse_args()
