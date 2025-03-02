import requests
from icalendar import Calendar
from datetime import datetime
import sys

def format_event_as_markdown(event):
    summary = event.get('SUMMARY')
    url = event.get('URL')
    start = event.get('DTSTART').dt
    end = event.get('DTEND').dt
    location = event.get('LOCATION')

    start_time = start.strftime("%I:%M %p") if isinstance(start, datetime) else "All Day"
    end_time = end.strftime("%I:%M %p") if isinstance(end, datetime) else "All Day"

    date_str = start.strftime("%A, %B %d, %Y") if isinstance(start, datetime) else "Unknown Date"

    markdown = ""
    if url:
        markdown += f"- [{summary}]({url}) - {start_time} - {end_time}, {location}\n" # Added dash and newline
    else:
        markdown += f"- {summary} - {start_time} - {end_time}, {location}\n"  # Added dash and newline
    return markdown

def parse_ical_to_markdown(ical_url):
    try:
        response = requests.get(ical_url)
        response.raise_for_status()

        cal = Calendar.from_ical(response.content)
        events_by_day = {}

        for event in cal.walk('VEVENT'):
            start = event.get('DTSTART').dt
            if not isinstance(start, datetime):
                start = datetime.combine(start, datetime.min.time())

            date_str = start.strftime("%Y-%m-%d")
            if date_str not in events_by_day:
                events_by_day[date_str] = {}
            time_str = start.strftime("%H:%M:%S")
            if time_str not in events_by_day[date_str]:
                events_by_day[date_str][time_str] = []
            events_by_day[date_str][time_str].append(event)

        markdown_output = ""
        for date_str in sorted(events_by_day.keys()):
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%A, %B %d, %Y")
            markdown_output += f"### {formatted_date}\n\n"

            for time_str in sorted(events_by_day[date_str].keys()):
                events = events_by_day[date_str][time_str]
                if len(events) > 1:
                    markdown_output += f"*Concurrent Events:*\n"
                    for event in events:
                        summary = event.get('SUMMARY')
                        event['SUMMARY'] = f"*{summary}*"
                        markdown_output += format_event_as_markdown(event)
                else:
                    for event in events:
                        markdown_output += format_event_as_markdown(event)

        return markdown_output

    except requests.exceptions.RequestException as e:
        return f"Error fetching iCal data: {e}"
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ical_url = sys.argv[1]
    else:
        ical_url = input("Enter the .ics URL: ")

    markdown = parse_ical_to_markdown(ical_url)
    print(markdown)
