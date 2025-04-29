import sys, os
from streamlit.web import cli as stcli

def main():
    # đúng folder chứa script khi EXE unpack
    base = sys._MEIPASS if getattr(sys, "frozen", False) else os.path.dirname(__file__)
    script = os.path.join(base, "mo_phong_dashboard_chien_luoc.py")

    sys.argv = [
        "streamlit","run",
        "--global.developmentMode","false",
        "--server.port","8501",
        "--server.fileWatcherType","none",
        script
    ]
    sys.exit(stcli.main())

if __name__=="__main__":
    main()
