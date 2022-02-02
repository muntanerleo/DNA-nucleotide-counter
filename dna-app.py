# the altair library helps with the graphs and the PIL displays my dna image
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image 

# code below: loads the image to the web page.
image = Image.open('dna-logo.jpg')

# code below: expands the logo width
st.image(image, use_column_width=True)

# code below: this displays the header in the web page.
# the '***' at the end is for the horizontal line at the end of the short description.
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of a DNA Query!

***
""")

st.header('Enter DNA sequence')

# sample DNA sequence
sequence_input = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# this puts the text box in the web page
sequence = st.text_area("Sequence input", sequence_input, height=250)

# this will split the lines of the DNA query and create a list of each line.
sequence = sequence.splitlines()

# this line skips the sequence name (first line)
sequence = sequence[1:]

# this will concatenates list to string. making it a long line of DNA sequence that is already pre-processed and ready for computation.
sequence = ''.join(sequence)

st.write("""
***
""")

# prints the input DNA sequence from above.
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# there are different ways in which i can display the output
# but before displaying the output, i need to do some computation

# first i print the dictionary:
st.subheader('1. Print Dictionary')

# code below: i make a costum function that that counts the dna nucleotide from the sequence.
def DNA_nucleotide_count(seq):
  # here i make a dictionary that contains 4 members A,T,G,C. this will count how many members are in the dna sequence.
  # i use the .count function to do this.
  # at the end i will return the d variable which is a dictionary containing the nucleotide of A,T,G,C.
  d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
            ])
  return d

# assigns the function to X
X = DNA_nucleotide_count(sequence)
X

# second way to display the output is by printing the text:
# this makes it much easier for the user to read the data.
st.subheader('2. Print Text')
st.write('There are ' +str(X['A']) + ' adenine (A)')
st.write('There are ' +str(X['T']) + ' thymine (T)')
st.write('There are ' +str(X['G']) + ' guanine (G)')
st.write('There are ' +str(X['C']) + ' cytosine (C)')

# third way of displaying the output is by showing a dataframe
# i will have two columns in the dataframe. 1=nucleotide 2=count
# this dataframe will help build a bar chart in step 4 for the output
st.subheader('3. Display DataFrame')
# code below: creates a dataframe from the dictionary function
dataframe = pd.DataFrame.from_dict(X, orient='index')

# here i will rename the column because at default its 0
dataframe = dataframe.rename({0: 'count'}, axis='columns')
dataframe.reset_index(inplace=True)
dataframe = dataframe.rename(columns = {'index':'nucleotide'})
st.write(dataframe)

# fourth way of displaying the output would be using a Bar Chart by using the Altair library
st.subheader('4. Display Bar Chart')
# code below: this will create the actual plot
plot = alt.Chart(dataframe).mark_bar().encode(
  x='nucleotide',
  y='count'
)

# code below: adjusts the width of the bar because by default the bars are thin.
plot = plot.properties(
  width=alt.Step(80)
)
st.write(plot)