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
		  <source src="https://rr4---sn-gvnuxaxjvh-c35z.googlevideo.com/videoplayback?expire=1686269230&ei=zhiCZJXvB-P7zLUP3K6SeA&ip=5.182.110.165&id=o-AOMElUbQqPajhZX5aErHwivnMyjp6i6a4uDOp4L6B3c8&itag=399&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&spc=qEK7B7Pbxq1VUrzvbs7fHjl6u6WKTaCFFP3qRYtBLA&vprv=1&svpuc=1&mime=video%2Fmp4&ns=NXLw4J-BddEHxlAHSqJEAZAN&gir=yes&clen=198203522&dur=3609.999&lmt=1630799721330343&keepalive=yes&fexp=24007246,24350018,51000011&beids=24350018&c=WEB&txp=5432434&n=qTHryvAvH9uy7A&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgMOr2k93xnKlQJTWwD400i4MLLRM7EjtE5MegwNmDkqECIQDOrlXOzYVXJZHHUG4jKkur9BYeQZWVRvj8kF0zse7jEg%3D%3D&redirect_counter=1&rm=sn-vgqee776&req_id=9fc7062719efa3ee&cms_redirect=yes&cmsv=e&ipbypass=yes&mh=D8&mip=5.228.41.215&mm=31&mn=sn-gvnuxaxjvh-c35z&ms=au&mt=1686247277&mv=m&mvi=4&pcm2cms=yes&pl=21&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pcm2cms,pl&lsig=AG3C_xAwRQIgTj1QLulfeB4eyrjf3vVnn4YAhZgSSDckaKESfmGwLh0CIQCDhcJaLoz9B45N-6cBAS52R3k9vbyeQsDTjhIAAtWA0w%3D%3D")>
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
