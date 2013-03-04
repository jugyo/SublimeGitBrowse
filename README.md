GitBrowse
====

Sublime Text 2 plugin to browse code on browser.

# Usage

Add setting to `Preferences.sublime-settings`:

```
{
  "git_browse":
  {
    "url": "https://xxxxx.com/:dir/tree/:file?h=:branch#n:line"
  }
}
```

or `.sublime-project`:

```
{
  "settings": {
    "git_browse":
    {
      "url": "https://xxxxx.com/:dir/tree/:file?h=:branch#n:line"
    }
  }
}
```

Execute `git_browse` command by using the Command Pallet.
