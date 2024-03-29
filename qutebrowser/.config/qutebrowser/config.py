import glob
import os.path

# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401

config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

c.aliases = {
    "q": "quit",
    "w": "session-save",
    "wq": "quit --save",
    "x": "quit --save",
    "h": "help",
}

c.bindings.commands = {
    "command": {
        "<Ctrl-w>": "rl-filename-rubout",
        "<Ctrl-Shift-w>": "rl-rubout ' '",
    },
    "prompt": {
        "<Ctrl-w>": "rl-filename-rubout",
        "<Ctrl-Shift-w>": "rl-rubout ' '",
    },
}

c.confirm_quit = ["downloads"]

c.new_instance_open_target = "tab-silent"
c.new_instance_open_target_window = "last-focused"

c.window.hide_decoration = False

c.editor.command = [
    "footclient",
    "hx",
    "{file}:{line}:{column0}",
]

ranger = ["footclient", "ranger"]
c.fileselect.handler = "external"
c.fileselect.single_file.command = [*ranger, "--choosefile={}"]
c.fileselect.multiple_files.command = [*ranger, "--choosefiles={}"]
c.fileselect.folder.command = [*ranger, "--choosedir={}"]

c.auto_save.session = True

c.content.javascript.enabled = True
c.content.autoplay = False
c.content.pdfjs = True
c.content.netrc_file = "~/.netrc"
c.content.notifications.presenter = "libnotify"

c.completion.shrink = True
c.completion.scrollbar.width = 0
c.completion.scrollbar.padding = 0
c.completion.open_categories = ["quickmarks", "bookmarks", "history", "filesystem"]

c.hints.auto_follow = "always"
c.hints.mode = "letter"
if c.hints.mode == "number":
    c.hints.auto_follow_timeout = 400

c.search.incremental = False

c.tabs.background = True
c.tabs.favicons.scale = 0.9
c.tabs.last_close = "close"
c.tabs.padding = {"bottom": 4, "left": 3, "right": 3, "top": 4}
c.tabs.mode_on_change = "restore"
c.tabs.show = "multiple"
c.tabs.indicator.width = 0

c.url.open_base_url = True
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "ap": "https://archlinux.org/packages/?q={}",
    "aur": "https://aur.archlinux.org/packages.php?K={}",
    "a": "https://wiki.archlinux.org/?search={}",
    "d": "https://duckduckgo.com/?q={}",
    "gi": "https://github.com/search?q={}",
    "ho": "https://www.haskell.org/hoogle/?hoogle={}",
    "ji": "http://jisho.org/search/{}",
    "ra": "https://rateyourmusic.com/search?searchtype=a&searchterm={}",
    "wikt": "https://en.wiktionary.org/wiki/Special:Search?search={}",
    "w": "https://en.wikipedia.org/wiki/Special:Search?search={}",
    "y": "https://youtube.com/results?search_query={}",
}

c.fonts.default_family = ["Fantasque Sans Mono", "monospace"]
c.fonts.default_size = "14pt"

# c.fonts.completion.entry = mono
# c.fonts.completion.category = 'bold default_size default_family'
# c.fonts.debug_console = mono
# c.fonts.downloads = mono
c.fonts.hints = "bold 13pt default_family"
c.fonts.prompts = "13pt sans_serif"
# c.fonts.keyhint = mono
# c.fonts.messages.error = mono
# c.fonts.messages.info = mono
# c.fonts.messages.warning = mono
# c.fonts.statusbar = mono
# c.fonts.tabs = mono

config.bind(",d", "hint all delete")
config.bind(",r", "set-cmd-text :open {url:domain}/")
config.bind(",R", "set-cmd-text :open -t {url:domain}/")
config.bind("xP", "open -b -- {primary}")
config.bind("xp", "open -b -- {clipboard}")
config.bind("pw", "open https://en.wikipedia.org/wiki/Special:Search?search={primary}")
config.bind(
    "Pw", "open -t https://en.wikipedia.org/wiki/Special:Search?search={primary}"
)
config.bind(
    "PW", "open -b https://en.wikipedia.org/wiki/Special:Search?search={primary}"
)
config.bind(";x", "hint links spawn -dv umpv --profile=no-term {hint-url}")
config.bind("X", "spawn -dv umpv --profile=no-term {url}")
config.bind("<Ctrl+e>", "run-with-count 3 scroll down")
config.bind("<Ctrl+y>", "run-with-count 3 scroll up")
PASS_CMD = (
    "qute-pass --username-target secret "
    "--username-pattern '(?:username|email): (.+)' "
    "--dmenu-invocation 'fuzzel --dmenu'"
)
config.bind("zl", f"spawn --userscript {PASS_CMD}")
config.bind("zul", f"spawn --userscript {PASS_CMD} --username-only")
config.bind("zpl", f"spawn --userscript {PASS_CMD} --password-only")

config.load_autoconfig()

for f in glob.glob(str(config.configdir / "conf.d" / "*.py")):
    config.source(str(os.path.relpath(f, start=config.configdir)))
