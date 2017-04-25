# Sublime Text3配置文件

### Settings:

```json
{
    "color_inactive_tabs": true,
    "color_scheme": "Packages/User/SublimeLinter/Monokai (SL).tmTheme",
    "default_encoding": "UTF-8",
    "draw_white_space": "all",
    "font_size": 14.0,
    "highlight_line": true,
    "ignored_packages":
    [
        "Markdown",
        "Vintage"
    ],
    "line_numbers": true,
    "line_padding_bottom": 1,
    "line_padding_top": 1,
    "scroll_past_end": false,
    "shift_tab_unindent": true,
    "sidebar_size_13": true,
    "status_bar_brighter": true,
    "tab_size": 4,
    "tabs_label_not_italic": true,
    "tabs_medium": true,
    "tabs_padding_medium": true,
    "theme": "Afterglow-blue.sublime-theme",
    "translate_tabs_to_spaces": true,
    "update_check": true,
    "word_wrap": true
}
```

### Key Bindings:

```json
[
    {
        "keys": ["ctrl+shift+c"],
        "command": "copy_path"
    },
    {
        "keys": ["ctrl+alt+j"],
        "command": "Pretty JSON: Format (Pretty Print) JSON"
    },
    {
        "keys": ["alt+d"],
        "command": "delete_trailing_spaces"
    },
    {
        "keys": ["alt+t"],
        "command": "toggle_trailing_spaces"
    },
    {
        "keys": ["alt+p"],
        "command": "sublime_tmpl", "args": {"type": "python"}
    },
    {
        "keys": ["alt+x"],
        "command": "close_file"
    },
    {
        "keys": ["f1"],
        "command": "side_bar_files_open_with", "args": {"extensions": ".*", "paths": [], "application": "C:\\Program Files\\Internet Explorer\\iexplore.exe"}
    },
    {
        "keys": ["f2"],
        "command": "side_bar_files_open_with", "args": {"extensions": ".*", "paths": [], "application": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"}
    },
]
```

### Installed Package:

```
BracketHighlighter
FileDiffs
Keymaps
Monokai Extended
Package Control
Predawn Monokai
Predawn
Pretty JSON
OmniMarkupPreviewer
Python PEP8 Autoformat
SideBarEnhancements
SublimeLinter
SublimeLinter-pylint
SublimeCodeIntel
SublimeTmpl
Theme - Afterglow
Theme - Soda
TortoiseSVN
Terminal
TrailingSpaces
```
### Package Control无法安装插件：

>打开 Sublime Text 3，在菜单栏中选择：Preferences → Package settings → Package Control → Settings – User

```
"channels": [
        "https://git.oschina.net/mugood/PackageControl/raw/master/channel_v3.json"
    ],
```