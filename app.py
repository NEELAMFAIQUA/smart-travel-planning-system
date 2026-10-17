import streamlit as st

from planner import DESTINATIONS, plan_with_agents

st.set_page_config(page_title="Travel Day Planner", page_icon="🧭")
st.title("Travel Day Planner")
st.caption("Create a simple sample itinerary from locally bundled ideas.")
destination = st.selectbox("Destination", list(DESTINATIONS))
days = st.slider("Trip length (days)", 1, 7, 3)
interests = st.multiselect("Interests", ["culture", "food", "nature"])
budget = st.number_input("Total trip budget ($)", min_value=100, max_value=30000, value=1500, step=100)

plan = plan_with_agents(destination, days, interests, budget)
st.subheader(f"{days}-day plan for {destination}")
for activity in plan["itinerary"]:
    st.markdown(
        f"**Day {activity['day']} — {activity['name']}**  \n"
        f"{activity['interest'].title()} · sample activity estimate ${activity['cost']}"
    )
budget_breakdown = plan["budget"]
st.subheader("Planning-team budget estimate")
st.dataframe(
    [
        {"Category": "Activities", "Estimate": budget_breakdown["activities"]},
        {"Category": "Food", "Estimate": budget_breakdown["food"]},
        {"Category": "Local transport", "Estimate": budget_breakdown["local_transport"]},
        {"Category": "Sample lodging", "Estimate": budget_breakdown["sample_lodging"]},
        {"Category": "Total", "Estimate": budget_breakdown["total"]},
    ],
    hide_index=True,
)
if budget_breakdown["within_budget"]:
    st.success(f"Estimated ${budget_breakdown['total']} — within your ${budget} budget.")
else:
    st.warning(f"Estimated ${budget_breakdown['total']} — above your ${budget} budget.")
with st.expander("Planning team handoffs"):
    for agent in plan["agents"]:
        st.markdown(f"**{agent['role']}** — {agent['result']}")
st.info(
    "Planner roles are transparent local demo steps, not remote AI services. "
    "All activities and costs are illustrative; no live travel data, bookings, "
    "reservations, or price quotes are provided."
)
