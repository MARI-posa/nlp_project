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
		  <source src="https://rr1---sn-p5qddn7k.googlevideo.com/videoplayback?expire=1686241935&ei=L66BZNrqIMyk1gL8k7WYBw&ip=195.146.4.71&id=o-ACQGiFTQT9zSqkQN4h25fAzhZMe6qZOWIIpIyGr73cBD&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&spc=qEK7B4Ajz-YTBetD_q7arLcAD-_2Wp8uykt3IvqeDw&vprv=1&svpuc=1&mime=video%2Fmp4&ns=MXqQN23hmr3WGimsk9x_7X8N&gir=yes&clen=319656408&dur=3610.000&lmt=1607152879559618&keepalive=yes&fexp=24007246,24350017,51000023&beids=24350017&c=WEB&txp=5432434&n=uo3cc0_vHY-kPw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIjEwtX81aPmadQx2XmDlMcVouC05-QPJPqyqzkuuTLaAiEA-tv5uIzuSYMAMbx9Kmu70zxhie3AbbT__up_TPMPEJg%3D&redirect_counter=1&rm=sn-4g5erl76&req_id=87ca94ed90a0a3ee&cms_redirect=yes&cmsv=e&ipbypass=yes&mh=D8&mip=162.255.44.118&mm=31&mn=sn-p5qddn7k&ms=au&mt=1686221519&mv=u&mvi=1&pl=24&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRgIhAN2wmu80rRefhfzquLHfXk-DNtZkmLB7C7Loh6qQOqrHAiEArWpdQHSmn0R2VP1H2xczNc5bCP5CBroUorzIJzQVlg8%3D")>
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
