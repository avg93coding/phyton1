import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit App: Python for Health Data Mini-eBook (For Absolute Beginners)

def main():
    st.set_page_config(
        page_title="Python for Health Data - Dummies Guide", layout="wide"
    )
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to", [
            "Introduction",
            "What is Python?",
            "Why Python?",
            "Setup Environment",
            "Your First Script",
            "Load & Preview Data",
            "Understand Data Types",
            "Customize & Save Plots",
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
    elif page == "Setup Environment":
        show_setup()
    elif page == "Your First Script":
        show_hello_world()
    elif page == "Load & Preview Data":
        show_load_preview()
    elif page == "Understand Data Types":
        show_data_types()
    elif page == "Customize & Save Plots":
        show_customize_plots()
    elif page == "Interactive Charts":
        show_interactive()
    elif page == "Download eBook":
        show_download()

# Section: Introduction

def show_introduction():
    st.title("Python for Health Data: Step-by-Step for Absolute Beginners")
    st.markdown(
        "**No jargon, no assumptions.** In this guide, each section is broken into tiny steps that anyone can follow—from installing Python to building interactive charts."
    )
    st.markdown("---")

# Section: What is Python?

def show_what_is_python():
    st.header("What is Python?")
    st.subheader("Step 1: Define Python")
    st.write(
        "Python is a **programming language** used to write instructions that a computer can execute."
    )
    st.subheader("Step 2: Why Python?")
    st.write(
        "- Readable syntax (looks like English)",
        "- Huge community & libraries",
        "- Runs on Windows, Mac, Linux",
        sep="\n"
    )
    st.subheader("Step 3: Try the Python Shell")
    st.write(
        "Open your terminal or command prompt and type `python` (or `python3`)."
    )
    st.code(
        ">>> python",
        language="bash"
    )
    st.write(
        "Then type: `print('Hello, Python!')` and press Enter. You should see `Hello, Python!` printed back."
    )
    st.markdown("---")

# Section: Why Python?

def show_why_python():
    st.header("Why Python for Health Data?")
    st.subheader("Step 1: Data Tools Built-In")
    st.write("Libraries like Pandas, NumPy, and SciPy simplify data cleaning, analysis, and calculations.")
    st.subheader("Step 2: Visualization Made Easy")
    st.write("Use Matplotlib, Seaborn, and Plotly to turn numbers into clear charts.")
    st.subheader("Step 3: Shareable Workflows")
    st.write("Jupyter Notebooks and Streamlit apps let you show your colleagues both code and results in one place.")
    st.markdown("---")

# Section: Setup Environment

def show_setup():
    st.header("Setup Your Python Environment")
    st.subheader("Step 1: Open a Terminal or Command Prompt")
    st.write(
        "- **Windows**: Search 'cmd' or 'PowerShell'.",
        "- **Mac**: Open 'Terminal'.",
        "- **Linux**: Open your Terminal emulator.",
        sep="\n"
    )
    st.markdown("---")
    st.subheader("Step 2: Download and Install Python")
    st.write(
        "1. Go to https://www.python.org/downloads/",
        "2. Download the latest Python 3.x installer for your OS.",
        "3. Run the installer and **check 'Add Python to PATH'**.",
        sep="\n"
    )
    st.markdown("---")
    st.subheader("Step 3: Verify Python Installation")
    st.code(
        "python --version",
        language="bash"
    )
    st.write("You should see something like `Python 3.9.7`.")
    st.markdown("---")
    st.subheader("Step 4: Install Anaconda (Recommended)")
    st.write(
        "1. Go to https://www.anaconda.com/products/distribution",
        "2. Download and install for your OS.",
        sep="\n"
    )
    st.markdown("---")
    st.subheader("Step 5: Create a Virtual Environment")
    st.code(
        "conda create -n health_data python=3.9 -y\nconda activate health_data",
        language="bash"
    )
    st.write(
        "This keeps your project dependencies separate and easy to manage."
    )
    st.markdown("---")
    st.subheader("Step 6: Install Required Libraries")
    st.code(
        "pip install streamlit pandas matplotlib plotly",
        language="bash"
    )
    st.write("Now you're ready to run Python data scripts and Streamlit apps.")
    st.markdown("---")

# Section: Your First Script

def show_hello_world():
    st.header("Your First Python Script")
    st.subheader("Step 1: Create a new file")
    st.write("In your project folder, create `hello.py` with the following line:")
    st.code(
        "print('Hello, World!')",
        language="python"
    )
    st.subheader("Step 2: Run the script")
    st.write("In your terminal, navigate to the folder and type:")
    st.code(
        "python hello.py",
        language="bash"
    )
    st.write("You should see `Hello, World!` printed.")
    st.markdown("---")

# Section: Load & Preview Data

def show_load_preview():
    st.header("Load & Preview Data")
    st.subheader("Step 1: Import Pandas")
    st.code(
        "import pandas as pd",
        language="python"
    )
    st.subheader("Step 2: Read a CSV File")
    st.code(
        "df = pd.read_csv('data.csv')",
        language="python"
    )
    st.subheader("Step 3: Preview with head()")
    st.code(
        "df.head()  # Display first 5 rows",
        language="python"
    )
    st.subheader("Step 4: Summary Stats")
    st.code(
        "df.describe()  # Summary of numeric columns",
        language="python"
    )
    st.markdown("---")

# Section: Understanding Data Types

def show_data_types():
    st.header("Understanding Data Types")
    st.subheader("Step 1: Check Column Types")
    st.code(
        "df.dtypes",
        language="python"
    )
    st.subheader("Step 2: Convert to Datetime")
    st.code(
        "df['date'] = pd.to_datetime(df['date'])",
        language="python"
    )
    st.subheader("Step 3: Convert Strings to Numbers")
    st.code(
        "df['value'] = df['value'].astype(float)",
        language="python"
    )
    st.markdown("---")

# Section: Customize & Save Plots

def show_customize_plots():
    st.header("Customize & Save Plots")
    st.subheader("Step 1: Import Matplotlib")
    st.code(
        "import matplotlib.pyplot as plt",
        language="python"
    )
    st.subheader("Step 2: Plot Data with Style")
    st.code(
        "plt.plot(df['date'], df['cases'], color='blue', linewidth=2)
plt.title('Daily Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.grid(True)
",language="python"
    )
    st.subheader("Step 3: Save High-Res Image")
    st.code(
        "plt.savefig('daily_cases.png', dpi=300, bbox_inches='tight')",
        language="python"
    )
    st.markdown("---")

# Section: Interactive Charts

def show_interactive():
    st.header("Interactive Charts")
    st.subheader("Step 1: Import Plotly Express")
    st.code(
        "import plotly.express as px",
        language="python"
    )
    st.subheader("Step 2: Create Interactive Figure")
    st.code(
        "fig = px.line(df, x='date', y='cases', title='Interactive Trends')",
        language="python"
    )
    st.subheader("Step 3: Display in Streamlit")
    st.code(
        "st.plotly_chart(fig, use_container_width=True)",
        language="python"
    )
    st.markdown("---")

# Section: Download eBook

def show_download():
    st.header("Download the Full eBook")
    st.subheader("Step 1: Place PDF in Directory")
    st.write("Add `health_data_python_guide.pdf` to this folder.")
    st.subheader("Step 2: Click to Download")
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
        st.error("PDF guide not found. Add it to the directory.")

if __name__ == "__main__":
    main()

