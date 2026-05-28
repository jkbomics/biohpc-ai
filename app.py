import streamlit as st
import os

from utils.yaml_loader import load_tool_config
from estimators.resource_estimator import estimate_resources
from estimators.scheduler_generator import generate_slurm

KNOWLEDGEBASE_DIR = "knowledgebase"

tool_paths = {}

# Load all YAML tools dynamically
for domain in os.listdir(KNOWLEDGEBASE_DIR):

    domain_path = os.path.join(
        KNOWLEDGEBASE_DIR,
        domain
    )

    if os.path.isdir(domain_path):

        for file in os.listdir(domain_path):

            if file.endswith(".yaml"):

                tool_name = file.replace(
                    ".yaml",
                    ""
                )

                tool_paths[tool_name] = os.path.join(
                    domain_path,
                    file
                )

# Streamlit UI
st.title("BioHPC-AI")

st.write(
    "AI-powered HPC recommendation engine "
    "for bioinformatics workflows."
)

selected_tool = st.selectbox(
    "Select Tool",
    sorted(tool_paths.keys())
)

samples = st.number_input(
    "Number of Samples",
    min_value=1,
    value=10
)

data_size = st.number_input(
    "Total Dataset Size (GB)",
    min_value=1,
    value=50
)

scheduler = st.selectbox(
    "Scheduler",
    ["SLURM"]
)

# Generate recommendation
if st.button("Generate Recommendation"):

    config = load_tool_config(
        tool_paths[selected_tool]
    )

    resources = estimate_resources(
        config,
        data_size
    )

    slurm_script = generate_slurm(
        selected_tool,
        resources["cpus"],
        resources["ram_gb"],
        resources["runtime_hours"]
    )

    st.subheader("Recommended Resources")

    st.write(
        f"CPUs: {resources['cpus']}"
    )

    st.write(
        f"RAM: {resources['ram_gb']} GB"
    )

    st.write(
        f"Estimated Runtime: "
        f"{resources['runtime_hours']} hours"
    )

    st.subheader("Generated SLURM Script")

    st.code(
        slurm_script,
        language="bash"
    )

    st.subheader("Tool Characteristics")

    st.json(
        config["resource_behavior"]
    )