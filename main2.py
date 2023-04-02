import pandas as pd
import os
import glob
import warnings
warnings.filterwarnings('ignore')

os.makedirs('Results', exist_ok=True)
result_directory = os.getcwd()+'/'+'Results'
os.chdir('files')

jobtitles = ['Chief Academic Officer', 'Chief Accounting Officer', 'Chief Administrative Officer', 'Chief Analytics Officer', 'Chief Architect Officer', 'Chief Audit Executive', 'Chief Brand Officer', 'Chief Business Development Officer', 'Chief Business Officer', 'Chief Commercial Officer', 'Chief Communications Officer', 'Chief Compliance Officer', 'Chief Content Officer', 'Chief Creative Officer', 'Chief Customer Officer', 'Chief Data Officer', 'Chief Design Officer', 'Chief Development Officer', 'Chief Digital Officer', 'Chief Diversity Officer', 'Chief Engineer', 'Chief Executive Officer', 'Chief Experience Officer', 'Chief Financial Officer', 'Chief Human Resources Officer', 'Chief Information Officer', 'Chief Information Security Officer', 'Chief Innovation Officer', 'Chief Investment Officer', 'Chief Learning Officer', 'Chief Legal Officer', 'Chief Marketing Officer', 'Chief Medical Officer', 'Chief Nursing Officer', 'Chief Operating Officer', 'Chief People Officer', 'Chief Privacy Officer', 'Chief Procurement Officer', 'Chief Product Officer', 'Chief Quality Officer', 'Chief Research Officer', 'Chief Revenue Officer', 'Chief Risk Officer', 'Chief Robot Whisperer', 'Chief Sales Officer', 'Chief Science Officer', 'Chief Security Officer', 'Chief Strategy Officer', 'Chief Technology Officer', 'Executive Vice President', 'Senior Vice President', 'Vice President', 'Vice President Business', 'Vice President Finance', 'Vice President Human Resources', 'Vice President Marketing', 'Vice President of Accounting', 'Vice President of Administration', 'Vice President of Audit', 'Vice President Of Business Development', 'Vice President of Communications', 'Vice President of Compliance', 'Vice President of Design', 'Vice President Of Development', 'Vice President of Engineering', 'Vice President of Facilities', 'Vice President of Finance', 'Vice President of Human Resources', 'Vice President of Information Technology', 'Vice President of Maintenance', 'Vice President of Manufacturing', 'Vice President of Marketing', 'Vice President of Media', 'Vice President of Operation', 'Vice President of Operations', 'Vice President of Product', 'Vice President of Purchasing', 'Vice President of Quality', 'Vice President of Research And Development', 'Vice President of Risk', 'Vice President of Safety', 'Vice President of Sales', 'Vice President of Sales and Marketing', 'Vice President of Security', 'Vice President Of Services', 'Vice President of Software', 'Vice President of Technical', 'Vice President of Training', 'Vice President Operations', 'Vice President Sales Marketing', 'Zone Vice President', 'Assistant to Vice President', 'Assistant Vice President', 'Accounting Director', 'Administration Director', 'Audit Director', 'Board of Directors', 'Brand Director', 'Business Development Director', 'Communication Director', 'Communications Director', 'Compliance Director', 'Controlling Director', 'Cruise Director', 'Customer Experience Director', 'Design Director', 'Director', 'Director General', 'Director of Bean Counting', 'Director Of Business Development', 'Director of Ethical Hacking', 'Director of First Impressions', 'Director Of Information Technology', 'Director of Inside Sales', 'Director of Maintenance', 'Director Of Operations', 'Director of Photography', 'Director Of Quality', 'Director Of Services', 'Director of Storytelling', 'Director Of Youth Ministry', 'Director Sales and Marketing', 'Engineering Director', 'Executive Director', 'Facilities Director', 'Finance Director', 'Financial Director', 'Human Resources Director', 'Information Technology Director', 'Maintenance Director', 'Managing Director', 'Manufacturing Director', 'Marketing Director', 'Media Director', 'Motion Picture Director', 'Non Executive Director', 'Operation Director', 'Operations Director', 'Payroll Director', 'Product Director', 'Project Director', 'Property Director', 'Public Relation Director', 'Purchasing Director', 'Quality Director', 'Research And Development Director', 'Risk Director', 'Safety Director', 'Sales Director', 'Security Director', 'Sourcing Director', 'Technical Director', 'Training Director', 'Youth Director', 'Zone Director', 'Account Manager', 'Accounting Manager', 'Administration Manager', 'Administrative Manager', 'Animal Shelter Manager', 'Area Sales Manager', 'Assistant General Manager', 'Assistant Manager', 'Audit Manager', 'Benefits Manager', 'Branch Manager', 'Brand Manager', 'Business Development Manager', 'Business Manager', 'Business Unit Manager', 'Category Manager', 'Communication Manager', 'Compliance Manager', 'Construction Manager', 'Content Marketing Manager', 'Controlling Manager', 'Culture Operations Manager', 'Customer Experience Manager', 'Customer Service Manager', 'Design Manager', 'Digital Marketing Manager', 'District Manager', 'E-Commerce Manager', 'Engineering Manager', 'Events Manager', 'Facilities Manager', 'Finance Manager', 'Front Desk Manager', 'General Manager', 'General Sales Manager', 'Hotel Manager', 'Human Resources Manager', 'Information Technology Manager', 'IT Manager', 'Junior Manager', 'Junior Project Manager', 'Key Account Manager', 'Key Account Sales Manager', 'Kitchen Manager', 'Knowledge Manager', 'Lodging Manager', 'Logistics Manager', 'Maintenance Manager', 'Manager', 'Manufacturing Manager', 'Market Development Manager', 'Marketing Communications Manager', 'Marketing Manager', 'Media Manager', 'National Account Manager', 'National Key Account Manager', 'National Sales Manager', 'Network Manager', 'Nursing Manager', 'Office Manager', 'Operation Manager', 'Operations Manager', 'Outside Sales Manager', 'Payroll Manager', 'Portfolio Manager', 'Procurement Manager', 'Product Manager', 'Production Manager', 'Program Manager', 'Project Manager', 'Property Manager', 'Public Relation Manager', 'Purchasing Manager', 'Quality Assurance Manager', 'Quality Manager', 'Recruiting Manager', 'Regional Manager', 'Regional Sales Manager', 'Relationship Manager', 'Research And Development Manager', 'Restaurant Manager', 'Risk Manager', 'Safety Manager', 'Sales and Marketing Manager', 'Sales Manager', 'Salon Manager', 'Security Manager', 'Senior Key Account Manager', 'Senior Manager', 'Senior Project Manager', 'SEO Manager', 'Sourcing Manager', 'Spa Manager', 'Store Manager', 'Supply Chain Manager', 'Technical Manager', 'Territory Manager', 'Training Manager', 'Underwriting Manager', 'Unit Manager', 'Wait Staff Manager', 'Warehouse Manager', 'Yield Manager', 'Zonal Business Manager', 'Zonal Manager', 'Zonal Sales Manager', 'Zone Manager', 'Zone Operations Manager', 'Zone Sales Manager', 'Account Assistant', 'Account Executive', 'Account Representative', 'Account Specialist', 'Accountant', 'Accounting Analyst', 'Accounting Staff', 'Actor', 'Administration Executive', 'Administrative Analyst', 'Administrative Assistant', 'Administrative Officer', 'Administrative Specialist', 'Administrator', 'Advisor', 'Analyst', 'Anesthesiologist', 'Application Developer', 'Architect', 'Artificial Intelligence Engineer', 'Artist', 'Assistant', 'Assistant Engineer', 'Assistant Human Resources', 'Assistant Professor', 'Associate', 'Attorney', 'Audit Executive', 'Auditing Clerk', 'Auditor', 'Banker', 'Biological Engineer', 'Biologist', 'Biomedical Equipment Technician', 'Biostatistician', 'Board Member', 'Bookkeeper', 'Boss', 'Brand Representative', 'Brand Specialist', 'Brand Strategist', 'Broker', 'Business Analyst', 'Business Consultant', 'Business Development Executive', 'Business Development Specialist', 'Business Specialist', 'Buyer', 'Call Center Representative', 'Cardiologist', 'Care Specialist', 'Carpenter', 'Cashier', 'Certified Nursing Assistant', 'Certified Specialist', 'Chairman', 'Chairperson', 'Chef', 'Chemical Engineer', 'Civil Engineer', 'Clerk', 'Client Service Specialist', 'Client Services Representative', 'Cloud Architect', 'Co-Founder', 'Co-Owner', 'Coach', 'Columnist', 'Commercial Loan Officer', 'Commercial Specialist', 'Communications Executive', 'Communications Specialist', 'Community Specialist', 'Compliance Executive', 'Computer Programmer', 'Computer Scientist', 'Consultant', 'Content Creator', 'Content Strategist', 'Content Writer', 'Contract Specialist', 'Contractor', 'Controller', 'Coordinator', 'Coordinator Of Volunteers', 'Copy Editor', 'Copywriter', 'Corporate Specialist', 'Cosmetologist', 'Counselor', 'Courier', 'Customer Care Associate', 'Customer Service', 'Customer Service Representative', 'Customer Service Specialist', 'Customer Specialist', 'Customer Support', 'Customer Support Representative', 'Data Analyst', 'Data Entry', 'Data Specialist', 'Dentists', 'Dermatologist', 'Design Engineer', 'Design Specialist', 'Designer', 'Developer', 'Development Specialist', 'DevOps Engineer', 'Diagnostic Radiologist', 'Digital Specialist', 'Doctor', 'eCommerce Marketing Specialist', 'Economist', 'Editor', 'Education Professional', 'Electrical Engineer', 'Electrician', 'Engineer', 'Engineer Intern', 'Engineering Executive', 'Engineering Specialist', 'Engineering Technician', 'English Teacher', 'Entertainment Specialist', 'Entrepreneur', 'Event Planner', 'Event Specialist', 'Executive', 'Executive Assistant', 'Facilitator', 'Facilities Specialist', 'Family Specialist', 'Field Engineer', 'Field Service Specialist', 'Field Specialist', 'Film Producer', 'Finance Executive', 'Finance Specialist', 'Financial Advisor', 'Financial Analyst', 'Financial Assistant', 'Financial Controller', 'Financial Planner', 'Financial Services Representative', 'Founder', 'Freelance', 'Freelance Graphic Designer', 'Freelance Journalist', 'Freelance Writer', 'Front Desk Associate', 'Front Desk Staff', 'Front-Line Employees', 'Gastroenterologist', 'General', 'General Assistant', 'Geological Engineer', 'Geologist', 'Ghostwriter', 'Graphic Design Specialist', 'Graphic Designer', 'Graphic Web Designer', 'Group Lead', 'Group Sales', 'Guest Services Specialist', 'Guidance Counselor', 'Guide', 'Gynecologist', 'Head', 'Head Of Department', 'Head Of Marketing', 'Head Of Operations', 'Head Of Quality Assurance', 'Head Of Sales', 'Head Of Unit', 'Healthcare Specialist', 'Help Desk', 'Help Desk Specialist', 'Homemaker', 'Host', 'Housekeeper', 'Human Resources', 'Human Resources Administrator', 'Human Resources Assistant', 'Human Resources Business Partner', 'Human Resources Consultant', 'Human Resources Coordinator', 'Human Resources Executive', 'Human Resources Generalist', 'Human Resources Intern', 'Human Resources Officer', 'Human Resources Specialist', 'HVAC Technician', 'Independent Consultant', 'Industrial Specialist', 'Industry Specialist', 'Information Security Analyst', 'Information Specialist', 'Information Technology Analyst', 'Information Technology Consultant', 'Information Technology Executive', 'Information Technology Specialist', 'Information Technology Support Specialist', 'Inspector', 'Installer', 'Instructor', 'Integration Specialist', 'Intensive Care Nurse', 'Interior Designer', 'Intern', 'Internal Medicine', 'International Specialist', 'Investment Specialist', 'Iron Worker', 'IT Professional', 'Java Software Engineer', 'Java Specialist', 'Journalist', 'Junior Account', 'Junior Accountant', 'Junior Analyst', 'Junior Architect', 'Junior Assistant', 'Junior Consultant', 'Junior Designer', 'Junior Engineer', 'Junior Executive', 'Junior Researcher', 'Junior Software Engineer', 'Keeper', 'Key Account', 'Key Account Executive', 'Key Account Sales Specialist', 'Knowledge Specialist', 'Laboratory Assistant', 'Laboratory Specialist', 'Laboratory Technician', 'Laborer', 'Landscaping Assistant', 'Landscaping Worker', 'Language Specialist', 'Law Clerk', 'Law Specialist', 'Lawyer', 'Lead', 'Learning Specialist', 'Lecturer', 'Legal Assistant', 'Legal Intern', 'Legal Secretary', 'Legal Specialist', 'Librarian', 'Library Assistant', 'Life Coach', 'Lifeguard', 'Loan Officer', 'Logistics Specialist', 'Machinery Operator', 'Maintenance Engineer', 'Makeup Artist', 'Management', 'Management Consultant', 'Management Intern', 'Managing Member', 'Managing Partner', 'Manufacturing Assembler', 'Market Researcher', 'Marketing Assistant', 'Marketing Consultant', 'Marketing Executive', 'Marketing Intern', 'Marketing Research Analyst', 'Marketing Specialist', 'Marketing Staff', 'Massage Therapy', 'Mathematician', 'Mechanical Engineer', 'Media Buyer', 'Media Relations Coordinator', 'Medical Administrator', 'Medical Doctor', 'Medical Laboratory Tech', 'Medical Researcher', 'Meeting Planner', 'Member', 'Mental Health Counselor', 'Mentor', 'Merchandising Associate', 'Mining Engineer', 'Mortgage Loan Processor', 'Mover', 'Music Producer', 'Musician', 'National Account Specialist', 'National Key Account', 'National Sales Specialist', 'Navy', 'Nephrologist', 'Network Administrator', 'Network Engineer', 'Network Specialist', 'Network Technician', 'Networking Specialist', 'Neurologist', 'Neurosurgeon', 'News Specialist', 'Nuclear Engineer', 'Nurse', 'Nurse Practitioner', 'Nurse Practitioners', 'Nursing Specialist', 'Nutrition', 'Nutrition Specialist', 'Occupational Medicine', 'Office Administrator', 'Office Assistant', 'Office Associate', 'Office Clerk', 'Office Volunteer', 'Officer', 'Online Specialist', 'Operation Executive', 'Operational Specialist', 'Operations Analyst', 'Operations Assistant', 'Operations Coordinator', 'Operations Professional', 'Operations Specialist', 'Operations Supervisor', 'Operator', 'Optometry', 'Orderly', 'Organizer', 'Overseer', 'Owner', 'Painter', 'Paralegal', 'Partner', 'Pathologist', 'Payroll Clerk', 'Personal Assistant', 'Personal Trainer', 'Petroleum Engineer', 'Pharmacist', 'Pharmacy Assistant', 'Phone Sales Specialist', 'Photographer', 'Physical Therapist', 'Physical Therapy Assistant', 'Physician', 'Physicist', 'Planning Specialist', 'Plant Engineer', 'Plastic Surgeon', 'Playwright', 'Plumber', 'Podiatrist', 'Police Officer', 'Political Scientist', 'Porter', 'Postdoctoral Researcher', 'Preschool Teacher', 'President', 'Principal', 'Producer', 'Product Executive', 'Product Specialist', 'Production Engineer', 'Production Specialist', 'Professional', 'Professional Singer', 'Professor', 'Program Administrator', 'Program Coordinator', 'Program Specialist', 'Project Engineer', 'Project Lead', 'Project Specialist', 'Proposal Writer', 'Proprietor', 'Psychologist', 'Public Relations', 'Public Relations Specialist', 'Purchasing Staff', 'Quality Analyst', 'Quality Assurance Analyst', 'Quality Assurance Engineer', 'Quality Assurance Lead', 'Quality Assurance Officer', 'Quality Assurance Specialist', 'Quality Assurance Supervisor', 'Quality Assurance Tester', 'Quality Control', 'Quality Control Analyst', 'Quality Control Coordinator', 'Quality Control Engineer', 'Quality Control Inspector', 'Quality Control Lead', 'Quality Coordinator', 'Quality Engineer', 'Quality Inspector', 'Quality Management Specialist', 'Quality Specialist', 'Quantity Surveyor', 'Radiology Nurse', 'Real Estate Agent', 'Real Estate Broker', 'Realtor', 'Receivable Clerk', 'Receptionist', 'Recruiter', 'Recruitment Specialist', 'Recyclables Collector', 'Red Cross Volunteer', 'Registered Nurse', 'Reiki Practitioner', 'Representative', 'Research And Development Specialist', 'Research Assistant', 'Research Intern', 'Researcher', 'Reservationist', 'Resource Specialist', 'Retail Specialist', 'Retail Worker', 'Rheumatologist', 'Risk Executive', 'Roofer', 'Safety Engineer', 'Sales Analyst', 'Sales And Marketing Specialist', 'Sales Assistant', 'Sales Associate', 'Sales Consultant', 'Sales Engineer', 'Sales Executive', 'Sales Representative', 'Sales Specialist', 'Salesperson', 'School Counselor', 'School Volunteer', 'Screenwriter', 'Scrum Master', 'Secretary', 'Security Executive', 'Security Guard', 'Security Officer', 'Security Professional', 'Self Employed', 'Senior Business Analyst', 'Senior Consultant', 'Senior Engineer', 'Senior Financial Analyst', 'Senior Graphic Designer', 'Senior Java Software Engineer', 'Senior Network Engineer', 'Senior Quality Assurance Engineer', 'Senior Quality Assurance Specialist', 'Senior Quality Specialist', 'Senior Software Engineer', 'Senior Underwriter', 'Senior User Experience Designer', 'Server', 'Service Dog Trainer', 'Shareholders', 'Skin Care Specialist', 'Social Media Assistant', 'Social Media Specialist', 'Social Worker', 'Sociologist', 'Software Developer', 'Software Engineer', 'Software Executive', 'Software Ninjaneer', 'Software Quality Assurance Engineer', 'Solar Photovoltaic Installer', 'Sound Engineer', 'Specialist', 'Speech Pathologist', 'Speechwriter', 'Sports Volunteer', 'SQL Developer', 'Staff Writer', 'Student', 'Superintendent', 'Supervisor', 'Supervisors', 'Support Specialist', 'Surgeon', 'System Engineer', 'System Specialist', 'Teacher', 'Teaching Assistant', 'Teaching Specialist', 'Team Lead', 'Team Leader', 'Team Specialist', 'Technical Consultant', 'Technical Executive', 'Technical Lead', 'Technical Specialist', 'Technical Support Specialist', 'Technical Writer', 'Technician', 'Technology Specialist', 'Telemarketer', 'Telephone Operator', 'Test Scorer', 'Therapist', 'Title Analyst', 'Title Researcher', 'Tour Guide', 'Tow Truck Operator', 'Trainee', 'Training Executive', 'Training Specialist', 'Translator', 'Travel Agent', 'Travel Nurse', 'Travel Writer', 'Tutor', 'Undergraduate', 'Undergraduate Research Assistant', 'Undergraduate Research Fellow', 'Undergraduate Student', 'Underwriter', 'Underwriting Assistant', 'Unit Secretary', 'University Lecturer', 'University Student', 'Urologist', 'User Experience Design Specialist', 'User Experience Designer', 'User Interface Designer', 'Utilities Specialist', 'UX Designer & UI Developer', 'Veterinarian', 'Veterinary Assistant', 'Vice Chair', 'Vice Chairman', 'Video Editor', 'Video Game Writer', 'Video Producer', 'Videographer', 'Virtual Assistant', 'Visiting Researcher', 'Visual Merchandiser', 'Volunteer', 'Waiter', 'Waitress', 'Warehouse Associate', 'Warehouse Specialist', 'Warehouse Supervisor', 'Warehouse Worker', 'Web Design Specialist', 'Web Designer', 'Web Developer', 'Web Specialist', 'Webmaster', 'Wedding Coordinator', 'Welder', 'Welding', 'Well Driller', 'Wellness Specialist', 'Worker', 'Writer', 'Writer', 'Writing Specialist', 'Yoga Instructor', 'Youth Advisor', 'Youth Advocate', 'Youth Care Worker', 'Youth Coordinator', 'Youth Counselor', 'Youth Development Specialist', 'Youth Lead', 'Youth Minister', 'Youth Pastor', 'Youth Program Coordinator', 'Youth Specialist', 'Youth Volunteer', 'Youth Worker', 'Zonal Head', 'Zone Sales Lead', 'Zoning Administrator', 'Zoologist', 'Addiction Counselor', 'Animal Breeder', 'Animal Control Officer', 'Animal Shelter Board Member', 'Animal Shelter Volunteer', 'Animal Shelter Worker', 'Animal Trainer', 'Medical Transcriptionist', 'Chief', 'Business Development', 'E-Commerce', 'ECommerce', 'Finance', 'Sales', 'Information Technology', 'Information ', 'Technology', 'Marketing', 'Doctor', 'Operation', 'Portfolio', 'Product', 'Program', 'Property', 'Quality', 'Agent', 'Broker', 'Safety', 'Security', 'Software', 'Project', 'SEO', 'Developer', 'Engineer', 'Technical', 'UX Designer', 'UI Developer', 'User Experience', 'Accounting', 'Audit', 'Administration', 'Communications', 'Compliance', 'Design', 'Development', 'Engineering', 'Facilities', 'Maintenance', 'Manufacturing', 'Operations', 'Purchasing', 'Risk', 'Safety', 'Sales and Marketing', 'Training']

columns_list= ['Gender','Full_Name', 'First_Name', 'Last_Name', 'Job_Title','Job_Title_Levels', 'Email_0', 'Email_0_Type','Email_1', 'Email_1_Type','Phone_0', 
 'Phone_1','linkedin_url', 'Industry',  'Location_Locality', 'Location_Metro',
 'Location_Region', 'Location_Country', 'Location_Continent','Job_Company_Name', 'Job_Company_Website', 
 'Job_Company_Size', 'Job_Company_Founded', 'Job_Company_Industry','job_company_linkedin_url',
       'Job_Company_Location_Street_Address','Job_Company_Location_Address_Line_2',
       'Job_Company_Location_Locality', 'Job_Company_Location_Metro',
       'Job_Company_Location_Region','Job_Company_Location_Postal_Code','Job_Company_Location_Country','Job_Company_Location_Continent']

def organize_df(df,columns_list):
    df = df[columns_list]
    df.columns = ['Gender','Full Name', 'First Name', 'Last Name', 'Job Title','Job Title Levels', 'Email Address 1', 'Email Address Type 1','Email Address 2', 'Email Address Type 2','Phone Number', 
 'Mobile Number','Linkedin URL', 'Industry',  'Person City', 'Person Metro',
 'Person States', 'Person Country', 'Person Continent','Company Name', 'Company Website', 
 'Company Size', 'Company Founded', 'Company Industry','Company Linkedin URL','Company Street Address','Company Address Line 2','Company City','Company Metro','Company State','Company Post Code','Company Country','Company Continent']
    return df

def chunk_df(df, chunk_size=100000):
    num_chunks = len(df) // chunk_size + 1
    for i in range(num_chunks):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        yield df.iloc[start:end]

def divide_states(df,title):

    df = df[df['Person States'].notna()]
    df['Person States'] = df['Person States'].str.replace('/','-')
    states = df['Person States'].unique()
    os.makedirs(result_directory+'/'+title, exist_ok=True)
    os.makedirs(result_directory+'/'+title+'/All States',exist_ok=True)
    for state in states:    
        new_df = df[df['Person States']==state]
        
        if len(new_df) > 100000:
            chunk_size = 100000
            df_list = list(chunk_df(new_df, chunk_size))
            for i, df_chunk in enumerate(df_list):
                df_chunk.to_csv(result_directory+'/'+title+'/All States/'+str(state)+f'_{i}.csv', index=False)
        elif len(new_df)<200:
            pass
        else:
            new_df.to_csv(result_directory+'/'+title+'/All States/'+str(state)+'.csv',index=False)       

def divide_Industry(df,title):
    df = df[df['Industry'].notna()]
    df['Industry'] = df['Industry'].str.replace('/','-')
    industries = df['Industry'].unique()
    
    os.makedirs(result_directory+'/'+title, exist_ok=True)
    os.makedirs(result_directory+'/'+title+'/All Industries',exist_ok=True)
    for industry in industries:
        new_df = df[df['Industry']==industry]
        if len(new_df) > 100000:
            chunk_size = 100000
            df_list = list(chunk_df(new_df, chunk_size))
            for i, df_chunk in enumerate(df_list):
                df_chunk.to_csv(result_directory+'/'+title+'/All Industries/'+str(industry)+f'_{i}.csv', index=False)
        else:
            new_df.to_csv(result_directory+'/'+title+'/All Industries/'+str(industry)+'.csv',index=False)             

def divide_countries(df,title):

    df = df[df['Person Country'].notna()]
    df['Person Country'] = df['Person Country'].str.replace('/','-')
    countries = df['Person Country'].unique()
    os.makedirs(result_directory+'/'+title, exist_ok=True)
    os.makedirs(result_directory+'/'+title+'/All Countries',exist_ok=True)
    for country in countries:    
        new_df = df[df['Person Country']==country]
        if len(new_df) > 100000:
            chunk_size = 100000
            df_list = list(chunk_df(new_df, chunk_size))
            for i, df_chunk in enumerate(df_list):
                df_chunk.to_csv(result_directory+'/'+title+'/All Countries/'+str(country)+f'_{i}.csv', index=False)
        else:
            new_df.to_csv(result_directory+'/'+title+'/All Countries/'+str(country)+'.csv',index=False)    

def divide_cities(df,title):

    df = df[df['Person City'].notna()]
    df['Person City'] = df['Person City'].str.replace('/','-')
    cities = df['Person City'].unique()
    os.makedirs(result_directory+'/'+title, exist_ok=True)
    os.makedirs(result_directory+'/'+title+'/All Cities',exist_ok=True)
    for city in cities:
        
        new_df = df[df['Person City']==city]
        if len(new_df) > 100000:
            chunk_size = 100000
            df_list = list(chunk_df(new_df, chunk_size))
            for i, df_chunk in enumerate(df_list):
                df_chunk.to_csv(result_directory+'/'+title+'/All Cities/'+str(city)+f'_{i}.csv', index=False)
        elif len(new_df)<200:
            pass
        else:
            new_df.to_csv(result_directory+'/'+title+'/All Cities/'+str(city)+'.csv',index=False)       

def divide_company_size(df,title):

    df = df[df['Company Size'].notna()]
    company_ranges = df['Company Size'].unique()
    os.makedirs(result_directory+'/'+title, exist_ok=True)
    os.makedirs(result_directory+'/'+title+'/Employee Range',exist_ok=True)
    for comp_range in company_ranges:
        new_df = df[df['Company Size']==comp_range]
        if len(new_df) > 100000:
            chunk_size = 100000
            df_list = list(chunk_df(new_df, chunk_size))
            for i, df_chunk in enumerate(df_list):
                df_chunk.to_csv(result_directory+'/'+title+'/Employee Range/'+str(comp_range)+f'_{i}.csv', index=False)
        else:
            new_df.to_csv(result_directory+'/'+title+'/Employee Range/'+str(comp_range)+'.csv',index=False)        
  
def divide_email_types(df,title):
    df = df[df['Email Address 1'].notna()]
    df = df.fillna('')
    df['Email Address Type 1'] = df['Email Address Type 1'].fillna('')    
    email_types = df['Email Address Type 1'].unique()
    os.makedirs(result_directory+'/'+title, exist_ok=True)
    os.makedirs(result_directory+'/'+title+'/Email Type',exist_ok=True)
    for email_type in email_types:
        new_df = df[df['Email Address Type 1']==email_type]
        
        
        if len(new_df) > 100000:
            chunk_size = 100000
            df_list = list(chunk_df(new_df, chunk_size))
            for i, df_chunk in enumerate(df_list):
                df_chunk.to_csv(result_directory+'/'+title+'/Email Type/'+str(email_type)+f'_{i}.csv', index=False)
        else:
            new_df.to_csv(result_directory+'/'+title+'/Email Type/'+str(email_type)+'.csv',index=False)

def divide_phones(df,title):

    df1 = df[df['Phone Number'].notna()]
    df2 = df[df['Phone Number'].isna()]
    


    os.makedirs(result_directory+'/'+title, exist_ok=True)
    os.makedirs(result_directory+'/'+title+'/Phone',exist_ok=True)
    if len(df1)>100000:
        chunk_size = 100000
        df_list1 = list(chunk_df(df1, chunk_size))
        df_list2 = list(chunk_df(df2, chunk_size))
        for i, df_chunk in enumerate(df_list1):
            df_chunk.to_csv(result_directory+'/'+title+'/Phone/'+str("phone")+f'_{i}.csv', index=False)
        for i, df_chunk in enumerate(df_list2):
            df_chunk.to_csv(result_directory+'/'+title+'/Phone/'+str("no_phone")+f'_{i}.csv', index=False)        

    else :

        df1.to_csv(result_directory+'/'+title+'/Phone/'+str("phone")+'.csv',index=False)
        df2.to_csv(result_directory+'/'+title+'/Phone/'+str("no_phone")+'.csv',index=False)
        

def filter_titles(job_titles,title_startindex=None,title_endindex=None):
    """ title_startindex and title_endindex are used if you want to use the script for limited titles"""
    if title_startindex is not None and title_endindex is not None:

        job_titles=job_titles[title_startindex:title_endindex]
    i=0   
    for title in job_titles:
        i+=1
        try:
            csv_files = glob.glob(title+'_*.{}'.format('csv'))
            df_append = pd.DataFrame()
            #append all files together
            for file in csv_files:
                        df_temp = pd.read_csv(file,engine="python",error_bad_lines=False,encoding='utf-8')
                        df_append = df_append.append(df_temp, ignore_index=True)
            try:
                df_append = organize_df(df_append,columns_list)
            except:
                pass

            print('\n',"Total Progress ",int((i/len(job_titles))*100),'%' )

            
            divide_states(df_append,title)

            print('\n',title,"  Progress 10%" ) 

            divide_Industry(df_append,title)

            print('\n',title,"  Progress 25%" ) 
            
            divide_countries(df_append,title)

            print('\n',title,"  Progress 40%" ) 

            divide_cities(df_append,title)

            print('\n',title,"  Progress 60%" ) 
           
            divide_company_size(df_append,title)

            print('\n',title,"  Progress 80%" ) 

            divide_email_types(df_append,title)

            print('\n',title,"  Progress 95%" ) 

            divide_phones(df_append,title)
            
            
        except Exception as e:
            print('\n',title, ' :is not exist in files directory')
            print("ERROR : "+str(e))
 

filter_titles(jobtitles)
k=input("press close to exit") 