import streamlit as st
from PIL import Image
from PIL import ImageOps # to rotate iphone images

st.markdown("<h1 style='text-align: center; color: black;'>👀 Danny's Submission for the Position of Begum's Boyfriend</h1>", unsafe_allow_html=True)

st.write(
    "In this application, I'll walk you through Danny's pros and pros (he's a flawless person JK) and why you should consider him as your " \
    "boyfriend. Hopefully you will fall in love with him after reading this."
)

herImage = Image.open('her.jpg').resize((350, 350))
meImage = Image.open('me.jpg').resize((350, 300))
meImage = ImageOps.exif_transpose(meImage)

st.image(
    [herImage, meImage]
)

st.markdown(
    ":small[**Look how cute they look together 😳**]"
)

st.markdown(
    "&nbsp; &nbsp; &nbsp; &nbsp;First of all, Danny is a lover boy. To list a few, He will treat you like a princess." \
    " He will open and hold every door for you, pull out the chair when you sit down " \
    " for you, and drive you everywhere as long as you handle aux (he doesn't mind " \
    " girly music). Yes, acts of service is one of his love languages."
)

st.write('-------------------------------------------------------------------')

st.markdown(
    "&nbsp; &nbsp; &nbsp; &nbsp;Second, Danny is fun and adventurous. Instead of cliche tourist destinations like Cancun" \
    " or Cabo, he will take you to explore bars and clubs in Ensenada and"
    " local taco stands in Rosarito. You guys can even get a couple massage in Tijuana."
)
st.image(
    [Image.open('tacos.JPG').resize((250, 350)), Image.open('hotel.JPG').resize((250, 350)), Image.open('bar.JPG').resize((350, 350))], 
    ['Taco Stand', 'Hotel View', 'Local Bar Buried in $ Bills']
)

st.write('-------------------------------------------------------------------')

st.markdown(
    "&nbsp; &nbsp; &nbsp; &nbsp;Moreover, Danny is fun and has a lot of hobbies, and you will never feel"
    " bored around him. He is into Indie" \
    " music, EDM, and Rap music. Hopefully you are a music lover too and you guys will go to a lot of concerts together. " \
    " Danny is also a runner, a rollerblader, and a gym-goer. He is currently" \
    " training for the Orange County Half Marathon race. He is also designing his next tattoos on his laptop. "
)

st.image(
    [Image.open('run.PNG').resize((250, 500)), 
     Image.open('tattoo.JPG').resize((440, 350)), 
     ImageOps.exif_transpose(Image.open('rave.JPEG').resize((350, 270)))], 
    ['Half Marathon Training', 'Tattoo Design WIP', 'ISOKNOCK 4EVER Concert Pregame']
)

st.write('-------------------------------------------------------------------')

st.markdown(
    "&nbsp; &nbsp; &nbsp; &nbsp;Last but not least, Danny loves food - and boy can" \
    " he cook. Danny enjoys cooking as much " \
    " as he likes trying out different restaurants and cheap eats. As a first " \
    "-generation immigrant, Danny specializes in Chinese dishes that are healthy"
    " and nutritious to sustain his active lifestyle. He will also make whatever" \
    " you are craving happen. One thing I can gurantee you" \
    " is that you will never starve with him."
)

st.image(
    [Image.open('Red Braised Pork.JPEG').resize((220, 175)), 
     Image.open('BBQ Pork Char Siu.jpg').resize((220, 175)), 
     Image.open('Baked Salmon.jpg').resize((220, 175))], 
    ['Red Braised Pork', 'BBQ Pork Char Siu', 'Baked Salmon']
)

st.write('-------------------------------------------------------------------')

st.markdown(
    "## *Bonus: Why is Danny the perfect candidate for your August wedding +1*"
)

st.markdown(
    "He's tall and handsome, has a good career and a good degree, decent and funny" \
    " at the same time. And most importantly, you guys might end up getting married too 😌"
)

st.image(
    Image.open('firstDateSc.png')
)