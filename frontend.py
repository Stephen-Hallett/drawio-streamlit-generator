import streamlit as st
from code_generator import generate_streamlit
from code_editor import code_editor
from io import StringIO

def save_to_py(code):
    if len(code["text"]):
        saved_code = code["text"]
    else:
        saved_code = st.session_state.code
    with open("app.py", "w") as f:
        f.write(saved_code)
    st.success("File saved!")


st.set_page_config(layout="wide")

btn_settings_editor_btns  = [{
    "name": "Copy",
    "feather": "Copy",
    "hasText": True,
    "alwaysOn": True,
    "commands": ["copyAll"],
    "style": {"top": "0rem", "right": "4.3rem"}
  },
  {
    "name": "Save",
    "feather": "Save",
    "hasText": True,
    "alwaysOn": True,
    "commands": [
      "save-state",
      [
        "response",
        "saved"
      ]
    ],
    "response": "saved",
    "style": {"top": "0rem", "right": "0.4rem"}
  }]

st.title("Streamlit Code Generator")
st.divider()
col0, col1 = st.columns([370, 340])
with col0:
    st.markdown(body="""<iframe frameborder="0" style="width:100%;height:643px;" src="https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1#R7Ztbd9o4EMc%2FDY%2F46G75MSRp2u223dN0m7P75osAb43tNXZC%2Buk78gVsrJBNgHLZknOCGcm2ND%2FNzF8OGdDL2eImc9PphyRQ0YCgYDGgVwNCMCYc3rTlsbLYrDZMsjCoO60Mt%2BF3VRtRbS3CQM07HfMkifIw7Rr9JI6Vn3dsbpYlD91u4yTq3jV1J6pnuPXdqG%2B9C4N8WlklRyv7WxVOps2dGapbZm7TuTbMp26QPLRM9HpAL7Mkyauj2eJSRdp5jV%2Bq89480bocWKbi%2FL%2BcECSTD2mS3v0jb2xveO95V38%2FDml1lXs3KuoJD4iI4HqjAs4VE33UWKJw3TJP3VjPLH%2Bs3SX%2BLfR0RuMkzofzEuYFdCAsXZSnobLhoXaYbrLBX2VLrhb50I3CSVw1%2BDAtlbXaHmCBVU1xUh2PVjdsRjYq56E73U0TGBRBt36mVNyMGNxTDbo7ETD3Z3cK870pJ1f2uoRbuWEM1zjTuX7K3HhS3%2FUWsoLnns1Ukef63yZZUsTB0E%2BiJKt6hHGYh25k9MYfRZZGqkEfFbN4%2Fow3vOxk%2FbM%2B%2Bb8gtelcqrt9CXMd6OexENYn%2BlkFVZ93cVrk8K4iNYMrPcd62wk%2Fvx7Ra31iDoAN7lr3yd00zOubXsSP%2BjruDNykNcAsTWJdDncSCGBsF0HScRTRA9YezLPkm7qsfHQVw%2B31cgmjaM00zWfgtysMhw96%2FLep6%2Bsr1R64V1keguq4qDxwNQuDQN9plEDLuFzrV1Ow6WQ%2F6lf%2BWgzoq6hFy1QrgRuVzFSeaV89rEQMa0TMtCVglnLFrYXTZHnuSlvAQS0vzFLj8%2FVbmQ6lN2W3X78X9PP70V0xZD2p8fHTl%2BuaY3k6%2BLLw8yJzozbMeamdkiLSiD1d0qPEd%2FOSeBjPoRDo0cbw8Q04nKAkLjViqg%2FH%2BnCqO3j6rjrPzvXbvBYFTThZ1VrKp2E80db7stHVXg4XpaJNiry%2BVX1RNy%2B9WQ68HFWmZgArsHorpQwjHcdX6An6rcWxDdu6lQlp1SK7Ft0N0xZ8inDTadrVr9vjv3nHPSU%2FXn8YfRzFowKTxbfxEPfwb%2BeodowNCA1cJcd%2BLyChRfhSeWNoCWcg1i%2FmabVNwI2lkfWEgcVfiqhqELvAgbosWB%2BGLQyRuNxJ7BwF2S%2BK8VgJ34gisB2vrAXHiwLb3KKSCcyr3%2Bxngunvxr6oWRpBstOSN8%2BUO4tCnXcu0nQDsqeKzCZkY%2FIEMuEJLg6HjGC5xoz0mHFpCB%2BxL0j9OjaPoDJk2wF5jXvXIUpfmSF6kutivxMgnFnL4Ch%2Fd%2FBQU0gxYXXOEAbZASXLxozI5jfdEz3%2Bi94GepJYssXBOW6W4hfLp1kywq02BXncLLHdg1m6fTtlcqCitZmMbibtMHsdGm5bbTBwyvZojBu3Fyn3l2sPhQOubFOwOMKm7iG1B%2BnqRVNx02FGsSFwnB3oD%2BMj%2Bz3jABgyYCYcknhUHBSH081w0raaybeJIG4J2SeCKbeY3Ff6cv7HVCxJ1uKEW9J%2BARjbQjtIXl%2FfUxn9Wdz9lt6NR7b9u%2F%2Fdnbxsr7uX5LUDH1ObWtwBPyFKGF5uSht3CwyVgKLli%2FbrCRYWc5DjICEociQz1BOMkWUTBLVEVC%2B%2Bp1g5p0qvFbMtGMKYOA6jfE1PCxACiK5evEfGkcDOwRxEAWBuMlyHC6KWBHSr155CpS%2BnTzBUOGIW45QJSrBNBV%2BLFeY4FgdRBeCeInKoWDEy6W9XT5DJ5vR1xEjMpR6dUf7imFqCOJxJBB8c2VVYHFIPwmL1Our81X8wd4KxAhsKWMYOsW2o6FJwetqx0t%2BsnG6sbK71RxsrZjB9XXy6YCCLWRJWus24LYjdzO3YwRiT2OEftuwkiYG3mOTQjxNJHbsD5Ij3K0Ykpu9InhySZ3TxETMx568%2BlHPNX0e7iTSD6auw0wWzWR0fLRjjU%2FzDPwg7EEQhnn%2BKj6npq3C7eIRvDBJ5RjEibASFZfWzlrzKR8Et9dV%2FLIyRYyGn9WMbooRKi%2BFWqO0JTP8p%2FrmC4fr7f7KlitnrwBDQDbjFd18izLCTDML7Z%2F7a%2F3O%2Bb7n%2BtTKKmcX765wzQ47B3GIvX8zwcfV%2FQ2Vb67%2Bv6PUP"></iframe>""", unsafe_allow_html=True)
    file = st.file_uploader(label="Upload XML",  type=[".xml"])
with col1:
    if file is not None:
        content = file.getvalue().decode('utf-8')
        print(content)
    else:
        with open("template.xml", 'rb') as f:
            content = f.read()
    st.session_state["code"] = generate_streamlit(content)
    code_string = code_editor(st.session_state.code, buttons=btn_settings_editor_btns, height=26, allow_reset=True, focus=True, key="code_editor")
    st.button(label="Download code to app.py", use_container_width=True, type="secondary", on_click=save_to_py, args=(code_string,), help="Remember to click \"Save\" before you download!")