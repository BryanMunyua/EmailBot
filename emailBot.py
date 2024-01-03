import re
import os
from email.message import EmailMessage
import ssl
import smtplib
import csv

text_sample = """Skip to main contentTurn off continuous scrolling
Accessibility help
Accessibility feedback
Google
site:linkedin.com/in/"ceo" or "founder" "market" "United Kingdom" "England" "@gmail.com"

All
NewsMapsBooksImagesMore
Tools
SafeSearch
About 42,500 results (0.75 seconds) 
No results found for site:linkedin.com/in/"ceo" or "founder" "market" "United Kingdom" "England" "@gmail.com".
Results for site:linkedin.com/in/ ceo or founder market United Kingdom England @gmail.com (without quotes):

Seb Batiste(LION)(sjeanbatiste7@gmail.com) - CEO

linkedin.com
https://uk.linkedin.com › southlondonseoexpert
South Croydon, England, United Kingdom · CEO · SouthLondonSEOExpert
I offer Local Business Marketing to small and medium sized businesses. Website development and traffic growth to increase online revenue, ...

Biju Kariyil - FIRSTRING MEDIA www.firstringmedia.co.uk

linkedin.com
https://uk.linkedin.com › bijukariyil
I am Biju Kariyil , Managing Director of FIRSTRING MEDIA, FIRSTRING MEDIA is a digital marketing and promotion company.which is working with new and ...

Paul Shipley - Owner - Origin UK

linkedin.com
https://uk.linkedin.com › mrpaulshipley
Origin UK specialise in one of a kind, Artisan made jewellery pieces. Using only high quality materials and ethically sourced gemstones from around the world to ...

Caroline Harrison - CEO / Owner - Invest In A Better Africa

linkedin.com
https://uk.linkedin.com › ...
Caroline Harrison. Director of Digital Marketing, HSBC UK. London. 234 others named Caroline Harrison in United Kingdom are on LinkedIn. See others named ...

Jessica Caswell-James - Founder & CEO - Shorso

linkedin.com
https://uk.linkedin.com › ...
United Kingdom · Founder & CEO · Shorso
Experienced in providing leadership across all product & business development, including managing various sales & marketing campaigns both in the UK and ...

Toby Anres - Founder | Director | CEO at TobysocialIn.co.uk

linkedin.com
https://uk.linkedin.com › tobyanres
Toby Anres. ◾️The LinkedIners ◾️Branding Expert ◾️Social Media Marketing ◾️ Lead-Gen Specialist ◾️ For Professionals, ...

Eddie Okutu - CEO & Founder - OKU2 STUDIOS

linkedin.com
https://uk.linkedin.com › eddie-okutu
Founder & CEO of Oku2 Studios, an independent studio and production company based in the heart of London. Creating video strategies and delivering quality ...

Rafid Nassir - Co-Founder & Marketing Director - Luna Lee ...

linkedin.com
https://uk.linkedin.com › rafidnassir
I oversee all client projects, calculate strategies for each one and ensure all work is on track, with the help of my team of geniuses! As well as this, ...

Kash Withakay - CEO - Cryptosage.co.uk

linkedin.com
https://uk.linkedin.com › ...
CEO and Co-Founder at SaaScada Limited. London · Connect · Jay Peeples. Dallas, TX ... Head of Sales - UHNW, Off-Market Hotels,Trophy Assets//Land/Development ...

Nigel Warner - Founder and CEO - N W Marketing

linkedin.com
https://uk.linkedin.com › nigel-warner-39754017
Leicester, England, United Kingdom · Founder and CEO · N W Marketing
Nigel Warner. Professional Internet Marketer and Business Coach. N W Marketing University of Leicester. Leicester, England, United Kingdom.

Us Man - Founder - Britain SEO Consultants

linkedin.com
https://uk.linkedin.com › ...
United Kingdom · Founder · Britain SEO Consultants
... marketing, keyword analysis, SEO (Search Engine Optimization), SEO content development, Organic keywording and traffic. e-mail: usahmad146@gmail.com | Learn ...

Emmanuel Digispace Marketing - Owner and Creative ...

linkedin.com
https://uk.linkedin.com › emmanuel-digispace-marketing...
London, England, United Kingdom · Owner and Creative Director · Digispace Marketing
Emmanuel Digispace Marketing. Digital Marketing Consultant. Help businesses achieve their goals. Digispace Marketing School of Life. London, England, United ...

Carlo Devlieger - Associate Founder - Pivotal Peak UK

linkedin.com
https://www.linkedin.com › ...
Strategic marketing (re)design and implementation, Webdevelopment, software development, app development, web communication management, data visualization, ...

Tafhim Kiani - Founder and CEO - WLC - International

linkedin.com
https://uk.linkedin.com › tafhim-kiani
Amazon FBA Seller. amazon 3rd party seller. Nov 2017 - Present 6 years 2 months. London, England, United Kingdom.

Muhammad Danish - Chief Executive Officer

linkedin.com
https://uk.linkedin.com › danishtalksmarketing
London, England, United Kingdom. 1K followers 500+ connections. See your ... Muhammad Danish - CEO/Founder at Reconnectors, Top-Rated Freelancer offers ...

Samuel Adebiyi - Founder - Adtony

linkedin.com
https://uk.linkedin.com › samuel-adebiyi-19407134
Founder at Papsonsports. Adtony. London, England, United Kingdom. 2K followers ... Websites. Personal Website: http://www.ceo.papsonnetwork.co.uk External link.

Mikail Aleem - Chief Executive Officer - Aleemscorner

linkedin.com
https://uk.linkedin.com › mikail-aleem-207422168
... gmail.com. | Learn more about Mikail Aleem's work experience, education ... May 2023 - Present 8 months. London, England, United Kingdom. I am the CEO and founder ...

Damon Oldcorn - Founder

linkedin.com
https://uk.linkedin.com › damonoldcorn
Easton Royal, England, United Kingdom · Founder · OLDCORN & OLDCORN LLP
Easton Royal, England, United Kingdom. 2K followers 500+ connections. See your ... Interim roles as CEO and marketing director to emerging technology companies ...

Jane Efagwu - Founder and CEO - The Refined Advisory

linkedin.com
https://uk.linkedin.com › ...
... market; deliverables that are as solid and as captivating as this copy you ... Saint Paul's, England, United Kingdom. 433 followers 305 connections. See your ...

Barnabas Dada - CEO and founder - Miracle Mane

linkedin.com
https://uk.linkedin.com › barnabas-dada
London, England, United Kingdom · CEO and founder · Miracle Mane
... gmail.com | Learn more about Barnabas Dada's work experience, education, connections ... Apr 2019 - Sep 2021 2 years 6 months. London, England, United Kingdom.

Jaymes Payten - Founder & CEO - JAYPAY

linkedin.com
https://uk.linkedin.com › jaymespayten
London, England, United Kingdom · Founder & CEO · JAYPAY
... Marketing Agency | The Brandpreneur You've Been Looking for. JAYPAY Anglia Ruskin University. London, England, United Kingdom. 18K followers 500+ ...

Stuart Taylor - UK Country Director - Justdiggit

linkedin.com
https://uk.linkedin.com › stuarttaylor1
London, England, United Kingdom · UK Country Director · Justdiggit
... founder and chair of the Newspaper Marketing agency. Email: sstu.taylor ... CEO UK. Kinetic Worldwide. Jan 2013 - Jun 2019 6 years 6 months. London, United ...

David Wills (LION) (wealthandmoney@gmail.com) - Owner

linkedin.com
https://uk.linkedin.com › david-wills-lion-wealthandmon...
Bedworth, England, United Kingdom · Owner · DMW Marketing
David Wills (LION) (wealthandmoney@gmail.com). Owner at DMW Marketing. DMW Marketing. Bedworth, England, United Kingdom. 1K ...

Harry Jackson - Founder - wehatethecold

linkedin.com
https://uk.linkedin.com › harry-jackson-socialmediaexpert
Felixstowe, England, United Kingdom · Founder · wehatethecold
Solihull, England, United Kingdom. Gelato Sounds UK Graphic. Marketing Manager. Gelato Sounds UK. Mar 2017 - Nov 2019 2 years 9 months. Birmingham, United ...

Miriam Kay - Business Coach and Ambassador

linkedin.com
https://uk.linkedin.com › miriamkay
CEO & Founder of The Dora Foundation. -. Miriam Kay Graphic. Business Coach/Marketing Strategist. Miriam Kay. Jul 2017 - Present 6 years 6 months. United ...

silvia Sánchez Santiago - Business Owner - Tapas catering

linkedin.com
https://uk.linkedin.com › ...
Birmingham, England, United Kingdom · Business Owner · Tapas catering
Business Owner at Tapas catering and events management by silvia sanchez. Tapas catering University College Birmingham. Birmingham, England, United Kingdom.

R. S SHETTY - Business Management - Trading - Marketing

linkedin.com
https://uk.linkedin.com › r-s-shetty-287812110
R. S SHETTY. Founder & CEO - R S VENTURES. www.rsexims.com , www.wildcity.co.uk ,www.libertyshoesonline.com MBA-UK (Masters in business administration )- ...

Peter Worsfold (peterworsfold@gmail.com) - Owner

linkedin.com
https://uk.linkedin.com › peter-worsfold-peterworsfold-g...
Inverness, Scotland, United Kingdom · Owner · drummond marketing
Owner, drummond marketing \experienced online, Social Media marketer. drummond marketing not available. Inverness, Scotland, United Kingdom. 1K followers 500+ ...

Rick Hignett - Owner/Director & Seller - Canei Trading Ltd.

linkedin.com
https://uk.linkedin.com › rickhignett
Owner at Canei Trading Ltd. Canei Trading Ltd. Stowe School, Buckingham. Worcester City, England, United Kingdom. 951 followers 500+ connections. See your ...

Mark Burgess - iceberg-digital.co.uk

linkedin.com
https://uk.linkedin.com › mark-burgess-ba905419
My Name is Mark Burgess and I am the CEO at Iceberg Digital. I am the author of two… | Learn more about Mark Burgess's work experience, education, ...

London Times Official - Business Owner

linkedin.com
https://uk.linkedin.com › ...
London, England, United Kingdom · Business Owner · London Times Official
Brand Marketing; Content Marketing; Email Marketing; Lead Generation; Event Marketing. Work location: London, England, United Kingdom. Work preference: In ...

Stephen Doran - Hook, England, United Kingdom

linkedin.com
https://uk.linkedin.com › stephendoran
Advisor, mentor and C level contributor. CEO with a Masters in Executive Coaching; Non-exec Director, Estonia e-resident A passion for start ups, ...

Chris Saynor - Co-Owner - Bethnal&Bec

linkedin.com
https://uk.linkedin.com › chrissaynor
... Marketing Innovator * Consultant / Board Member / Fractional Executive / Conference Speaker. Bethnal&Bec The University of Hull. London, England, United Kingdom.

Ben Sillitoe - Founder and editor - Green Retail World

linkedin.com
https://uk.linkedin.com › ben-sillitoe-34962318
Previously, I was founding editor of Essential Retail, an online magazine for the retail solutions industry. In association with the UK and Europe's leading ...

Tony Watson(LION)tonyvwatson@gmail.com

linkedin.com
https://uk.linkedin.com › tonyvwatson
Greater Bristol Area, United Kingdom · Business Owner · Home business entrepreneur
Ex Air Force Pilot Airport Operations Director in UK, Hong Kong and Australia MD Airport Management Consultancy Non-Executive Hospital Director Real Estate ...

Paul A. - Managing Director - Aztec capital Advisers

linkedin.com
https://uk.linkedin.com › ...
We work with property developers in the UK. Off market sites for experienced developers. We work closely with our overseas buyers predominantly within prime ...

Linda Hitman - City of Durham, England, United Kingdom

linkedin.com
https://uk.linkedin.com › ...
As Founder and CEO of Exclusive Business, I have had a varied career path that has covered a wide cross section of businesses. Effective business networking ...

Tim Wakefield - United Kingdom | Professional Profile

linkedin.com
https://uk.linkedin.com › timothywakefield
... gmail.com, + ... Managing Director, Market Intelligence. Euromoney Institutional Investor. Oct 2020 - Aug 2022 1 year 11 months. London, England, United Kingdom.

Sedge Beswick - Founder - SEEN Connects

linkedin.com
https://uk.linkedin.com › sedge-beswick
London, England, United Kingdom · Founder · SEEN Connects
Before founding my own business, I worked in-house for household brands; Red Bull, Three UK and ASOS where I was their first “social” hire and built a team of ...

Leandro Godinho - Founder - NSS National Services and ...

linkedin.com
https://uk.linkedin.com › leandro-godinho
Brookvale, England, United Kingdom · Founder · NSS National Services and Supplies
Founder and CEO at NSS National Services and Supplies. NSS National Services and Supplies LDS Business College. Brookvale, England, United Kingdom. 657 ...

Giuseppe Paolelli - CEO & Co-Founder - Optimand

linkedin.com
https://uk.linkedin.com › giuseppepaolelli
London Area, United Kingdom · CEO & Co-Founder · Optimand
Cluster Revenue Manager. HotelRevenue.co.uk. Nov 2013 - Nov 2017 4 years 1 month. London, ...

Jenny Milne - Owner of Sad Film Club - Self-employed

linkedin.com
https://uk.linkedin.com › jenny-milne-
Aberdeen, Scotland, United Kingdom · Owner of Sad Film Club · Self-employed
Jenny Milne. Creative Marketing Specialist and Visual Artist. Self-employed Robert Gordon University. Aberdeen, Scotland, United Kingdom.

Tyler Johnson - Business Owner - Boomslang Media

linkedin.com
https://uk.linkedin.com › ...
Tyler Johnson. Owner of Boomslang Media - Social Media Marketing Agency. Boomslang Media. United Kingdom. 441 followers 420 ...

Daniel Singer - London, England, United Kingdom

linkedin.com
https://uk.linkedin.com › daniel-singer-18555623
I help companies optimise their digital strategy and online marketing by providing data driven insight and research. In particular I provide commercial and ...

Vivek Thadhani - Founder - CommuniTea

linkedin.com
https://uk.linkedin.com › vivekthadhani
Vivek Thadhani. Vivek Thadhani Real Estate - Property Consultant and Owner at Keller Williams Realty, Inc. CommuniTea Keele University UK ...

Jason Kwamie - Executive Director - Xposd Group Ltd(XGL)

linkedin.com
https://uk.linkedin.com › jason-kwamie-08282524
London, England, United Kingdom · Executive Director · Xposd Group Ltd(XGL)
BUSINESS. Xposd Group Ltd(XGL) National Institute of Information Technology. London, England, United Kingdom ... jasonkwamie@gmail.com | jason@xposdgroup.co.uk ...

Manuel Díaz - Co-Founder - SUK Sports

linkedin.com
https://uk.linkedin.com › manueldiazmorales
Currently Founder and Managing Director of Events & Hospitality company in the UK, besides Co-Founder of Sports Marketing Consultancy. Previous Business ...

Kristie Prada - Founder - DUE PRADA

linkedin.com
https://uk.linkedin.com › dueprada
Helping businesses achieve their goals with Digital Marketing | Facebook | Pinterest | Instagram | LinkedIn | Email. DUE PRADA. London, England, United Kingdom.

Belinda Youngs - Univeristy of Newcastle Upon Tyne

linkedin.com
https://uk.linkedin.com › ...
Belinda Youngs. CEO. COOPLAND & SON (SCARBOROUGH) LIMITED University of London. Leeds, England, United Kingdom.

Chloe Pepa - Co-founder/Customer Service Manager

linkedin.com
https://uk.linkedin.com › ...
Crawley, England, United Kingdom · Co-founder/Customer Service Manager · Pepa's Building Solutions Ltd.
Co-founder at Pepa's Building Solutions Ltd. Pepa's Building Solutions Ltd. Pearson College. Crawley, England, United Kingdom. 420 followers 423 connections.

Haydn Elliott - Managing Director of CSG Owned Studios ...

linkedin.com
https://uk.linkedin.com › haydnelliott
Co-Founder. The Trailblazers Club. May 2017 - Present 6 years 8 months. London, United Kingdom.

Paul Clarke - Business Owner - Improve4u

linkedin.com
https://uk.linkedin.com › ...
Sandhurst, England, United Kingdom · Business Owner · Improve4u
... gmail.com Thanks for reading my profile | Learn more about Paul ... Director @ Improve4U. Improve4u Kingston University. Sandhurst, England, United Kingdom.

Paulina Day - Head of Marketing and Communications

linkedin.com
https://uk.linkedin.com › paulina-day
London, England, United Kingdom · Head of Marketing and Communications · BUILA
... gmail.com | Learn more about Paulina Day's work experience ... Managing Director, Marketing & Communications Consultant. BUILA. London, England, United Kingdom.

Emma Rees - Warrington, England, United Kingdom

linkedin.com
https://uk.linkedin.com › emma-rees-90956097
I am a qualified beauty therapist,nail technician and special effects make up artist. Career of working with horses for 12 years which was fun and a ...

Tommy Prendergast - Marketing Manager - Dainty & Heaps

linkedin.com
https://uk.linkedin.com › dyintolive-tommy
Vape FINDR & London Vape Show. Aug 2014 - Apr 2018 3 years 9 months. West Midlands, UK. Owner/ ...

Ian Gunner - Creative Director - STAY STRONG INTL LTD

linkedin.com
https://uk.linkedin.com › ian-gunner-26845768
Ware, England, United Kingdom · Creative Director · STAY STRONG INTL LTD
Creative Director · Creative Director · Creative Director / Managing Director · Creative Director · Editor in Chief & Brand Manager - Ride UK BMX magazine, ...

Justin Finch - General Manager at Free Courses UK

linkedin.com
https://uk.linkedin.com › finchjustin
Birmingham, England, United Kingdom · General Manager at Free Courses UK · Free Courses UK
Co-founder of www.safer-jobs.com. Former Chairman of the English Subbuteo Association. Key Skills: • Sales Management • Team Leadership • Communication • Online ...

Andrew McGuinness - Ellipsis Entertainment Ltd (Layered ...

linkedin.com
https://uk.linkedin.com › ...
United Kingdom · Ellipsis Entertainment Ltd (Layered Reality™)
London, England, United Kingdom. Company ghost image Graphic. -. Company ghost ... Founder & Owner at The Boundary. Southend-on-Sea · Connect · Lucia Rimini.

Courey Peart 🌐 - Company Owner - WEB47: Ecom Agency

linkedin.com
https://uk.linkedin.com › ...
London, England, United Kingdom · Company Owner · WEB47: Ecom Agency
London, England, United Kingdom. 51 followers 50 connections. See your mutual ... Barry Sinatra. Growth Marketer - Marketing Strategist - Web Agency Owner.

Isaac Ofereh-Mugbeh - Business & Company Owner ...

linkedin.com
https://uk.linkedin.com › ...
Business & Company Owner Foundation's Founder Overseer International Worldwide Glob. Self-employed. Jan 1994 - Present 30 years. London, England, United Kingdom.

Rosie Baulcombe - BLUE TURACO COFFEE

linkedin.com
https://uk.linkedin.com › ...
Sales And Marketing Strategist. RB Consulting. Apr 2021 - Present 2 years 10 months. London, England, United Kingdom.

Abdullah Ahmed - Digital Marketing Consultant - Weblinerz ...

linkedin.com
https://uk.linkedin.com › ...
... gmail.com | Learn more about Abdullah Ahmed's work experience, education ... CEO and Founder of Invesign. Blackburn · Connect · Jacob Day. CEO of Guppy Fish ...

Shahzad Saleem - SEO Expert In Blog Post at SAA ...

linkedin.com
https://uk.linkedin.com › ...
SEO Expert In Blog Post at SAA Marketing UK SEO Management. SAA Marketing Oxford Brookes University. Consett, England, United Kingdom ... Founder & CEO of Fragers ...

Janna Bastow - ProdPad

linkedin.com
https://uk.linkedin.com › jannabastow
Brighton, England, United Kingdom · ProdPad
I'm a product manager, taking the forms of a startup founder and CEO, consultant, and ... Janna Bastow. ProdPad. Brighton, England, United Kingdom. 20K followers ...
Missing: @gmail. ‎| Show results with: @gmail.

MICHAEL UTTLEY - Chief Executive Officer - Self-employed

linkedin.com
https://uk.linkedin.com › michael-uttley
... gmail.com | Learn more about MICHAEL UTTLEY's work experience ... Chief Executive Officer. Self-employed Rossall School. Harrogate, England, United Kingdom.

Lois Parmenter - Business Owner - six ounces

linkedin.com
https://nz.linkedin.com › loisparmenter
Christchurch, Canterbury, New Zealand · Business Owner · six ounces
Please DM or email me at lois.parmenter.uk@gmail.com. Articles by Lois ... Metropolitan Pub Company. Jul 2017 - Apr 2019 1 year 10 months. London, United Kingdom.

Jeff Cremer - CEO - jeffsmusicology@gmail.com

linkedin.com
https://www.linkedin.com › ...
Dublin, Georgia, United States · CEO · jeffsmusicology@gmail.com
Co owner, Executive Chef, Customer relations. The Peppercorn Restaurant. May 1990 - 2009 19 years. 110 West Jackson St. Dublin GA ...

Ignacio Llado - Blank Street

linkedin.com
https://www.linkedin.com › ignacio-llado
United States · Blank Street
London, England, United Kingdom. Company ghost image ... Founder of Hoyalist, StartUp Hoyas, Head of Asia Desk at Zeeba Student Run ...

Engr Sharif Dewan - Chief Executive Officer - EngrSEO

linkedin.com
https://bd.linkedin.com › engrsharifdewan
I was also working at Sh Service BD, Tech ICS UK Based Software Company as a Sr. SEO Executive and digital marketing manager. With more than 3 years' experience ...

Colin Dingelstad - CEO and Founder

linkedin.com
https://www.linkedin.com › colin-dingelstad
Austin, Texas, United States · CEO and Founder · Beyond Social Conditioning
Colin Dingelstad, the CEO/Founder, started Beyond SocialConditioning to provide an organic digital marketing solution for starting, small or medium-sized ...

Margarita Khartanovich - Platform6 Startup House

linkedin.com
https://fi.linkedin.com › khartanovich
Tampere, Pirkanmaa, Finland · Platform6 Startup House
London, England, United Kingdom. Company ghost image Graphic. -. Tampere ... Head of Sales & Deal Flow, Deputy Managing Director. Helsinki · Connect · Ossi ...

Dylan Mapura - Gloucester, England, United Kingdom
linkedin.com
https://uk.linkedin.com › ...
Dylan Mapura. Owner of Mapura Marketing Services. Gloucester, England, United Kingdom. 1 follower 1 connection. See your mutual connections ...

Gemma Young - Entrepreneur First

linkedin.com
https://uk.linkedin.com › gemmayoung
London, England, United Kingdom · Entrepreneur First
Gemma Young. Entrepreneur First. London, England, United Kingdom. 4K followers ... founder and CEO!” Show less. Click here to view Eddy Ankrett's profile. Eddy ...
Missing: @gmail. ‎| Show results with: @gmail.

Juliet Roland - Business Owner - Juliette

linkedin.com
https://ng.linkedin.com › ...
England, United Kingdom · Business Owner · Juliette
Email: okohjuliet6@gmail.com | Learn more about Juliet Roland's work ... Juliet. Juliette. England, United Kingdom. 12 followers 11 connections. See your ...

John Casson - Video Editor - LinkedVideo.net

linkedin.com
https://th.linkedin.com › johnrcasson
สิงห์บุรี, ประเทศไทย · Video Editor · LinkedVideo.net
... Founder & CEO, Revenue Accelerators, New York “He is an excellent ... Commercial Union. ส.ค. 1970 - ก.พ. 1975 4 ปี 7 เดือน. Newcastle upon Tyne, United Kingdom.

Jonay Brito - Business&Marketing Administrator

linkedin.com
https://si.linkedin.com › jonaybritogarcia
Ljubljana, Slovenia · Business&Marketing Administrator · Jungle Odyssey
Business&Marketing ☛ CEO & Co-Founder of Jungle Odyssey ✓ ✉ jbritok88@gmail.com ... Aug 2020 - Present 3 years 5 months. Edinburgh, Scotland, United Kingdom.

Manana Samuseva Ph.D (Babylon Voice)

linkedin.com
https://www.linkedin.com › mananasamuseva
New York, New York, United States · Babylon Voice
London, England, United Kingdom. Company ghost image Graphic. -. New York, United States. Company ghost image Graphic. -. Greater New York City Area. Company ...

Pratik Gauri - 5ireChain

linkedin.com
https://ae.linkedin.com › pratikgauri
دبي الإمارات العربية المتحدة · 5ireChain
As the Founder & CEO of 5ire.org ( pronounced FIRE ) which recently became a ... London, United Kingdom. رسم بياني صورة مؤقتة للشركة. -. Shenzhen, Guangdong ...

James Lawrence - MIGLASA ENTERPRISE

linkedin.com
https://gh.linkedin.com › james-lawrence-a32156266
Chief Executive Officer (CEO) & Founder of Miglasa Enterprise. MIGLASA ... United Kingdom · James Lawrence. Murrieta, CA · James Lawrence. Lindon, UT · James ...

Raman Sehgal - ramarketing

linkedin.com
https://ca.linkedin.com › ramansehgalus
Having founded ramarketing in 2009, I have grown the business (headquartered in the UK's… | Learn more about Raman Sehgal's work experience, education, ...
Missing: @gmail. ‎| Show results with: @gmail.
More results
Kenya
Thika - Based on your past activity
 - Update location
More options in Quick settings ()"""

emailList = []

def extract_emails(text):
    # Define the regular expression pattern for extracting email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to find all matches in the text
    emails = re.findall(email_pattern, text)

    return emails


def removingDuplicates():
    extracted_emails = extract_emails(text_sample)

    for email in extracted_emails:
        emailList.append(email)

    originalEmailList = emailList

    uniqueEmailList = []
    for item in originalEmailList:
        if item not in uniqueEmailList:
            uniqueEmailList.append(item)

    return uniqueEmailList

emailDataList = removingDuplicates()

print("Extracted: ",print(emailDataList)," emails")

def save_emails_to_csv(emails, file_path):
    # Ensure that the file path has a .csv extension
    if not file_path.endswith('.csv'):
        file_path += '.csv'

    # Read existing emails from the CSV file, if it exists
    existing_emails = set()
    try:
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                existing_emails.add(row['Emails'])
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist yet

    # Filter out duplicates and append new emails
    new_emails = [email for email in emails if email not in existing_emails]

    # Append new emails to the CSV file
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # If the file is empty, write the header
        if not existing_emails:
            csv_writer.writerow(['Emails'])

        # Write the new emails to the CSV file
        csv_writer.writerows([[email] for email in new_emails])

    print(f"New emails saved to {file_path}")




def is_email_in_csv(email, file_path):
    # Ensure that the file path has a .csv extension
    if not file_path.endswith('.csv'):
        file_path += '.csv'

    try:
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                if email.lower() == row['Emails'].lower():
                    return True
    except FileNotFoundError:
        return False  # File not found, email is not present

    return False  # Email not found in the file



def sendEmail(email):
    email_sender = 'briantaylor5830@gmail.com'
    email_password = 'kylzflzecnpvkfix'
    email_receiver = email

    subject = 'Exploring Opportunities for Software Development Collaboration'
    
    body = """
Dear Sir/Madam,

I hope this email finds you well. My name is Brian Taylor, and I am writing to introduce myself as a skilled software developer with expertise in Python, automation, WordPress, and machine learning.
With a passion for crafting efficient and innovative solutions, I have successfully contributed to a variety of projects, ranging from automating repetitive tasks to developing custom WordPress websites and implementing machine learning algorithms. My diverse skill set allows me to tackle challenges from different angles and deliver high-quality results.

My Skills:
Python Development: I am proficient in developing scalable and maintainable Python applications for diverse purposes, including web development, data analysis, and automation.
Automation: I am experienced in creating automated workflows to streamline business processes, reduce manual effort, and enhance overall efficiency.
Data Scraping: I am also proficient in extracting valuable data from various sources, providing clients with actionable insights for marketing and strategic decision-making.
WordPress Development: I am skilled in designing and implementing custom WordPress solutions tailored to meet clients' unique requirements, ensuring a seamless online presence.
Machine Learning: I am well knowledgeable in the field of machine learning. I have successfully implemented predictive models and data-driven solutions, empowering businesses to make informed decisions.
I am currently exploring new opportunities for collaboration and am interested in discussing how my skills and experiences align with your business needs. Whether you have a specific project in mind or wish to explore potential areas of improvement, I am confident in my ability to contribute positively to your team.
If you are available, I would love the opportunity to further discuss how my expertise can bring value to your projects.

Thank you for considering my application. I look forward to the possibility of working together and contributing to the success of your endeavors.

Best regards,
Brian Taylor,
Software Developer.
"""
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


for email in emailDataList:    
    # Example usage:
    email_to_check = email

    # Replace 'path/to/your/file' with the actual file path and name
    csv_file_path = 'Emails.csv'

    if is_email_in_csv(email_to_check, csv_file_path):
        print("Already sent a message to this email")
    else:
        try:
            sendEmail(email)
            print("Email sent to: ", email) 
        except:
            print("Couldn't send an email to: ", email)
    
# Example usage:
email_list = emailDataList

# Replace 'path/to/your/file' with the desired file path and name
csv_file_path = 'Emails.csv'

save_emails_to_csv(email_list, csv_file_path)