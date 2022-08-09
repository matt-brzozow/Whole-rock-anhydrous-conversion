#####################################################################################################
# Libraries
#####################################################################################################

import streamlit as st
import pandas as pd
import numpy as np

#####################################################################################################
# Title
#####################################################################################################

st.set_page_config(page_title = "Whole-rock anhdyrous conversion", layout="wide")
st.title("Whole-rock anhdyrous conversion")
st.write("Contact Information: Matthew Brzozowski, PhD | matt.brzozow@gmail.com")

st.write("-------------")
st.write("")

#####################################################################################################
# Important - read first
#####################################################################################################

st.subheader("Important - read first")

with st.expander("Important - read first"):
    st.write("")
    st.write("Remove any headings from your raw CSV file. The first row should be your elements and your data should start on the second row.")
    st.write("The script takes all < and > symbols and replaces the cell with a 0. If you want to treat the data differently, do these modifications before uploading the CSV for anhydrous conversion.")
    st.write("Make sure your sample column is labeled 'Sample' (case sensitive).")
    st.write("The script was created based on a certain set of elements. If your worksheet does not have some of the elements, add a blank column for those elements, otherwise there will be errors in the script.")
    st.write("-------------")
    st.write("MAJOR AND MINOR ELEMENTS")
    st.write("SiO2,	Al2O3,	Fe2O3,	CaO,	MgO,	Na2O,	K2O,	Cr2O3,	TiO2,	MnO,	P2O5,	SrO,	BaO,	LOI,	Total")
    st.write("-------------")
    st.write("TRACE ELEMENTS")
    st.write("C,	S,	Ba,	Ce,	Cr,	Cs,	Dy,	Er, Eu,	Ga,	Gd,	Ge,	Hf,	Ho,	La,	Lu,	Nb,	Nd,	Pr,	Rb,	Sm,	Sn,	Sr,	Ta,	Tb,	Th,	Tm,	U,	V,	W,	Y,	Yb,	Zr,	As,	Bi,	Hg,	In,	Re,	Sb,	Se,	Te, Tl,	Ag,	Cd,	Co,	Cu,	Li,	Mo,	Ni,	Pb,	Sc,	Zn")

st.write("-------------")
st.write("")

#####################################################################################################
# Load user data
#####################################################################################################

st.subheader("Upload your data as a CSV")

uploaded_file = st.file_uploader(label = "", type = "csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

#####################################################################################################
# Data clean-up
#####################################################################################################
if uploaded_file is not None:

    data["SiO2"] = pd.to_numeric(data["SiO2"], errors='coerce')
    data["TiO2"] = pd.to_numeric(data["TiO2"], errors='coerce')
    data["Al2O3"] = pd.to_numeric(data["Al2O3"], errors='coerce')
    data["Fe2O3"] = pd.to_numeric(data["Fe2O3"], errors='coerce')
    data["MnO"] = pd.to_numeric(data["MnO"], errors='coerce')
    data["MgO"] = pd.to_numeric(data["MgO"], errors='coerce')
    data["CaO"] = pd.to_numeric(data["CaO"], errors='coerce')
    data["Na2O"] = pd.to_numeric(data["Na2O"], errors='coerce')
    data["K2O"] = pd.to_numeric(data["K2O"], errors='coerce')
    data["Cr2O3"] = pd.to_numeric(data["Cr2O3"], errors='coerce')
    data["P2O5"] = pd.to_numeric(data["P2O5"], errors='coerce')
    data["SrO"] = pd.to_numeric(data["SrO"], errors='coerce')
    data["BaO"] = pd.to_numeric(data["BaO"], errors='coerce')
    data["Total"] = pd.to_numeric(data["Total"], errors='coerce')
    data["C"] = pd.to_numeric(data["C"], errors='coerce')
    data["S"] = pd.to_numeric(data["S"], errors='coerce')
    data["Ba"] = pd.to_numeric(data["Ba"], errors='coerce')
    data["Ce"] = pd.to_numeric(data["Ce"], errors='coerce')
    data["Cr"] = pd.to_numeric(data["Cr"], errors='coerce')
    data["Cs"] = pd.to_numeric(data["Cs"], errors='coerce')
    data["Dy"] = pd.to_numeric(data["Dy"], errors='coerce')
    data["Er"] = pd.to_numeric(data["Er"], errors='coerce')
    data["Eu"] = pd.to_numeric(data["Eu"], errors='coerce')
    data["Ga"] = pd.to_numeric(data["Ga"], errors='coerce')
    data["Gd"] = pd.to_numeric(data["Gd"], errors='coerce')
    data["Ge"] = pd.to_numeric(data["Ge"], errors='coerce')
    data["Hf"] = pd.to_numeric(data["Hf"], errors='coerce')
    data["Ho"] = pd.to_numeric(data["Ho"], errors='coerce')
    data["La"] = pd.to_numeric(data["La"], errors='coerce')
    data["Lu"] = pd.to_numeric(data["Lu"], errors='coerce')
    data["Nb"] = pd.to_numeric(data["Nb"], errors='coerce')
    data["Nd"] = pd.to_numeric(data["Nd"], errors='coerce')
    data["Pr"] = pd.to_numeric(data["Pr"], errors='coerce')
    data["Rb"] = pd.to_numeric(data["Rb"], errors='coerce')
    data["Sm"] = pd.to_numeric(data["Sm"], errors='coerce')
    data["Sn"] = pd.to_numeric(data["Sn"], errors='coerce')
    data["Sr"] = pd.to_numeric(data["Sr"], errors='coerce')
    data["Ta"] = pd.to_numeric(data["Ta"], errors='coerce')
    data["Tb"] = pd.to_numeric(data["Tb"], errors='coerce')
    data["Th"] = pd.to_numeric(data["Th"], errors='coerce')
    data["Tm"] = pd.to_numeric(data["Tm"], errors='coerce')
    data["U"] = pd.to_numeric(data["U"], errors='coerce')
    data["V"] = pd.to_numeric(data["V"], errors='coerce')
    data["W"] = pd.to_numeric(data["W"], errors='coerce')
    data["Y"] = pd.to_numeric(data["Y"], errors='coerce')
    data["Yb"] = pd.to_numeric(data["Yb"], errors='coerce')
    data["Zr"] = pd.to_numeric(data["Zr"], errors='coerce')
    data["As"] = pd.to_numeric(data["As"], errors='coerce')
    data["Bi"] = pd.to_numeric(data["Bi"], errors='coerce')
    data["Hg"] = pd.to_numeric(data["Hg"], errors='coerce')
    data["In"] = pd.to_numeric(data["In"], errors='coerce')
    data["Re"] = pd.to_numeric(data["Re"], errors='coerce')
    data["Sb"] = pd.to_numeric(data["Sb"], errors='coerce')
    data["Se"] = pd.to_numeric(data["Se"], errors='coerce')
    data["Te"] = pd.to_numeric(data["Te"], errors='coerce')
    data["Tl"] = pd.to_numeric(data["Tl"], errors='coerce')
    data["Ag"] = pd.to_numeric(data["Ag"], errors='coerce')
    data["Cd"] = pd.to_numeric(data["Cd"], errors='coerce')
    data["Co"] = pd.to_numeric(data["Co"], errors='coerce')
    data["Cu"] = pd.to_numeric(data["Cu"], errors='coerce')
    data["Li"] = pd.to_numeric(data["Li"], errors='coerce')
    data["Mo"] = pd.to_numeric(data["Mo"], errors='coerce')
    data["Ni"] = pd.to_numeric(data["Ni"], errors='coerce')
    data["Pb"] = pd.to_numeric(data["Pb"], errors='coerce')
    data["Sc"] = pd.to_numeric(data["Sc"], errors='coerce')
    data["Zn"] = pd.to_numeric(data["Zn"], errors='coerce')

    data["SiO2"] = data["SiO2"].fillna(0)
    data["TiO2"] = data["TiO2"].fillna(0)
    data["Al2O3"] = data["Al2O3"].fillna(0)
    data["Fe2O3"] = data["Fe2O3"].fillna(0)
    data["MnO"] = data["MnO"].fillna(0)
    data["MgO"] = data["MgO"].fillna(0)
    data["CaO"] = data["CaO"].fillna(0)
    data["Na2O"] = data["Na2O"].fillna(0)
    data["K2O"] = data["K2O"].fillna(0)
    data["Cr2O3"] = data["Cr2O3"].fillna(0)
    data["P2O5"] = data["P2O5"].fillna(0)
    data["SrO"] = data["SrO"].fillna(0)
    data["BaO"] = data["BaO"].fillna(0)
    data["Total"] = data["Total"].fillna(0)
    data["C"] = data["C"].fillna(0)
    data["S"] = data["S"].fillna(0)
    data["Ba"] = data["Ba"].fillna(0)
    data["Ce"] = data["Ce"].fillna(0)
    data["Cr"] = data["Cr"].fillna(0)
    data["Cs"] = data["Cs"].fillna(0)
    data["Dy"] = data["Dy"].fillna(0)
    data["Er"] = data["Er"].fillna(0)
    data["Eu"] = data["Eu"].fillna(0)
    data["Ga"] = data["Ga"].fillna(0)
    data["Gd"] = data["Gd"].fillna(0)
    data["Ge"] = data["Ge"].fillna(0)
    data["Hf"] = data["Hf"].fillna(0)
    data["Ho"] = data["Ho"].fillna(0)
    data["La"] = data["La"].fillna(0)
    data["Lu"] = data["Lu"].fillna(0)
    data["Nb"] = data["Nb"].fillna(0)
    data["Nd"] = data["Nd"].fillna(0)
    data["Pr"] = data["Pr"].fillna(0)
    data["Rb"] = data["Rb"].fillna(0)
    data["Sm"] = data["Sm"].fillna(0)
    data["Sn"] = data["Sn"].fillna(0)
    data["Sr"] = data["Sr"].fillna(0)
    data["Ta"] = data["Ta"].fillna(0)
    data["Tb"] = data["Tb"].fillna(0)
    data["Th"] = data["Th"].fillna(0)
    data["Tm"] = data["Tm"].fillna(0)
    data["U"] = data["U"].fillna(0)
    data["V"] = data["V"].fillna(0)
    data["W"] = data["W"].fillna(0)
    data["Y"] = data["Y"].fillna(0)
    data["Yb"] = data["Yb"].fillna(0)
    data["Zr"] = data["Zr"].fillna(0)
    data["As"] = data["As"].fillna(0)
    data["Bi"] = data["Bi"].fillna(0)
    data["Hg"] = data["Hg"].fillna(0)
    data["In"] = data["In"].fillna(0)
    data["Re"] = data["Re"].fillna(0)
    data["Sb"] = data["Sb"].fillna(0)
    data["Se"] = data["Se"].fillna(0)
    data["Te"] = data["Te"].fillna(0)
    data["Tl"] = data["Tl"].fillna(0)
    data["Ag"] = data["Ag"].fillna(0)
    data["Cd"] = data["Cd"].fillna(0)
    data["Co"] = data["Co"].fillna(0)
    data["Cu"] = data["Cu"].fillna(0)
    data["Li"] = data["Li"].fillna(0)
    data["Mo"] = data["Mo"].fillna(0)
    data["Ni"] = data["Ni"].fillna(0)
    data["Pb"] = data["Pb"].fillna(0)
    data["Sc"] = data["Sc"].fillna(0)
    data["Zn"] = data["Zn"].fillna(0)

#####################################################################################################
# Anhydrous calculation
#####################################################################################################

if uploaded_file is not None:

    LOI_Factor = data.Total/(data.Total - data.LOI)

    SiO2_anh = data.SiO2 * (100.0 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    TiO2_anh = data.TiO2 * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    Al2O3_anh = data.Al2O3 * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    Fe2O3_anh = data.Fe2O3 * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    MnO_anh = data.MnO * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    MgO_anh = data.MgO * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    CaO_anh = data.CaO * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    Na2O_anh = data.Na2O * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    K2O_anh = data.K2O * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    Cr2O3_anh = data.Cr2O3 * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    P2O5_anh = data.P2O5 * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    SrO_anh = data.SrO * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))
    BaO_anh = data.BaO * (100 / (data.SiO2 + data.TiO2 + data.Al2O3 + data.Fe2O3 + data.MnO + data.MgO + data.CaO + data.Na2O + data.K2O + data.Cr2O3 + data.P2O5 + data.SrO + data.BaO))

    Mg_No = ((0.063 * MgO_anh) / 24.31) / ((((0.9 * Fe2O3_anh) * 0.6994) / 55.85) + ((0.063 * MgO_anh) / 24.31))

    Cr_anh = data.Cr * LOI_Factor
    Co_anh = data.Co * LOI_Factor
    Ni_anh = data.Ni * LOI_Factor
    Rb_anh = data.Rb * LOI_Factor
    Sr_anh = data.Sr * LOI_Factor
    Cs_anh = data.Cs * LOI_Factor
    Ba_anh = data.Ba * LOI_Factor
    Sc_anh = data.Sc * LOI_Factor
    V_anh = data.V * LOI_Factor
    Ta_anh = data.Ta * LOI_Factor
    Nb_anh = data.Nb * LOI_Factor
    Zr_anh = data.Zr * LOI_Factor
    Hf_anh = data.Hf * LOI_Factor
    Th_anh = data.Th * LOI_Factor
    U_anh = data.U * LOI_Factor
    Y_anh = data.Y * LOI_Factor
    La_anh = data.La * LOI_Factor
    Ce_anh = data.Ce * LOI_Factor
    Pr_anh = data.Pr * LOI_Factor
    Nd_anh = data.Nd * LOI_Factor
    Sm_anh = data.Sm * LOI_Factor
    Eu_anh = data.Eu * LOI_Factor
    Gd_anh = data.Gd * LOI_Factor
    Tb_anh = data.Tb * LOI_Factor
    Dy_anh = data.Dy * LOI_Factor
    Ho_anh = data.Ho * LOI_Factor
    Er_anh = data.Er * LOI_Factor
    Tm_anh = data.Tm * LOI_Factor
    Yb_anh = data.Yb * LOI_Factor
    Lu_anh = data.Lu * LOI_Factor
    Cu_anh = data.Cu * LOI_Factor
    Zn_anh = data.Zn * LOI_Factor
    Mo_anh = data.Mo * LOI_Factor
    Ag_anh = data.Ag * LOI_Factor
    Tl_anh = data.Tl * LOI_Factor
    Pb_anh = data.Pb * LOI_Factor
    Sn_anh = data.Sn * LOI_Factor
    Sb_anh = data.Sb * LOI_Factor
    Ga_anh = data.Ga * LOI_Factor
    Ge_anh = data.Ge * LOI_Factor
    As_anh = data.As * LOI_Factor
    W_anh = data.W * LOI_Factor
    Bi_anh = data.Bi * LOI_Factor
    Hg_anh = data.Hg* LOI_Factor
    In_anh = data.In * LOI_Factor
    Re_anh = data.Re * LOI_Factor
    Se_anh = data.Se * LOI_Factor
    Te_anh = data.Te * LOI_Factor
    Cd_anh = data.Cd * LOI_Factor
    Li_anh = data.Li * LOI_Factor

    ## Primitive Mantle (McDonough and Sun, 1995)

    Cr_anh_PM = Cr_anh/2625
    Co_anh_PM = Co_anh/105
    Ni_anh_PM = Ni_anh/1960
    Rb_anh_PM = Rb_anh/0.6
    Sr_anh_PM = Sr_anh/19.9
    Cs_anh_PM = Cs_anh/0.021
    Ba_anh_PM = Ba_anh/6.6
    Sc_anh_PM = Sc_anh/16.2
    V_anh_PM = V_anh/82
    Ta_anh_PM = Ta_anh/0.037
    Nb_anh_PM = Nb_anh/0.658
    Zr_anh_PM = Zr_anh/10.5
    Hf_anh_PM = Hf_anh/0.283
    Th_anh_PM = Th_anh/0.0795
    U_anh_PM = U_anh/0.0203
    Y_anh_PM = Y_anh/4.3
    La_anh_PM = La_anh/0.648
    Ce_anh_PM = Ce_anh/1.675
    Pr_anh_PM = Pr_anh/0.254
    Nd_anh_PM = Nd_anh/1.25
    Sm_anh_PM = Sm_anh/0.406
    Eu_anh_PM = Eu_anh/0.154
    Gd_anh_PM = Gd_anh/0.544
    Tb_anh_PM = Tb_anh/0.099
    Dy_anh_PM = Dy_anh/0.674
    Ho_anh_PM = Ho_anh/0.149
    Er_anh_PM = Er_anh/0.438
    Tm_anh_PM = Tm_anh/0.068
    Yb_anh_PM = Yb_anh/0.441
    Lu_anh_PM = Lu_anh/0.0675
    Cu_anh_PM = Cu_anh/30
    Zn_anh_PM = Zn_anh/55
    Mo_anh_PM = Mo_anh/0.05
    Ag_anh_PM = Ag_anh/0.008
    Tl_anh_PM = Tl_anh/0.0035
    Pb_anh_PM = Pb_anh/0.15
    Sn_anh_PM = Sn_anh/0.13
    Sb_anh_PM = Sb_anh/0.0055
    Ga_anh_PM = Ga_anh/4
    Ge_anh_PM = Ge_anh/1.1
    As_anh_PM = As_anh/0.05
    W_anh_PM = W_anh/0.029
    Bi_anh_PM = Bi_anh/0.0025
    Hg_anh_PM = Hg_anh/0.01
    In_anh_PM = In_anh/0.011
    Re_anh_PM = Re_anh/0.00028
    Se_anh_PM = Se_anh/0.075
    Te_anh_PM = Te_anh/0.012
    Cd_anh_PM = Cd_anh/0.04
    Li_anh_PM = Li_anh/1.6

    ## Chondrite (McDonough and Sun, 1995)

    Cr_anh_CN = Cr_anh/2650
    Co_anh_CN = Co_anh/500
    Ni_anh_CN = Ni_anh/10500
    Rb_anh_CN = Rb_anh/2.3
    Sr_anh_CN = Sr_anh/7.25
    Cs_anh_CN = Cs_anh/0.19
    Ba_anh_CN = Ba_anh/2.41
    Sc_anh_CN = Sc_anh/5.92
    V_anh_CN = V_anh/56
    Ta_anh_CN = Ta_anh/0.0136
    Nb_anh_CN = Nb_anh/0.24
    Zr_anh_CN = Zr_anh/3.82
    Hf_anh_CN = Hf_anh/0.103
    Th_anh_CN = Th_anh/0.029
    U_anh_CN = U_anh/0.0074
    Y_anh_CN = Y_anh/1.57
    La_anh_CN = La_anh/0.237
    Ce_anh_CN = Ce_anh/0.613
    Pr_anh_CN = Pr_anh/0.0928
    Nd_anh_CN = Nd_anh/0.457
    Sm_anh_CN = Sm_anh/0.148
    Eu_anh_CN = Eu_anh/0.0563
    Gd_anh_CN = Gd_anh/0.199
    Tb_anh_CN = Tb_anh/0.0361
    Dy_anh_CN = Dy_anh/0.246
    Ho_anh_CN = Ho_anh/0.0546
    Er_anh_CN = Er_anh/0.16
    Tm_anh_CN = Tm_anh/0.0247
    Yb_anh_CN = Yb_anh/0.161
    Lu_anh_CN = Lu_anh/0.0246
    Cu_anh_CN = Cu_anh/120
    Zn_anh_CN = Zn_anh/310
    Mo_anh_CN = Mo_anh/500
    Ag_anh_CN = Ag_anh/0.2
    Tl_anh_CN = Tl_anh/0.14
    Pb_anh_CN = Pb_anh/2.47
    Sn_anh_CN = Sn_anh/1.65
    Sb_anh_CN = Sb_anh/0.14
    Ga_anh_CN = Ga_anh/9.2
    Ge_anh_CN = Ge_anh/31
    As_anh_CN = As_anh/1.85
    W_anh_CN = W_anh/0.093
    Bi_anh_CN = Bi_anh/0.11
    Hg_anh_CN = Hg_anh/0.3
    In_anh_CN = In_anh/0.08
    Re_anh_CN = Re_anh/0.04
    Se_anh_CN = Se_anh/21
    Te_anh_CN = Te_anh/2.33
    Cd_anh_CN = Cd_anh/0.71
    Li_anh_CN = Li_anh/1.5

    ## MORB (Sun and McDonough, 1989)

    Rb_anh_MORB = Rb_anh/0.56
    Sr_anh_MORB = Sr_anh/90
    Cs_anh_MORB = Cs_anh/0.007
    Ba_anh_MORB = Ba_anh/6.3
    Ta_anh_MORB = Ta_anh/0.132
    Nb_anh_MORB = Nb_anh/2.33
    Zr_anh_MORB = Zr_anh/74
    Hf_anh_MORB = Hf_anh/2.05
    Th_anh_MORB = Th_anh/0.12
    U_anh_MORB = U_anh/0.047
    Y_anh_MORB = Y_anh/28
    La_anh_MORB = La_anh/2.5
    Ce_anh_MORB = Ce_anh/7.5
    Pr_anh_MORB = Pr_anh/1.32
    Nd_anh_MORB = Nd_anh/7.3
    Sm_anh_MORB = Sm_anh/2.63
    Eu_anh_MORB = Eu_anh/1.02
    Gd_anh_MORB = Gd_anh/3.68
    Tb_anh_MORB = Tb_anh/0.67
    Dy_anh_MORB = Dy_anh/4.55
    Ho_anh_MORB = Ho_anh/1.01
    Er_anh_MORB = Er_anh/2.97
    Tm_anh_MORB = Tm_anh/0.456
    Yb_anh_MORB = Yb_anh/3.05
    Lu_anh_MORB = Lu_anh/0.455
    Mo_anh_MORB = Mo_anh/0.31
    Tl_anh_MORB = Tl_anh/0.0014
    Pb_anh_MORB = Pb_anh/0.3
    Sn_anh_MORB = Sn_anh/1.1
    Sb_anh_MORB = Sb_anh/0.01
    W_anh_MORB = W_anh/0.01
    Li_anh_MORB = Li_anh/4.3

#####################################################################################################
# Combine data into a dataframe
#####################################################################################################

if uploaded_file is not None:

    anhydrous_data = pd.DataFrame()

    anhydrous_data["Sample"] = data.Sample
    anhydrous_data["SiO2"] = SiO2_anh
    anhydrous_data["TiO2"] = TiO2_anh
    anhydrous_data["Al2O3"] = Al2O3_anh
    anhydrous_data["Fe2O3"] = Fe2O3_anh
    anhydrous_data["MnO"] = MnO_anh
    anhydrous_data["MgO"] = MgO_anh
    anhydrous_data["CaO"] = CaO_anh
    anhydrous_data["Na2O"] = Na2O_anh
    anhydrous_data["K2O"] = K2O_anh
    anhydrous_data["Cr2O3"] = Cr2O3_anh
    anhydrous_data["P2O5"] = P2O5_anh
    anhydrous_data["SrO"] = SrO_anh
    anhydrous_data["BaO"] = BaO_anh
    anhydrous_data["Mg_No"] = Mg_No
    anhydrous_data["LOI Factor"] = LOI_Factor
    anhydrous_data["Cr"] = Cr_anh
    anhydrous_data["Co"] = Co_anh
    anhydrous_data["Ni"] = Ni_anh
    anhydrous_data["Rb"] = Rb_anh
    anhydrous_data["Sr"] = Sr_anh
    anhydrous_data["Cs"] = Cs_anh
    anhydrous_data["Ba"] = Ba_anh
    anhydrous_data["Sc"] = Sc_anh
    anhydrous_data["V"] = V_anh
    anhydrous_data["Ta"] = Ta_anh
    anhydrous_data["Nb"] = Nb_anh
    anhydrous_data["Zr"] = Zr_anh
    anhydrous_data["Hf"] = Hf_anh
    anhydrous_data["Th"] = Th_anh
    anhydrous_data["U"] = U_anh
    anhydrous_data["Y"] = Y_anh
    anhydrous_data["La"] = La_anh
    anhydrous_data["Ce"] = Ce_anh
    anhydrous_data["Pr"] = Pr_anh
    anhydrous_data["Nd"] = Nd_anh
    anhydrous_data["Sm"] = Sm_anh
    anhydrous_data["Eu"] = Eu_anh
    anhydrous_data["Gd"] = Gd_anh
    anhydrous_data["Tb"] = Tb_anh
    anhydrous_data["Dy"] = Dy_anh
    anhydrous_data["Ho"] = Ho_anh
    anhydrous_data["Er"] = Er_anh
    anhydrous_data["Tm"] = Tm_anh
    anhydrous_data["Yb"] = Yb_anh
    anhydrous_data["Lu"] = Lu_anh
    anhydrous_data["Cu"] = Cu_anh
    anhydrous_data["Zn"] = Zn_anh
    anhydrous_data["Mo"] = Mo_anh
    anhydrous_data["Ag"] = Ag_anh
    anhydrous_data["Tl"] = Tl_anh
    anhydrous_data["Pb"] = Pb_anh
    anhydrous_data["Sn"] = Sn_anh
    anhydrous_data["Sb"] = Sb_anh
    anhydrous_data["Ga"] = Ga_anh
    anhydrous_data["Ge"] = Ge_anh
    anhydrous_data["As"] = As_anh
    anhydrous_data["W"] = W_anh
    anhydrous_data["Bi"] = Bi_anh
    anhydrous_data["Hg"] = Hg_anh
    anhydrous_data["In"] = In_anh
    anhydrous_data["Re"] = Re_anh
    anhydrous_data["Se"] = Se_anh
    anhydrous_data["TeCo"] = Te_anh
    anhydrous_data["Cd"] = Cd_anh
    anhydrous_data["Li"] = Li_anh

    ## Primitive Mantle (McDonough and Sun, 1995)

    anhydrous_data["Cr_PM"] = Cr_anh_PM
    anhydrous_data["Co_PM"] = Co_anh_PM
    anhydrous_data["Ni_PM"] = Ni_anh_PM
    anhydrous_data["Rb_PM"] = Rb_anh_PM
    anhydrous_data["Sr_PM"] = Sr_anh_PM
    anhydrous_data["Cs_PM"] = Cs_anh_PM
    anhydrous_data["Ba_PM"] = Ba_anh_PM
    anhydrous_data["Sc_PM"] = Sc_anh_PM
    anhydrous_data["V_PM"] = V_anh_PM
    anhydrous_data["Ta_PM"] = Ta_anh_PM
    anhydrous_data["Nb_PM"] = Nb_anh_PM
    anhydrous_data["Zr_PM"] = Zr_anh_PM
    anhydrous_data["Hf_PM"] = Hf_anh_PM
    anhydrous_data["Th_PM"] = Th_anh_PM
    anhydrous_data["U_PM"] = U_anh_PM
    anhydrous_data["Y_PM"] = Y_anh_PM
    anhydrous_data["La_PM"] = La_anh_PM
    anhydrous_data["Ce_PM"] = Ce_anh_PM
    anhydrous_data["Pr_PM"] = Pr_anh_PM
    anhydrous_data["Nd_PM"] = Nd_anh_PM
    anhydrous_data["Sm_PM"] = Sm_anh_PM
    anhydrous_data["Eu_PM"] = Eu_anh_PM
    anhydrous_data["Gd_PM"] = Gd_anh_PM
    anhydrous_data["Tb_PM"] = Tb_anh_PM
    anhydrous_data["Dy_PM"] = Dy_anh_PM
    anhydrous_data["Ho_PM"] = Ho_anh_PM
    anhydrous_data["Er_PM"] = Er_anh_PM
    anhydrous_data["Tm_PM"] = Tm_anh_PM
    anhydrous_data["Yb_PM"] = Yb_anh_PM
    anhydrous_data["Lu_PM"] = Lu_anh_PM
    anhydrous_data["Cu_PM"] = Cu_anh_PM
    anhydrous_data["Zn_PM"] = Zn_anh_PM
    anhydrous_data["Mo_PM"] = Mo_anh_PM
    anhydrous_data["Ag_PM"] = Ag_anh_PM
    anhydrous_data["Tl_PM"] = Tl_anh_PM
    anhydrous_data["Pb_PM"] = Pb_anh_PM
    anhydrous_data["Sn_PM"] = Sn_anh_PM
    anhydrous_data["Sb_PM"] = Sb_anh_PM
    anhydrous_data["Ga_PM"] = Ga_anh_PM
    anhydrous_data["Ge_PM"] = Ge_anh_PM
    anhydrous_data["As_PM"] = As_anh_PM
    anhydrous_data["W_PM"] = W_anh_PM
    anhydrous_data["Bi_PM"] = Bi_anh_PM
    anhydrous_data["Hg_PM"] = Hg_anh_PM
    anhydrous_data["In_PM"] = In_anh_PM
    anhydrous_data["Re_PM"] = Re_anh_PM
    anhydrous_data["Se_PM"] = Se_anh_PM
    anhydrous_data["Te_PM"] = Te_anh_PM
    anhydrous_data["Cd_PM"] = Cd_anh_PM
    anhydrous_data["Li_PM"] = Li_anh_PM

    ## Chondrite (McDonough and Sun, 1995)

    anhydrous_data["Cr_CN"] = Cr_anh_CN
    anhydrous_data["Co_CN"] = Co_anh_CN
    anhydrous_data["Ni_CN"] = Ni_anh_CN
    anhydrous_data["Rb_CN"] = Rb_anh_CN
    anhydrous_data["Sr_CN"] = Sr_anh_CN
    anhydrous_data["Cs_CN"] = Cs_anh_CN
    anhydrous_data["Ba_CN"] = Ba_anh_CN
    anhydrous_data["Sc_CN"] = Sc_anh_CN
    anhydrous_data["V_CN"] = V_anh_CN
    anhydrous_data["Ta_CN"] = Ta_anh_CN
    anhydrous_data["Nb_CN"] = Nb_anh_CN
    anhydrous_data["Zr_CN"] = Zr_anh_CN
    anhydrous_data["Hf_CN"] = Hf_anh_CN
    anhydrous_data["Th_CN"] = Th_anh_CN
    anhydrous_data["U_CN"] = U_anh_CN
    anhydrous_data["Y_CN"] = Y_anh_CN
    anhydrous_data["La_CN"] = La_anh_CN
    anhydrous_data["Ce_CN"] = Ce_anh_CN
    anhydrous_data["Pr_CN"] = Pr_anh_CN
    anhydrous_data["Nd_CN"] = Nd_anh_CN
    anhydrous_data["Sm_CN"] = Sm_anh_CN
    anhydrous_data["Eu_CN"] = Eu_anh_CN
    anhydrous_data["Gd_CN"] = Gd_anh_CN
    anhydrous_data["Tb_CN"] = Tb_anh_CN
    anhydrous_data["Dy_CN"] = Dy_anh_CN
    anhydrous_data["Ho_CN"] = Ho_anh_CN
    anhydrous_data["Er_CN"] = Er_anh_CN
    anhydrous_data["Tm_CN"] = Tm_anh_CN
    anhydrous_data["Yb_CN"] = Yb_anh_CN
    anhydrous_data["Lu_CN"] = Lu_anh_CN
    anhydrous_data["Cu_CN"] = Cu_anh_CN
    anhydrous_data["Zn_CN"] = Zn_anh_CN
    anhydrous_data["Mo_CN"] = Mo_anh_CN
    anhydrous_data["Ag_CN"] = Ag_anh_CN
    anhydrous_data["Tl_CN"] = Tl_anh_CN
    anhydrous_data["Pb_CN"] = Pb_anh_CN
    anhydrous_data["Sn_CN"] = Sn_anh_CN
    anhydrous_data["Sb_CN"] = Sb_anh_CN
    anhydrous_data["Ga_CN"] = Ga_anh_CN
    anhydrous_data["Ge_CN"] = Ge_anh_CN
    anhydrous_data["As_CN"] = As_anh_CN
    anhydrous_data["W_CN"] = W_anh_CN
    anhydrous_data["Bi_CN"] = Bi_anh_CN
    anhydrous_data["Hg_CN"] = Hg_anh_CN
    anhydrous_data["In_CN"] = In_anh_CN
    anhydrous_data["Re_CN"] = Re_anh_CN
    anhydrous_data["Se_CN"] = Se_anh_CN
    anhydrous_data["Te_CN"] = Te_anh_CN
    anhydrous_data["Cd_CN"] = Cd_anh_CN
    anhydrous_data["Li_CN"] = Li_anh_CN

    ## MORB (Sun and McDonough, 1989)

    anhydrous_data["Rb_MORB"] = Rb_anh_MORB
    anhydrous_data["Sr_MORB"] = Sr_anh_MORB
    anhydrous_data["Cs_MORB"] = Cs_anh_MORB
    anhydrous_data["Ba_MORB"] = Ba_anh_MORB
    anhydrous_data["Ta_MORB"] = Ta_anh_MORB
    anhydrous_data["Nb_MORB"] = Nb_anh_MORB
    anhydrous_data["Zr_MORB"] = Zr_anh_MORB
    anhydrous_data["Hf_MORB"] = Hf_anh_MORB
    anhydrous_data["Th_MORB"] = Th_anh_MORB
    anhydrous_data["U_MORB"] = U_anh_MORB
    anhydrous_data["Y_MORB"] = Y_anh_MORB
    anhydrous_data["La_MORB"] = La_anh_MORB
    anhydrous_data["Ce_MORB"] = Ce_anh_MORB
    anhydrous_data["Pr_MORB"] = Pr_anh_MORB
    anhydrous_data["Nd_MORB"] = Nd_anh_MORB
    anhydrous_data["Sm_MORB"] = Sm_anh_MORB
    anhydrous_data["Eu_MORB"] = Eu_anh_MORB
    anhydrous_data["Gd_MORB"] = Gd_anh_MORB
    anhydrous_data["Tb_MORB"] = Tb_anh_MORB
    anhydrous_data["Dy_MORB"] = Dy_anh_MORB
    anhydrous_data["Ho_MORB"] = Ho_anh_MORB
    anhydrous_data["Er_MORB"] = Er_anh_MORB
    anhydrous_data["Tm_MORB"] = Tm_anh_MORB
    anhydrous_data["Yb_MORB"] = Yb_anh_MORB
    anhydrous_data["Lu_MORB"] = Lu_anh_MORB
    anhydrous_data["Mo_MORB"] = Mo_anh_MORB
    anhydrous_data["Tl_MORB"] = Tl_anh_MORB
    anhydrous_data["Pb_MORB"] = Pb_anh_MORB
    anhydrous_data["Sn_MORB"] = Sn_anh_MORB
    anhydrous_data["Sb_MORB"] = Sb_anh_MORB
    anhydrous_data["W_MORB"] = W_anh_MORB
    anhydrous_data["Li_MORB"] = Li_anh_MORB

#####################################################################################################
# Download data
#####################################################################################################

if uploaded_file is not None:

    st.write("-------------")

    file_name = st.text_input(label = "Input file name (incude .csv)")

    @st.cache
    def convert_df(df):
        return df.to_csv(index = False).encode("utf-8")

    anhydrous_data_download = convert_df(anhydrous_data)
    st.download_button(label = "Download anhydrous data", data = anhydrous_data_download, file_name = file_name, mime = "text/csv")

    st.write("-------------")

    st.subheader("Raw data")
    st.dataframe(data)

    st.write("-------------")

    st.subheader("Anhydrous data")
    st.dataframe(anhydrous_data)