import streamlit as st
import holoviews as hv
import st_holoview as sth

##################################################################################################
def st_ui():
	st.set_page_config(layout = "wide")

	st.title('Regional Gulf Coast model')

	hv_plot = sth.create_hv_plot()
	# st.session_state.rxy = rxy

	st.bokeh_chart(hv.render(hv_plot, backend='bokeh'))

if __name__ == "__main__":
	st_ui()
