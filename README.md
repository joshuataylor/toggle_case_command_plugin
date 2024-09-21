# Toggle Case Command Plugin

Super simple Sublime Text 4 plugin to toggle case by Key Binding.

Copy `toggle_case_command.py` to `Packages/User/toggle_case_command.py`, or click `Tools > Developer > New Plugin...`,
and paste the contents of `toggle_case_command.py` into the new tab.

Key Bindings:

```json
[
  {
    "keys": [
      "super+l"
    ],
    "command": "toggle_case"
  }
]
```

FYI, the default upper/lower case commands for Key Bindings are:

```json
[
  {
    "keys": [
      "super+shift+u"
    ],
    "command": "upper_case"
  },
  {
    "keys": [
      "super+shift+l"
    ],
    "command": "lower_case"
  }
]
```
