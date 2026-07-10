from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration is the study of outer space using satellites, telescopes, spacecraft, and astronauts. It has greatly expanded our understanding of the universe and led to many technological advancements that benefit everyday life, including GPS, weather forecasting, and communication systems. 

Missions to the Moon, Mars, and other planets have revealed valuable scientific discoveries. As technology continues to improve, future space exploration may enable humans to establish settlements on other planets and uncover evidence of life beyond Earth.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0,
    separators="\n"
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)