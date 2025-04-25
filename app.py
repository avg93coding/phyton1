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
    st.title("Python for Health Data: Beginners Welcome (Dummies Edition)")
    st.markdown(
        "Welcome to the ultimate beginner's guide for using Python in health and epidemiology data visualization! "
        "This interactive mini-book will walk you through each concept step by step, with clear examples and exercises."
    )
    st.markdown("---")

# Section: What is Python?

def show_what_is_python():
    st.header("What is Python?")
    st.markdown(
        "Python is a versatile, high-level programming language used worldwide in data science, web development, automation, and more."
    )
    st.markdown("**Key Features:**")
    st.write(
        "- *Easy-to-read syntax* resembling pseudocode",
        "- *Interpreted* (no compilation step),",
        "- *Cross-platform* (Windows, MacOS, Linux),",
        "- *Large ecosystem* of libraries (over 200k packages on PyPI).",
        sep="\n"
    )
    st.markdown("---")

# Section: Why Python?

def show_why_python():
    st.header("Why Python for Health Data?")
    st.markdown("**Benefits:**")
    st.write(
        "1. Robust data tools: Pandas, NumPy, SciPy for cleaning & analysis",
        "2. Visualization libraries: Matplotlib, Seaborn, Plotly for static & interactive plots",
        "3. Reproducibility: share your code/notebooks with colleagues",
        "4. Integration: connect to databases (SQL), APIs (FHIR), and other languages",
        sep="\n"
    )
    st.markdown("**Real-world examples:**")
    st.write(
        "- COVID-19 dashboards built with Plotly Dash",
        "- Epidemiology analyses using Jupyter Notebooks",
        "- Automated reporting via scripts and cron jobs",
        sep="\n"
    )
    st.markdown("---")

# Section: Your First Steps

def show_setup():
    st.header("Your First Steps")
    st.markdown("**1. Install Anaconda or Miniconda:**")
    st.write(
        "- Go to https://www.anaconda.com/products/distribution",
        "- Download the Python 3.x installer for your OS",
        "- Follow the on-screen prompts to install",
        sep="\n"
    )
    st.markdown("**2. Create and activate a virtual environment:**")
    st.code(
        """
conda create -n health_data python=3.9 -y
conda activate health_data
pip install streamlit pandas matplotlib plotly
        """,
        language="bash"
    )
    st.markdown("**3. Launch Jupyter Notebook (optional):**")
    st.write(
        "Open your terminal or Anaconda Prompt and run:",
        "```bash
jupyter notebook
```",
        sep="\n"
    )
    st.markdown("---")

# Section: Starter Commands

def show_starter_commands():
    st.header("Starter Commands")
    st.markdown("Load and preview your health dataset:")
    code = '''
import pandas as pd    # Load the Pandas library
# Read a CSV file into a DataFrame
df = pd.read_csv("data.csv")
# Show first 5 rows
print(df.head())
# Display summary statistics
df.describe()
    '''
    st.code(code, language="python")
    st.write(
        "*Explanation:* `read_csv()` reads your data, `head()` previews it, and `describe()` summarizes numeric columns."
    )
    st.markdown("---")

# Section: Understanding Data Types

def show_data_types():
    st.header("Understanding Data Types")
    st.markdown("Pandas uses various data types to represent columns:")
    st.write(
        "- **int64:** integer numbers",
        "- **float64:** decimal numbers",
        "- **object:** text or mixed types",
        "- **datetime64[ns]:** dates and times",
        sep="\n"
    )
    st.markdown("**Check and convert types:**")
    type_code = '''
# Check column types
df.dtypes
# Convert a column to datetime
df['date'] = pd.to_datetime(df['date'])
# Convert numeric strings to floats
df['value'] = df['value'].astype(float)
    '''
    st.code(type_code, language="python")
    st.markdown("---")

# Section: Customize and Save Plots

def show_customize_plots():
    st.header("Customize and Save Plots")
    st.markdown("Learn how to style Matplotlib charts and save them:")
    plot_code = '''
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.plot(df['date'], df['cases'], label='Cases', linewidth=2)
plt.title('Daily Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
# Save figure at high resolution
plt.savefig('daily_cases.png', dpi=300, bbox_inches='tight')
plt.show()
    '''
    st.code(plot_code, language="python")
    st.write(
        "*Tip:* Use `figsize`, `label`, and `legend` to make your charts publication-ready."
    )
    st.markdown("---")

# Section: Interactive Charts

def show_interactive():
    st.header("Interactive Charts")
    st.markdown("Build interactive plots with Plotly Express and embed in Streamlit:")
    interact_code = '''
import plotly.express as px

fig = px.line(df, x='date', y='cases', title='Interactive Case Trend')
fig.update_layout(template='plotly_white')
# Display in Jupyter: fig.show()
# Display in Streamlit:
st.plotly_chart(fig, use_container_width=True)
    '''
    st.code(interact_code, language="python")
    st.write(
        "Customize tooltips, colors, and layout via `update_traces()` and `update_layout()`."
    )
    st.markdown("---")

# Section: Download eBook

def show_download():
    st.header("Download the Mini eBook")
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
        st.error(
            "PDF guide not found. Please add `health_data_python_guide.pdf` in the app directory."
        )

if __name__ == "__main__":
    main()
