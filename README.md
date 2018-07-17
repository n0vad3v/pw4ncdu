# Python Wrapper For NCDU

> ncdu 1.13, Python 3.6

# Goal

We need to help SAs to find large files in the given path.

# Considerations

* Since NCDU can do a great job for us, we still need a wrapper to make it more hackable.

* There might be some large files we want to exclude when scanning such as log files(with .log extension), so we need an option to exclude the specific file  pattern.

* For those who want to only show files bigger than known size, `pw4ncdu` provides a option to handle that.

# Usage

use `python3 pw4ncdu.py -h` for help.

`python3 pw4ncdu.py -p /path/for/scanning/ -e excluded_pattern -s only_show_files_with_size_bigger_than_mib`

# Test Case for coding.

We don't need the interactive UI for NCDU since we need further process by Python
example output with command`ncdu -xo- /home/Nova/Downloads/dosbox`
```
[
	1,
	1,
	{
		"progname": "ncdu",
		"progver": "1.13",
		"timestamp": 1528707036
	},
	[
		{
			"name": "/home/Nova/Downloads/dosbox",
			"asize": 4096,
			"dsize": 4096,
			"dev": 64770,
			"ino": 7086198
		},
		[
			{
				"name": "games",
				"asize": 4096,
				"dsize": 4096,
				"ino": 7220628
			},
			[
				{
					"name": "Prince",
					"asize": 4096,
					"dsize": 4096,
					"ino": 7086199
				},
				{
					"name": "VPALACE.DAT",
					"asize": 14226,
					"dsize": 16384,
					"ino": 7086228
				}
			]
		],
		[
			{
				"name": "code",
				"asize": 4096,
				"dsize": 4096,
				"ino": 7220629
			},
			{
				"name": "综合实验报告格式.doc",
				"asize": 14336,
				"dsize": 16384,
				"ino": 7220637
			}
		]
	]
]
```
