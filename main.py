import streamlit as st

st.set_page_config(layout="wide")

video_html = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: relative; /* Изменено на position: relative; */
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}

		[data-testid="stToolbar"] {
			right: 2rem;
		}

		div.css-d6uc01.e1tzin5v0 {
			background-color: rgba(238, 238, 238, 0.5);
			border: 10px solid #EEEEEE;
			padding: 5% 5% 5% 10%;
			border-radius: 5px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://streamable.com/6rr9i5")>
		  Your browser does not support HTML5 video.
		</video>
"""

st.markdown(video_html, unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,5,2])

with col2:
    st.title('✨NLP Project by GPT-Team✨')

col1, col2, col3 = st.columns([2,5,2])

with col2:
    st.markdown("<div style='text-align: center; font-size: 30px;'>Team members:</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; font-size: 25px;'>✨ Maria K.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✨ Osana B.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; font-size: 25px;'>✨ Veronika K.&nbsp;&nbsp;&nbsp;&nbsp;✨ Anna S.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; font-size: 25px;'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; font-size: 25px;'></div>", unsafe_allow_html=True)
