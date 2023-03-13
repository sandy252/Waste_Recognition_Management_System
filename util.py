import smtplib
from email.message import EmailMessage
import streamlit as st


def notify():
    name = st.text_input('Full Name')
    number = st.text_input('PhoneNo')
    location = st.text_input('Location Details')

    email_id = 'sandeep252kashyap@gmail.com'
    password = 'ucowoaurrcisbafj'

    msg = EmailMessage()
    msg['Subject'] = "Waste Mangagement"
    msg['From'] = email_id
    msg['To'] = 'kashyapsandeep252@gmail.com'

    msg.set_content(f"Name : {name} \nphone_no: {number}\nlocation: {location}\nplease collect the waste from this "
                    f"place")

    uploaded_file = st.camera_input("Take a picture of waste")
    if uploaded_file is not None:
        # Read the image file as bytes
        image_bytes = uploaded_file.read()
        msg.add_attachment(image_bytes, maintype='image', subtype='jpeg', filename='image.jpg')

        if st.button("Send mail"):
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(email_id, password)
                smtp.send_message(msg)

            # Display a message to the user
            st.success('Email sent!')


def info(prediction):
    for pred in data.keys():
        if pred == prediction:
            info = data[pred]
            st.header(pred + ' recycling techniques')
            st.markdown(str(info))


data = {
    "cardboard":
        "Battery recycling is a recycling activity that aims to reduce the number of batteries being disposed as "
        "municipal solid waste. Batteries contain a number of heavy metals and toxic chemicals and disposing of them "
        "by the same process as regular household waste has raised concerns over soil contamination and water "
        "pollution.<br><br> Most types of batteries can be recycled. However, some batteries are recycled more "
        "readily than others, such as lead–acid automotive batteries (nearly 90% are recycled) and button cells ("
        "because of the value and toxicity of their chemicals). Rechargeable nickel–cadmium (Ni-Cd), nickel metal "
        "hydride (Ni-MH), lithium-ion (Li-ion) and nickel–zinc (Ni-Zn), can also be recycled. There is currently no "
        "cost-neutral recycling option available for disposable alkaline batteries, though consumer disposal "
        "guidelines vary by region.",

    "glass":
        "Textile recycling is the process of recovering fiber, yarn or fabric and reprocessing the textile "
        "material into useful products. Textile waste products are gathered from different sources and are then "
        "sorted and processed depending on their condition, composition, and resale value. The end result of this "
        "processing can vary, from the production of energy and chemicals to new articles of clothing.<br><br>Due "
        "to a recent trend of over consumption and waste generation in global fashion culture, textile recycling "
        "has become a key focus of worldwide sustainability efforts. Globalization has led to a \"fast fashion\" "
        "trend where clothes are considered by many consumers to be disposable due to their increasingly lower "
        "prices. The development of recycled technology has allowed the textile industry to produce vast amounts "
        "of products that deplete natural resources.",

    "metal":
        "Electronic waste or e-waste describes discarded electrical or electronic devices. Used electronics which "
        "are destined for refurbishment, reuse, resale, salvage recycling through material recovery, or disposal "
        "are also considered e-waste. Informal processing of e-waste in developing countries can lead to adverse "
        "human health effects and environmental pollution.<br><br>Electronic scrap components, such as CPUs, "
        "contain potentially harmful materials such as lead, cadmium, beryllium, or brominated flame retardants. "
        "Recycling and disposal of e-waste may involve significant risk to health of workers and their "
        "communities.<br><br>E-waste or electronic waste is created when an electronic product is discarded after "
        "the end of its useful life. The rapid expansion of technology and the consumption driven society results "
        "in the creation of a very large amount of e-waste in every minute.",

    "paper":
        "Glass recycling is the processing of waste glass into usable products. Glass that is crushed and ready "
        "to be remelted is called cullet. There are two types of cullet: internal and external. Internal cullet "
        "is composed of defective products detected and rejected by a quality control process during the "
        "industrial process of glass manufacturing, transition phases of product changes (such as thickness and "
        "colour changes) and production offcuts. External cullet is waste glass that has been collected or "
        "reprocessed with the purpose of recycling. External cullet (which can be pre- or post-consumer) is "
        "classified as waste. The word \"cullet\", when used in the context of end-of-waste, will always refer to "
        "external cullet.<br><br>To be recycled, glass waste needs to be purified and cleaned of contamination. "
        "Then, depending on the end use and local processing capabilities, it might also have to be separated "
        "into different colors. Many recyclers collect different colors of glass separately since glass retains "
        "its color after recycling.",

    "plastic":
        "Recycling prevents the release of hazardous materials into the environment. Mercury, an extremely toxic "
        "heavy metal, is used in fluorescent light bulbs to increase energy efficiency. In addition to mercury, "
        "some HID bulbs contain radioactive substances like Krypton-85 and thorium used for quick and easy light "
        "ignition. LEDs on the other hand do not contain mercury; but, they do contain nickel, lead, "
        "and trace amounts of arsenic. Light bulbs often break when thrown into a dumpster, trash can or "
        "compactor, or when they end up in a landfill or incinerator. This causes the release of hazardous "
        "materials into the environment and can create serious public and environmental health "
        "concerns. It’s also important to remember that recycling allows the reuse of the glass, "
        "metals and other materials that make up light bulbs. Virtually all components of light bulbs can be "
        "recycled.",
    "trash":
        "Several kinds and also large amounts of metals are used in industrial processes every day. Since the "
        "industrial revolution period has taken place, our consumption levels skyrocketed due to the mass "
        "production of goods and the resulting low unit price.<br><br>The most consumed metal worldwide is "
        "aluminum, followed by copper, zinc, lead and nickel. Moreover, some precious materials like gold are "
        "used for our computers and other electronic devices.<br><br>Metal is therefore crucial to sustaining our "
        "living standard. However, metals are resources that are limited. The depletion of metals can be a big "
        "issue in the future since the world population grows rapidly and thus also the demand for goods made out "
        "of metal will increase.<br><br>To mitigate the problem of metal depletion, we have to look out for "
        "effective measures. One of those measures could be metal recycling.",

    "Organic":
        "Organic wastes contain materials which originated from living organisms. There are many types of organic "
        "wastes and they can be found in municipal solid waste , industrial solid waste , agricultural waste, "
        "and wastewaters. Organic wastes are often disposed of with other wastes in landfills or incinerators, "
        "but since they are biodegradable , some organic wastes are suitable for composting and land "
        "application.<br><br>Organic materials found in municipal solid waste include food, paper, wood, "
        "sewage sludge , and yard waste. Because of recent shortages in landfill capacity, the number of "
        "municipal composting sites for yard wastes is increasing across the country, as is the number of "
        "citizens who compost yard wastes in their backyards. On a more limited basis, some mixed municipal waste "
        "composting is also taking place. In these systems, attempts to remove inorganic materials are made prior "
        "to composting.<br><br>Food waste from restaurants and grocery stores is typically disposed of through "
        "garbage disposals, therefore, it becomes a component of wastewater and sewage sludge.",

}
