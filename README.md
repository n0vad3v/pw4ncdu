# Python Wrapper For NCDU

> ncdu 1.13, Python 3.6

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
