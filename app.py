import streamlit as st

from planner import DESTINATIONS, build_itinerary, estimate_total

st.set_page_config(page_title="Travel Day Planner", page_icon="🧭")
st.title("Travel Day Planner")
st.caption("Create a simple sample itinerary from locally bundled ideas.")
destination = st.selectbox("Destination", list(DESTINATIONS))
days = st.slider("Trip length (days)", 1, 7, 3)
interests = st.multiselect("Interests", ["culture", "food", "nature"])
food = st.slider("Illustrative food budget per day", 0, 150, 35)

itinerary = build_itinerary(destination, days, interests)
st.subheader(f"{days}-day plan for {destination}")
for activity in itinerary:
    st.markdown(
        f"**Day {activity['day']} — {activity['name']}**  \n"
        f"{activity['interest'].title()} · sample activity estimate ${activity['cost']}"
    )
total = estimate_total(itinerary, food)
st.metric("Illustrative trip activity + food estimate", f"${total}")
st.info(
    "Excludes lodging, transport, taxes, and fees. All amounts and activities are "
    "examples; no live travel data, bookings, or reservations are provided."
)
