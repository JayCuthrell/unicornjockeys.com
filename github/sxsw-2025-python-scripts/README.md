# sxsw-2025-python-scripts
Simple python scripts for parsing SXSW 2025 Schedules 

Each python script was written using Google Gemini (with significant errors) and tested in a virtual environment on OS Version: macOS 14.5 build 23F79 using omz (fa583cfb) and Python 3.12.4 with the following pip3 list

- certifi            2024.7.4
- charset-normalizer 3.3.2
- colored            2.2.4
- data-printer       0.0.8
- dist-info          0.1.1
- idna               3.7
- Jinja2             3.1.4
- MarkupSafe         2.1.5
- pip                24.1.2
- pyproject          1.3.1
- python-dateutil    2.9.0.post0
- python-dotenv      1.0.1
- pytz               2024.1
- requests           2.32.3
- setuptools         70.3.0
- six                1.16.0
- urllib3            2.2.2
- DateTime           5.5
- zope.interface     6.4.post2

## Scripts

- build_schedule.py - download ICS file and parse to create a markdown format blog that can be piped to pbcopy
