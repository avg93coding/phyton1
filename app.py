import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit App: Python for Health Data Mini-eBook

def main():
    st.set_page_config(page_title="Python for Health Data", layout="wide")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to", [
            "Introduction",
            "Why Python?",
            "Your First Steps",
            "Starter Commands",
            "Plot Your First Chart",
            "Interactive Charts",
            "Download eBook"
        ]
    )

    if page == "Introduction":
        show_introduction()
    elif page == "Why Python?":
        show_why_python()
    elif page == "Your First Steps":
        show_setup()
    elif page == "Starter Commands":
        show_starter_commands()
    elif page == "Plot Your First Chart":
        show_plot_chart()
    elif page == "Interactive Charts":
        show_interactive()
    elif page == "Download eBook":
        show_download()


def show_introduction():
    st.title("Python for Health Data: Beginners Welcome")
    st.write(
        "No coding background? No problem. This mini-guide will help you get started with Python for epidemiology "
        "and clinical data visualization."
    )
    st.markdown("---")


def show_why_python():
    st.header("1. Simple & Free")
    st.write("- Install in minutes via Anaconda")
    st.write("- Intuitive syntax that reads like English")
    st.write("- Completely open-source (no cost!)")
    st.markdown("---")


def show_setup():
    st.header("2. Set Up Your Environment")
    st.write("**Download Anaconda or Miniconda** to get Python and Jupyter in one bundle.")
    st.write("**Create a project folder** to keep your scripts and data organized.")
    st.write("**Launch Jupyter Notebook** by running `jupyter notebook` in your terminal or Anaconda Prompt.")
    st.markdown("---")


def show_starter_commands():
    st.header("3. Try These Starter Commands")
    code = '''import pandas as pd    # Load your data

df = pd.read_csv("data.csv")
df.head()              # Preview first rows
# Bonus: df.describe() for quick stats'''    
    st.code(code, language="python")
    st.markdown("---")


def show_plot_chart():
    st.header("4. Plot Your First Chart")
    code = '''import matplotlib.pyplot as plt

df["cases"].plot(linewidth=2)
plt.show()'''    
    st.code(code, language="python")
    st.write("Tip: Change \"cases\" to your metric (e.g., incidence, prevalence).")
    st.markdown("---")


def show_interactive():
    st.header("5. Interactive Charts in Seconds")
    code = '''import plotly.express as px

fig = px.line(df, x="date", y="cases")
fig.show()'''    
    st.code(code, language="python")
    st.write("Use `fig.show()` in a notebook or `st.plotly_chart(fig)` in Streamlit.")
    st.markdown("---")


def show_download():
    st.header("Download the Mini eBook")
    try:
        with open("health_data_python_guide.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📥 Download PDF Guide",
            data=PDFbyte,
            file_name="health_data_python_guide.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.error("PDF guide not found. Please upload `health_data_python_guide.pdf` in the app directory.")


if __name__ == "__main__":
    main()
