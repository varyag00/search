# Search

This script recursively searches for text within the specified directory.

## Usage
```
$ python search.py search_dir search_text

> ---------- MATCH ----------
> file: search_dir/test
> line: 0
> text: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet risus nullam eget felis eget nunc. Turpis cursus in hac habitasse platea dictumst quisque sagittis purus. Et netus et malesuada fames ac turpis. Aliquam id diam maecenas ultricies mi eget mauris pharetra et. Nibh ipsum consequat nisl vel pretium lectus quam. Felis eget nunc lobortis mattis aliquam faucibus purus in. Felis imperdiet proin fermentum leo vel orci porta non. Quis lectus nulla at volutpat. Dolor sit amet consectetur adipiscing. Non arcu risus quis varius. Porttitor massa id neque aliquam vestibulum morbi blandit. Nunc sed augue lacus viverra vitae congue eu. Fames ac turpis egestas sed tempus urna et. Ut tellus elementum sagittis vitae. Risus quis varius quam quisque id diam vel quam.
```
Or:
```
python search.py

> Enter directory to search for: test_dir
> Enter text to search for: Lorem

> ---------- MATCH ----------
> file: search_dir/test
> line: 0
> text: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet risus nullam eget felis eget nunc. Turpis cursus in hac habitasse platea dictumst quisque sagittis purus. Et netus et malesuada fames ac turpis. Aliquam id diam maecenas ultricies mi eget mauris pharetra et. Nibh ipsum consequat nisl vel pretium lectus quam. Felis eget nunc lobortis mattis aliquam faucibus purus in. Felis imperdiet proin fermentum leo vel orci porta non. Quis lectus nulla at volutpat. Dolor sit amet consectetur adipiscing. Non arcu risus quis varius. Porttitor massa id neque aliquam vestibulum morbi blandit. Nunc sed augue lacus viverra vitae congue eu. Fames ac turpis egestas sed tempus urna et. Ut tellus elementum sagittis vitae. Risus quis varius quam quisque id diam vel quam.
```

## Performance

This version of the script naively searches for the search text, storing every file in memory while doing so.
As a result, it grows linearly with input size both in terms of memory and runtime.

- Runtime: `O(n)`
- Memory: `O(n)`
