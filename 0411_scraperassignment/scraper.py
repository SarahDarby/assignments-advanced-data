import csv, mechanize
from bs4 import BeautifulSoup


# Get the HTML of the page
br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')


# Put this up here so you can loop over it
option_values = ['001', '003', '005', '007', '009', '011', '013', '015', '017', '019', '021', '023', '025', '027', '029', '031', '033', '035', '037', '039', '041', '043', '045', '047', '049', '051', '053', '055', '057', '059', '061', '063', '065', '067', '069', '071', '073', '075', '077', '079', '081', '083', '085', '087', '089', '091', '093', '095', '097', '099', '101', '095A', '103', '105', '107', '109', '111', '113', '115', '117', '119', '121', '123', '125', '127', '129', '131', '133', '135', '137', '139', '141', '143', '145', '147', '149', '151', '153', '155', '157', '159', '161', '163', '165', '167', '169', '171', '173', '175', '177', '179', '181', '195', '197', '199', '201', '203', '205', '183','185', '187', '189', '510', '188', '207','209', '211', '213', '215', '217', '219', '221', '223', '225', '227', '229']
i = 0

county_names = ['Adair', 'Andrew', 'Atchison', 'Audrain', 'Barry', 'Barton', 'Bates', 'Benton', 'Bollinger', 'Boone', 'Buchanan', 'Butler', 'Caldwell', 'Callaway', 'Camden', 'Cape Girardeau', 'Carroll', 'Carter', 'Cass', 'Cedar', 'Chariton', 'Christian', 'Clark', 'Clay', 'Clinton', 'Cole', 'Cooper', 'Crawford', 'Dade', 'Dallas', 'Daviess', 'De Kalb', 'Dent', 'Douglas', 'Dunklin', 'Franklin', 'Gasconade', 'Gentry', 'Greene', 'Grundy', 'Harrison', 'Henry', 'Hickory', 'Holt', 'Howard', 'Howell', 'Iron', 'Jackson', 'Jasper', 'Jefferson', 'Johnson', 'Kansas City', 'Knox', 'Laclede', 'Lafayette', 'Lawrence', 'Lewis', 'Lincoln', 'Linn', 'Livingston', 'Macon', 'Madison', 'Maries', 'Marion', 'McDonald', 'Mercer', 'Miller', 'Mississippi', 'Moniteau', 'Monroe', 'Montgomery', 'Morgan', 'New Madrid', 'Newton', 'Nodaway', 'Oregon', 'Osage', 'Ozark', 'Pemiscot', 'Perry', 'Pettis', 'Phelps', 'Pike', 'Platte', 'Polk', 'Pulaski', 'Putnam', 'Ralls', 'Randolph', 'Ray', 'Reynolds', 'Ripley', 'Saline', 'Schuyler', 'Scotland', 'Scott', 'Shannon', 'Shelby', 'St. Charles', 'St. Clair', 'St. Francois', 'St. Louis', 'St. Louis City', 'Ste. Genevieve', 'Stoddard', 'Stone', 'Sullivan', 'Taney', 'Texas', 'Vernon', 'Warren', 'Washington', 'Wayne', 'Webster', 'Worth', 'Wright']
i = 0

# loop over counties
for value in option_values: 
    br.select_form(nr=0) 
    br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
    br.form['ctl00$MainContent$cboCounty'] = [option_values[i]]
    [option_values[i]] = [county_names[i]]
    br.submit('ctl00$MainContent$btnCountyChange')

    html = br.response().read() 

    soup = BeautifulSoup(html, "html.parser")

    # Find the main table using both the "align" and "class" attributes
    main_table = soup.find('table',
        {'id': 'MainContent_dgrdResults'}
    )

    # Now get the data from each table row
    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]
        if data:
            if data[0] in ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich','Donald J. Trump']:
                print county_names[i], data[0], data[3]

    i=i+1
    if i == len(option_values):
        break
        


