import streamlit as st

from streamlit_calendar import calendar
from datetime import datetime

if __name__ == "__main__":

    today_date = datetime.today().strftime('%d-%m-%Y')

    st.markdown("<h1 style='text-align: center;'>Prenotazioni Campetto</h1>",
                unsafe_allow_html=True)

    # HTML layout with divs and flexbox to align the h4 text and the current date
    html_layout = f"""
    <div style='display: flex; justify-content: space-between; width: 100%;'>
        <div style='text-align: left;'>
            <h4>Nuovo Stadio Comunale</h4>
        </div>
        <div style='text-align: right;'>
            <h4>Oggi, {today_date.replace('-', '/')}</h4>
        </div>
    </div>
    """

    # Render the HTML layout
    st.markdown(html_layout, unsafe_allow_html=True)

    calendar_options = {
        "editable": "true",
        "selectable": "true",
        "headerToolbar": {
            "left": "",
            "center": "",
            "right": "",
        },
        "slotMinTime": "14:00",
        "slotMaxTime": "22:00",
        "initialView": "timelineDay",
        'slotDuration': "01:00:00",
        "contentHeight": 61
    }

    calendar_events = [
        {
            "title": "Frasconà",
            "start": "2024-10-15T15:00:00",
            "end": "2024-10-15T15:00:00",
            "backgroundColor": "#FF4B4B",
            "borderColor": "#FF4B4B",
            "resourceId": "a",
        },
        {
            "title": "Greco",
            "start": "2024-10-15T17:00:00",
            "end": "2024-10-15T18:00:00",
            "backgroundColor": "#FF4B4B",
            "borderColor": "#FF4B4B",
            "resourceId": "a",
        }
    ]

    custom_css = """
        .fc-event-past {
            opacity: 0.6;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
    """

    calendar = calendar(events=calendar_events,
                        options=calendar_options, custom_css=custom_css)
    try:
        if calendar["callback"] == "dateClick":
            date_str = calendar["dateClick"]["date"]
            date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))

            TIMEZONE_OFFSET = 2

            start_hour = date_obj.hour + TIMEZONE_OFFSET
            end_hour = date_obj.hour + TIMEZONE_OFFSET + 1

            with st.form("confirmation"):
                st.markdown(f"<h4 style='text-align: center;'>Hai selezionato dalle {start_hour} alle {end_hour}.</h4>",
                            unsafe_allow_html=True)
                st.markdown("<h4 style='text-align: center;'>Inserisci il tuo cognome e il tuo numero di cellulare per confermare:</h4>",
                            unsafe_allow_html=True)
                st.text_input("Cognome:")
                st.text_input("Numero di cellulare:", value="+39")
                submit_button = st.form_submit_button("Conferma")

        if calendar["callback"] == "eventClick":
            st.markdown("<h4 style='text-align: center;'>Hai selezionato uno slot occupato. Scegli uno slot libero.</h4>",
                            unsafe_allow_html=True)
    except KeyError:
        pass

    # st.write(calendar)
