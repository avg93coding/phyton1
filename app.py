import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit App: Python for Health Data Mini-eBook (For Dummies Edition)

def main():
    st.set_page_config(page_title="Python for Health Data - Dummies Guide", layout="wide")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to", [
            "Introduction",
            "What is Python?",
            "Why Python?",
            "Your First Steps",
            "Starter Commands",
            "Understanding Data Types",
            "Customize and Save Plots",
            "Interactive Charts",
            "Download eBook"
        ]
    )

    if page == "Introduction":
        show_introduction()
    elif page == "What is Python?":
        show_what_is_python()
    elif page == "Why Python?":
        show_why_python()
    elif page == "Your First Steps":
        show_setup()
    elif page == "Starter Commands":
        show_starter_commands()
    elif page == "Understanding Data Types":
        show_data_types()
    elif page == "Customize and Save Plots":
        show_customize_plots()
    elif page == "Interactive Charts":
        show_interactive()
    elif page == "Download eBook":
        show_download()

# Section: Introduction

def show_introduction():
    st.title("Python for Health Data: Step-by-Step (Dummies Edition)")
    st.markdown(
        "Welcome to the most detailed, step-by-step guide for using Python in health and epidemiology data visualization! "
        "Each section breaks down tasks into clear steps you can follow instantly."
    )
    st.markdown("---")

# Section: What is Python?

def show_what_is_python():
    st.header("What is Python?")
    st.subheader("Step 1: Understand the Language")
    st.write("Python is a high-level, interpreted programming language used for data analysis, web apps, automation, and more.")
    
    st.subheader("Step 2: Key Characteristics")
    st.write(
        "- *Easy-to-read syntax* resembling pseudocode", 
        "- *Interpreted* (no compile step needed)", 
        "- *Cross-platform* (runs on Windows, Mac, Linux)", 
        "- *Extensive ecosystem* with thousands of libraries", sep="\n"
    )

    st.subheader("Step 3: Try Your First Command")
    st.write("Open your terminal or Anaconda Prompt and type:")
    st.code("python --version", language="bash")
    st.write("You should see a version number like `Python 3.x.x`.")
    st.markdown("---")

# Section: Why Python?

def show_why_python():
    st.header("Why Python for Health Data?")
    st.subheader("Step 1: Leverage Data Libraries")
    st.write("Python offers robust tools like Pandas, NumPy, and SciPy for data cleaning and analysis.")

    st.subheader("Step 2: Visualize with Ease")
    st.write("Use Matplotlib, Seaborn, and Plotly to create publication-quality static and interactive plots.")

    st.subheader("Step 3: Share & Reproduce")
    st.write("Write code in Jupyter Notebooks or apps in Streamlit to share workflows and results seamlessly.")
    st.markdown("---")

# Section: Your First Steps

def show_setup():
    st.header("Your First Steps: Setup Environment")
    st.subheader("Step 1: Install Anaconda")
    st.write("1. Go to Anaconda website: https://www.anaconda.com/products/distribution")
    st.write("2. Download the Python 3.x installer for your OS.")
    st.write("3. Run the installer and follow prompts.")

    st.subheader("Step 2: Create Virtual Environment")
    st.code(
        """
conda create -n health_data python=3.9 -y
conda activate health_data
pip install streamlit pandas matplotlib plotly
        """,
        language="bash"
    )

    st.subheader("Step 3: Verify Installation")
    st.write("In your terminal, type:`streamlit --version` to confirm Streamlit is installed.")
    st.write("Then, run:`python -c \"import pandas; print(pandas.__version__)\"` to check Pandas.")
    st.markdown("---")

# Section: Starter Commands

def show_starter_commands():
    st.header("Starter Commands: Load & Preview Data")
    st.subheader("Step 1: Import Pandas")
    st.code("import pandas as pd", language="python")

    st.subheader("Step 2: Read Your Dataset")
    st.code("df = pd.read_csv('data.csv')", language="python")

    st.subheader("Step 3: Preview Data")
    st.code("df.head()  # Displays first 5 rows", language="python")

    st.subheader("Step 4: Quick Statistics")
    st.code("df.describe()  # Summary of numeric columns", language="python")
    st.markdown("---")

# Section: Understanding Data Types

def show_data_types():
    st.header("Understanding Data Types")
    st.subheader("Step 1: Check Column Types")
    st.code("df.dtypes", language="python")

    st.subheader("Step 2: Convert to Datetime")
    st.code("df['date'] = pd.to_datetime(df['date'])", language="python")

    st.subheader("Step 3: Convert Strings to Numbers")
    st.code("df['value'] = df['value'].astype(float)", language="python")
    st.markdown("---")

# Section: Customize and Save Plots

def show_customize_plots():
    st.header("Customize and Save Plots")
    st.subheader("Step 1: Import Matplotlib")
    st.code("import matplotlib.pyplot as plt", language="python")

    st.subheader("Step 2: Create a Figure")
    st.code(
        """
plt.figure(figsize=(8, 4))
plt.plot(df['date'], df['cases'], label='Cases', linewidth=2)
        """,
        language="python"
    )

    st.subheader("Step 3: Add Titles and Labels")
    st.code(
        """
plt.title('Daily Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
        """,
        language="python"
    )

    st.subheader("Step 4: Save at High Quality")
    st.code(
        """
plt.savefig('daily_cases.png', dpi=300, bbox_inches='tight')
plt.show()
        """,
        language="python"
    )
    st.markdown("---")

# Section: Interactive Charts

def show_interactive():
    st.header("Interactive Charts")
    st.subheader("Step 1: Import Plotly Express")
    st.code("import plotly.express as px", language="python")

    st.subheader("Step 2: Build Your Figure")
    st.code(
        """
fig = px.line(
    df,
    x='date',
    y='cases',
    title='Interactive Case Trend'
)
        """,
        language="python"
    )

    st.subheader("Step 3: Customize Aesthetics")
    st.code("fig.update_layout(template='plotly_white')", language="python")

    st.subheader("Step 4: Display in Streamlit")
    st.code("st.plotly_chart(fig, use_container_width=True)", language="python")
    st.markdown("---")

# Section: Download eBook

def show_download():
    st.header("Download the Full eBook")
    st.subheader("Step 1: Ensure PDF Exists")
    st.write("Place `health_data_python_guide.pdf` in the app directory.")
    st.subheader("Step 2: Download Button")
    try:
        with open("health_data_python_guide.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📥 Download Full PDF Guide",
            data=PDFbyte,
            file_name="health_data_python_guide.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.error("PDF guide not found. Add `health_data_python_guide.pdf` to the directory.")

if __name__ == "__main__":
    main()
