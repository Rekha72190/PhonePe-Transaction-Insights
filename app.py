# ============================================
# 📱 PHONEPE PULSE DASHBOARD — FINAL VERSION
# ============================================

import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="PhonePe Pulse Dashboard",
    layout="wide"
)

# ------------------------------------------------
# DATABASE CONNECTION (AUTO SAFE)
# ------------------------------------------------
try:
    engine = create_engine(
        "postgresql://postgres:qwerty123@localhost:5432/phonepe_db"
    )
    pd.read_sql("SELECT 1", engine)
    st.sidebar.success("✅ Database Connected")

except Exception as e:
    st.error("❌ Database Connection Failed")
    st.stop()

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------
st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "",
    ["🏠 Home", "📈 Business Case Study"]
)

# ------------------------------------------------
# INDIA GEOJSON
# ------------------------------------------------
GEOJSON = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

# =====================================================
# 🏠 HOME PAGE
# =====================================================
if page == "🏠 Home":

    st.image(
        "https://download.logo.wine/logo/PhonePe/PhonePe-Logo.wine.png",
        width=130
    )

    st.title("PhonePe Pulse — The Beat of Progress")

    # ---------------- Filters ----------------
    c1,c2,c3 = st.columns(3)

    year = c1.selectbox("Year",[2018,2019,2020,2021,2022,2023,2024])
    quarter = c2.selectbox("Quarter",[1,2,3,4])
    metric = c3.selectbox(
        "Metric",
        ["Transaction Amount","Transaction Count"]
    )

    # ---------------- Map Query ----------------
    query=f"""
    SELECT state,
    SUM(transaction_count) total_txn,
    SUM(transaction_amount) total_amt
    FROM aggregated_transaction
    WHERE year={year} AND quarter={quarter}
    GROUP BY state
    """

    df = pd.read_sql(query,engine)

    df["state"]=df["state"].str.replace("-"," ").str.title()

    value = "total_amt" if metric=="Transaction Amount" else "total_txn"

    fig = px.choropleth(
        df,
        geojson=GEOJSON,
        locations="state",
        featureidkey="properties.ST_NM",
        color=value,
        color_continuous_scale="Turbo"
    )

    fig.update_geos(fitbounds="locations",visible=False)
    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# EXPLORE DATA DROPDOWN
# =====================================================

    st.markdown("## 📊 Explore Data")

    explore = st.selectbox(
        "Choose Analysis",
        [
            "Top States",
            "Top District",
            "Top Pincode",
            "Reports",
            "Insights",
            "Data API"
        ]
    )

# ---------- TOP STATES ----------
    if explore=="Top States":

        df=pd.read_sql(f"""
        SELECT state,
        SUM(transaction_amount) amount
        FROM aggregated_transaction
        WHERE year={year} AND quarter={quarter}
        GROUP BY state
        ORDER BY amount DESC LIMIT 10
        """,engine)

        st.plotly_chart(
            px.bar(df,x="state",y="amount",
            title="🏆 Top States"),
            use_container_width=True
        )

# ---------- TOP DISTRICT ----------
    elif explore=="Top District":

        df=pd.read_sql(f"""
        SELECT district,
        SUM(transaction_amount) amount
        FROM map_transaction
        WHERE year={year} AND quarter={quarter}
        GROUP BY district
        ORDER BY amount DESC LIMIT 10
        """,engine)

        st.plotly_chart(
            px.bar(df,x="district",y="amount",
            title="🏙️ Top Districts"),
            use_container_width=True
        )

# ---------- AUTO SAFE PINCODE ----------
    elif explore=="Top Pincode":

        check = pd.read_sql(
            "SELECT * FROM top_transaction LIMIT 1",
            engine
        )

        col = check.columns[0]

        df=pd.read_sql(f"""
        SELECT {col},
        SUM(transaction_amount) amount
        FROM top_transaction
        WHERE year={year} AND quarter={quarter}
        GROUP BY {col}
        ORDER BY amount DESC LIMIT 10
        """,engine)

        st.plotly_chart(
            px.bar(df,x=col,y="amount",
            title="📍 Top Pincode"),
            use_container_width=True
        )

# ---------- REPORT ----------
    elif explore=="Reports":

        df=pd.read_sql("""
        SELECT year,
        SUM(transaction_amount) amount
        FROM aggregated_transaction
        GROUP BY year
        """,engine)

        st.plotly_chart(
            px.line(df,x="year",y="amount",
            markers=True,
            title="📈 Growth Report"),
            use_container_width=True
        )

# ---------- INSIGHTS ----------
    elif explore=="Insights":

        df=pd.read_sql("""
        SELECT state,
        SUM(transaction_amount) amount
        FROM aggregated_transaction
        GROUP BY state
        ORDER BY amount DESC LIMIT 1
        """,engine)

        st.metric("🔥 Top Performing State",df.iloc[0,0])
        st.metric("💰 Transaction Value",
                  f"₹ {df.iloc[0,1]/1e7:.2f} Cr")

# ---------- DATA API ----------
    elif explore=="Data API":

        df=pd.read_sql(
            "SELECT * FROM aggregated_transaction LIMIT 100",
            engine
        )
        st.dataframe(df)

# =====================================================
# 📈 BUSINESS CASE STUDY
# =====================================================
else:

    st.title("📈 Business Case Study")

    case = st.selectbox(
        "Select Case",
        [
            "Transaction Dynamics",
            "Device Dominance",
            "Insurance Growth",
            "Market Expansion",
            "User Engagement"
        ]
    )

    c1,c2=st.columns(2)
    year=c1.selectbox("Year",[2018,2019,2020,2021,2022,2023,2024])
    quarter=c2.selectbox("Quarter",[1,2,3,4])

# =====================================================
# CASE 1 — TRANSACTION DYNAMICS (5 ANALYSIS)
# =====================================================
    if case=="Transaction Dynamics":

        analysis=st.selectbox(
            "Analysis",
            ["Top States","Type Share","Year Growth","Quarter Trend","Count Spread"]
        )

        if analysis=="Top States":
            df=pd.read_sql("""
            SELECT state,SUM(transaction_amount) amount
            FROM aggregated_transaction GROUP BY state
            ORDER BY amount DESC LIMIT 10
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="amount"))

        elif analysis=="Type Share":
            df=pd.read_sql("""
            SELECT transaction_type,SUM(transaction_amount) amount
            FROM aggregated_transaction GROUP BY transaction_type
            """,engine)
            st.plotly_chart(px.pie(df,names="transaction_type",values="amount"))

        elif analysis=="Year Growth":
            df=pd.read_sql("""
            SELECT year,SUM(transaction_amount) amount
            FROM aggregated_transaction GROUP BY year
            """,engine)
            st.plotly_chart(px.line(df,x="year",y="amount"))

        elif analysis=="Quarter Trend":
            df=pd.read_sql("""
            SELECT quarter,SUM(transaction_amount) amount
            FROM aggregated_transaction GROUP BY quarter
            """,engine)
            st.plotly_chart(px.bar(df,x="quarter",y="amount"))

        else:
            df=pd.read_sql("""
            SELECT state,SUM(transaction_count) cnt
            FROM aggregated_transaction GROUP BY state
            """,engine)
            st.plotly_chart(px.scatter(df,x="state",y="cnt"))

# =====================================================
# CASE 2 DEVICE DOMINANCE (5 ANALYSIS)
# =====================================================
    elif case=="Device Dominance":

        analysis=st.selectbox(
            "Analysis",
            ["User Type","User Growth","State Users","App Opens","Engagement"]
        )

        if analysis=="User Type":
            df=pd.read_sql("""
            SELECT user_type,SUM(user_count) users
            FROM aggregated_user GROUP BY user_type
            """,engine)
            st.plotly_chart(px.bar(df,x="user_type",y="users"))

        elif analysis=="User Growth":
            df=pd.read_sql("""
            SELECT year,SUM(user_count) users
            FROM aggregated_user GROUP BY year
            """,engine)
            st.plotly_chart(px.line(df,x="year",y="users"))

        elif analysis=="State Users":
            df=pd.read_sql("""
            SELECT state,SUM(user_count) users
            FROM aggregated_user GROUP BY state
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="users"))

        elif analysis=="App Opens":
            df=pd.read_sql("""
            SELECT state,SUM(app_opens) opens
            FROM map_user GROUP BY state
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="opens"))

        else:
            df=pd.read_sql("""
            SELECT state,
            SUM(app_opens)/SUM(registered_users) ratio
            FROM map_user GROUP BY state
            """,engine)
            st.plotly_chart(px.scatter(df,x="state",y="ratio"))

# =====================================================
# CASE 3 INSURANCE (5 ANALYSIS)
# =====================================================
    elif case=="Insurance Growth":

        analysis=st.selectbox(
            "Analysis",
            ["State Premium","Year Growth","Quarter Trend","Policy Count","Average Premium"]
        )

        if analysis=="State Premium":
            df=pd.read_sql("""
            SELECT state,SUM(insurance_amount) amount
            FROM aggregated_insurance GROUP BY state
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="amount"))

        elif analysis=="Year Growth":
            df=pd.read_sql("""
            SELECT year,SUM(insurance_amount) amount
            FROM aggregated_insurance GROUP BY year
            """,engine)
            st.plotly_chart(px.line(df,x="year",y="amount"))

        elif analysis=="Quarter Trend":
            df=pd.read_sql("""
            SELECT quarter,SUM(insurance_amount) amount
            FROM aggregated_insurance GROUP BY quarter
            """,engine)
            st.plotly_chart(px.bar(df,x="quarter",y="amount"))

        elif analysis=="Policy Count":
            df=pd.read_sql("""
            SELECT state,SUM(insurance_count) cnt
            FROM aggregated_insurance GROUP BY state
            """,engine)
            st.plotly_chart(px.scatter(df,x="state",y="cnt"))

        else:
            df=pd.read_sql("""
            SELECT state,AVG(insurance_amount) avg_amt
            FROM aggregated_insurance GROUP BY state
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="avg_amt"))

# =====================================================
# CASE 4 MARKET EXPANSION (5 ANALYSIS)
# =====================================================
    elif case=="Market Expansion":

        analysis=st.selectbox(
            "Analysis",
            ["State Volume","District Amount","Year Trend","Quarter Trend","Average Value"]
        )

        if analysis=="State Volume":
            df=pd.read_sql("""
            SELECT state,SUM(transaction_count) cnt
            FROM map_transaction GROUP BY state
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="cnt"))

        elif analysis=="District Amount":
            df=pd.read_sql("""
            SELECT district,SUM(transaction_amount) amt
            FROM map_transaction GROUP BY district
            """,engine)
            st.plotly_chart(px.bar(df,x="district",y="amt"))

        elif analysis=="Year Trend":
            df=pd.read_sql("""
            SELECT year,SUM(transaction_amount) amt
            FROM map_transaction GROUP BY year
            """,engine)
            st.plotly_chart(px.line(df,x="year",y="amt"))

        elif analysis=="Quarter Trend":
            df=pd.read_sql("""
            SELECT quarter,SUM(transaction_count) cnt
            FROM map_transaction GROUP BY quarter
            """,engine)
            st.plotly_chart(px.bar(df,x="quarter",y="cnt"))

        else:
            df=pd.read_sql("""
            SELECT state,AVG(transaction_amount) avg_amt
            FROM map_transaction GROUP BY state
            """,engine)
            st.plotly_chart(px.scatter(df,x="state",y="avg_amt"))

# =====================================================
# CASE 5 USER ENGAGEMENT (5 ANALYSIS)
# =====================================================
    elif case=="User Engagement":

        analysis=st.selectbox(
            "Analysis",
            ["Registered Users","App Opens","Engagement Ratio","Year Opens","Quarter Opens"]
        )

        if analysis=="Registered Users":
            df=pd.read_sql("""
            SELECT state,SUM(registered_users) users
            FROM map_user GROUP BY state
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="users"))

        elif analysis=="App Opens":
            df=pd.read_sql("""
            SELECT state,SUM(app_opens) opens
            FROM map_user GROUP BY state
            """,engine)
            st.plotly_chart(px.bar(df,x="state",y="opens"))

        elif analysis=="Engagement Ratio":
            df=pd.read_sql("""
            SELECT state,
            SUM(app_opens)/SUM(registered_users) ratio
            FROM map_user GROUP BY state
            """,engine)
            st.plotly_chart(px.scatter(df,x="state",y="ratio"))

        elif analysis=="Year Opens":
            df=pd.read_sql("""
            SELECT year,SUM(app_opens) opens
            FROM map_user GROUP BY year
            """,engine)
            st.plotly_chart(px.line(df,x="year",y="opens"))

        else:
            df=pd.read_sql("""
            SELECT quarter,SUM(app_opens) opens
            FROM map_user GROUP BY quarter
            """,engine)
            st.plotly_chart(px.bar(df,x="quarter",y="opens"))