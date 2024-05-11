import streamlit as st
from gather import gather

def main():
    st.markdown(
            '<div style="text-align:center"><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDlhMDN3MncyZWRkemh5b2h0cmI2bWUwaTN3MmZkaTJ6cWJtZGxvNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1QGRJ9cOTbh5K/giphy.gif" width="500" height="150"></div>',
            unsafe_allow_html=True
        )
    st.markdown('<h1 style="text-align: center;">InFo_hUnT</h1>', unsafe_allow_html=True)
    input_data = st.text_input("Enter your word")
    if input_data:
        keyword = "_".join(input_data.strip().split())
        details, paragraphs = gather(keyword)

        if details:
            st.write("### Structured Data '{}'".format(input_data))
            for detail in details:
                rows = detail.find_all('tr')
                for row in rows:
                    heading = row.find('th')
                    detail = row.find('td')
                    if heading and detail:
                        st.write("**{}:** {}".format(heading.text.strip(), detail.text.strip()))
        else:
            st.write(" Stuctured data not yet available for '{}'".format(input_data))
        
        st.write("### Summary for '{}'".format(input_data))
        for paragraph in paragraphs:
            st.write(paragraph.text.strip())

if __name__ == "__main__":
    main()
