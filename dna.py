# Imports

import pandas as pd
import streamlit as st
import altair as alt

# Start Web App

st.set_page_config(page_title="DNA Nucleotide Count", page_icon="dna.png")

st.write("""

# DNA Nucleotide Count

Count the nucleotide composition of query DNA.

---
""")

# DNA Input

st.header("Enter DNA Sequence")

# Example Sequence
sequence_input = ">DNA Query\nTCGGGTGCCTCTAGTGGCTGGCTAGATAGACTAGCCGCTGGTAAACACACCATGACCCCGGCTCTCCATTGATGCCACGGCGATTGTTGGAGAGCCAGCA\nGCGACTGCAAACATCAGATCAGAGTAATACTAGCATGCGATAAGTCCCTAACTGACTATGGCCTTCTGTAGAGTCAACTTCACCACATATGCTGTCTCTG\nGCACGTGGATGGTTTAGAGGAATCAGATTCAAGTCTGGTTAACCATCAAACAGGTCTTGAGTCTAAAATTGTCGTCTCCTGCGTACGAGATGGAAATACT"

# Set up Text Area
sequence = st.text_area("Sequence Input", sequence_input, height=250)

# Split Lines so that every line is its own element in variable sequence
sequence = sequence.splitlines()

# Save the DNA Query Name
dna_query_name = sequence[0].replace(">", "")

# Skips the sequence name
sequence = sequence[1:]

# Concat list to string
sequence = "".join(sequence)

st.write("""
---         
""")

# Print the input DNA sequence
st.header(f"Input ({dna_query_name})")
st.write(sequence)

# DNA Nucleotide Count
st.header("Output (DNA Nucleotide Count)")

# Make a Dictionary


def DNA_N_Count(seq):
    '''
    Makes a Dictionary based on the DNA Nucleotide sequence given.
    '''
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C")),
    ])
    return d


# Run function using input
X = DNA_N_Count(sequence)

# Stuff everything into data frame for easy access in bar graph
df = pd.DataFrame.from_dict(X, orient="index")

# Rename count column
df = df.rename({0: "Count"}, axis="columns")

# Add new column for necleotides
df.reset_index(inplace=True)

# Rename the nucleotide column
df = df.rename(columns={"index": "Nucleotide"})

# Display as Data Frame for easy viewing of count
st.subheader("Data Frame")
st.write(df)

# Display info as a Bar Graph
st.subheader("Bar Graph")

# Make our Bar Graph
p = alt.Chart(df).mark_bar().encode(
    x="Nucleotide",
    y="Count"
)
p = p.properties(
    width=alt.Step(80)  # Control width of bars
)

# Display Bar Graph
st.write(p)
