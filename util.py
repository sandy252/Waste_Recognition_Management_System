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
            st.header(pred + ' waste recycling techniques')
            st.markdown(str(info))


data = {
    "cardboard":
        """
            Cardboard recycling is the process of reusing cardboard waste by transforming it into new products. Cardboard is a type of paper-based material that is commonly used for packaging and shipping goods. Recycling cardboard helps to reduce the amount of waste that ends up in landfills and conserves natural resources by reducing the need for new cardboard production.
            Here are some methods of cardboard recycling:

            - Pulping: Pulping is the process of breaking down cardboard into its constituent fibers using water and chemicals. The resulting pulp can then be used to make new paper-based products, such as cardboard boxes, paper bags, and other packaging materials.

            - Shredding: Shredding involves shredding cardboard into small pieces, which can then be used as a packaging material or as a feedstock for other materials.

            - Compacting: Compacting involves compressing cardboard waste into bales or blocks, which can then be transported to recycling facilities for processing.

            - Reuse: Cardboard can also be reused for its original purpose, such as for packaging and shipping goods. Used cardboard boxes can be flattened and stored for future use.
        """,

    "glass":
        """
            Glass waste recycling is the process of transforming glass waste into new products, reducing the need for 
            virgin raw materials, and reducing the amount of waste sent to landfills. Here are some of the various 
            methods of glass waste recycling: 

            - Glass bottle and jar recycling: The most common method of glass waste recycling is to collect and recycle glass bottles and jars. The glass is crushed and melted down to make new bottles and jars. 
            
            - Glass cullet recycling: Cullet is broken or crushed glass that can be used as a raw material in glass manufacturing. Glass cullet can be recycled repeatedly without losing quality, and it reduces the amount of virgin raw materials required for glass production. 
            
            - Glass fiber recycling: Glass fibers are commonly used in insulation and other building materials. Waste glass fibers can be recycled by melting them down and using them as raw material for new glass fiber products. 
            
            - Aggregate for construction: Crushed glass can be used as an aggregate in construction materials such as concrete and asphalt. This helps to reduce the demand for virgin materials and can improve the sustainability of construction projects. 
            
            - Glass art and crafts: Some glass waste can be repurposed for art and craft projects. This includes using broken glass to create mosaics or sculptures, or melting down colored glass to create new decorative pieces. 
            
            - Glass sand: Glass waste can be crushed into a fine sand-like material that can be used as a substitute for traditional sand in various applications such as landscaping, sports fields, and construction. 
        """,

    "metal":
        """
            Metal recycling is the process of reusing metals to create new metal products. Here are some of the methods used for metal recycling:

            - Collection and sorting: The first step in metal recycling is to collect and sort the metal. This involves separating the metal by type, such as steel, aluminum, or copper.

            - Processing: The sorted metal is then processed to remove any contaminants, such as plastic or rubber. This may involve shredding or crushing the metal into smaller pieces.

            - Melting: The processed metal is then melted down in a furnace. The temperature required to melt the metal will depend on the type of metal being recycled.

            - Purification: Once the metal is melted, it may need to be purified to remove any impurities. This involves adding chemicals to the metal to separate any non-metallic elements.

            - Solidifying: Once the metal is purified, it is solidified into the desired shape. This may involve casting the metal into molds or rolling it into sheets.

            - Fabrication: The final step in metal recycling is to use the newly created metal products to create new metal products. This may involve cutting, welding, or otherwise shaping the metal into the desired form.
        """,

    "paper":
        """
           Paper recycling is the process of reusing old paper to create new paper products. Here are some of the methods used for paper recycling:

            - Collection and sorting: The first step in paper recycling is to collect and sort the paper. This involves separating the paper by type, such as cardboard, newspaper, or office paper.

            - Pulping: The sorted paper is then mixed with water and chemicals to create a slurry. This slurry is called pulp, and it is the basis for creating new paper products.

            - Screening and cleaning: The pulp is screened to remove any remaining contaminants, such as staples or paper clips. It is also cleaned to remove any ink or other substances.

            - De-inking: If the recycled paper is going to be used to create new white paper products, it must be de-inked. This involves using chemicals and mechanical processes to remove the ink and other substances from the pulp.

            - Bleaching: If the recycled paper is going to be used to create new white paper products, it may also need to be bleached. This involves using chemicals to remove any remaining color from the pulp.

            - Repulping and refining: The cleaned and de-inked pulp is then repulped and refined to create new paper products. This involves adding water and other additives to the pulp to create the desired texture and quality.

            - Papermaking: The final step in paper recycling is to use the refined pulp to create new paper products. The pulp is spread out onto a screen and pressed to remove any remaining water. It is then dried and rolled into large rolls of paper, which can be used to create a variety of paper products. 
        """,

    "plastic":
        """
            Plastic recycling is the process of reusing plastic waste by transforming it into new products. It involves the collection, sorting, cleaning, and processing of plastic waste to create new materials that can be used in the production of a wide range of products, including plastic bottles, containers, bags, and other items.
            Here are some methods of plastic recycling:

            - Mechanical recycling: This is the most common method of plastic recycling, which involves sorting, cleaning, and shredding the plastic waste into small pieces. These pieces are then melted and reformed into new plastic products.

            - Chemical recycling: Chemical recycling involves breaking down plastic waste into its constituent molecules using various chemical processes. These molecules can then be used to create new plastic products or other chemicals.

            - Feedstock recycling: Feedstock recycling is a process of converting plastic waste into feedstock or raw materials, which can be used to create new plastic products or other chemicals.

            - Energy recovery: In this method, plastic waste is burned to generate energy. This process is known as waste-to-energy or incineration.

            - Biodegradable plastics: Biodegradable plastics are designed to decompose naturally when exposed to the environment, such as through composting or biodegradation in landfills.

            - Upcycling: Upcycling is the process of transforming plastic waste into new, higher-value products. This involves converting plastic waste into other materials, such as fabrics or building materials, instead of simply recycling it into new plastic products.
        """,
 
    "Organic":
        """
            Organic waste recycling is the process of converting organic waste, such as food scraps, yard waste, and agricultural waste, into a useful product. Organic waste contains carbon-based materials, which can be decomposed naturally by microorganisms and turned into compost, biogas, or other valuable products.
            Here are some methods of recycling organic waste:

            - Composting: Composting is a natural process of decomposing organic waste, such as food scraps, yard waste, and leaves, into a nutrient-rich soil amendment. It involves combining the organic waste with soil and other organic materials in a compost bin or pile and allowing it to decompose over time.

            - Vermicomposting: Vermicomposting is a type of composting that uses worms to break down organic waste. It involves placing the organic waste in a container with worms, such as red wigglers, and allowing the worms to digest the waste and produce nutrient-rich worm castings.

            - Anaerobic digestion: Anaerobic digestion is a process of breaking down organic waste in the absence of oxygen to produce biogas, which can be used as a source of renewable energy. It involves placing the organic waste in a sealed container, such as a digester, and allowing bacteria to break down the waste and produce methane gas.

            - Incineration: Incineration is a process of burning organic waste at high temperatures to reduce its volume and generate energy. This process is typically used for large-scale waste management and is not considered a sustainable method of organic waste recycling.

            - Land application: Land application involves spreading organic waste on farmland as a fertilizer. This method can help to improve soil health and fertility, but it must be done carefully to prevent contamination and nutrient runoff.
        """,

}
