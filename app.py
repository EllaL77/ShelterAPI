import math

from flask import Flask, render_template, jsonify, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# route to handle the search submission (GPT)
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if query:
        # Redirect to the corresponding endpoint
        return redirect(url_for('search_results', search_query=query))
    return redirect(url_for('home'))

# calculate distance between coordinates (GPT)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# portland zip codes and coordinates
portland_coord = {'97201': ('45.50742', '-122.68984'),
 '97202': ('45.48031', '-122.64512'),
 '97203': ('45.61112', '-122.74134'),
 '97204': ('45.51815', '-122.67415'),
 '97205': ('45.51548', '-122.69877'),
 '97206': ('45.47993', '-122.60057'),
 '97207': ('45.52390', '-122.67510'),
 '97208': ('45.52390', '-122.67510'),
 '97209': ('45.53346', '-122.68150'),
 '97210': ('45.55154', '-122.73514'),
 '97211': ('45.57732', '-122.64162'),
 '97212': ('45.54417', '-122.64307'),
 '97213': ('45.53779', '-122.60081'),
 '97214': ('45.51394', '-122.64412'),
 '97220': ('45.55191', '-122.55533'),
 '97221': ('45.49829', '-122.72776'),
 '97215': ('45.51396', '-122.59940'),
 '97216': ('45.51342', '-122.55834'),
 '97217': ('45.58959', '-122.69299'),
 '97218': ('45.58088', '-122.60030'),
 '97219': ('45.45102', '-122.69501'),
 '97222': ('45.44218', '-122.61861'),
 '97223': ('45.44686', '-122.79557'),
 '97227': ('45.54028', '-122.67696'),
 '97228': ('45.52390', '-122.67510'),
 '97229': ('45.55438', '-122.81131'),
 '97231': ('45.71214', '-122.84004'),
 '97232': ('45.52964', '-122.64391'),
 '97233': ('45.51376', '-122.49640'),
 '97236': ('45.48263', '-122.50228'),
 '97256': ('45.52390', '-122.67510'),
 '97258': ('45.51310', '-122.67550'),
 '97266': ('45.48170', '-122.55741'),
 '97268': ('45.41660', '-122.63860'),
 '97269': ('45.44650', '-122.63820'),
 '97280': ('45.52390', '-122.67510'),
 '97290': ('45.52390', '-122.67510'),
 '97291': ('45.52510', '-122.80970'),
 '97292': ('45.52390', '-122.67510'),
 '97293': ('45.52390', '-122.67510'),
 '97224': ('45.40530', '-122.79857'),
 '97225': ('45.50052', '-122.77916'),
 '97230': ('45.56244', '-122.50172'),
 '97238': ('45.52390', '-122.67510'),
 '97239': ('45.48798', '-122.69265'),
 '97240': ('45.52390', '-122.67510'),
 '97242': ('45.52390', '-122.67510'),
 '97267': ('45.40178', '-122.61463'),
 '97281': ('45.46670', '-122.74840'),
 '97282': ('45.52390', '-122.67510'),
 '97283': ('45.52390', '-122.67510'),
 '97286': ('45.52390', '-122.67510'),
 '97294': ('45.52390', '-122.67510'),
 '97296': ('45.52390', '-122.67510'),
 '97298': ('45.49170', '-122.77400')}

# acquired shelter list in portland
portland = {
    "0": {"name": "Family Promise of Greater Washington County", "addr": "5625 Southwest Erickson Avenue, Beaverton",
          "web": "https://www.familypromisegwc.org/?utm_source=google&utm_medium=wix_google_business_profile&utm_campaign=17066741240387882471",
          "phone": "(971) 217-8949", "latitude": 45.4789802, "longitude": -122.8124068688},
    "1": {"name": "Family Promise of Beaverton", "addr": "14986 Northwest Cornell Road, Portland",
          "web": "https://www.familypromisegwc.org/", "phone": "(971) 217-8949", "latitude": 45.5712294,
          "longitude": -122.8313623086},
    "2": {"name": "Path Home", "addr": "6220 Southeast 92nd Avenue, Portland", "web": "http://www.path-home.org/",
          "phone": "(503) 915-8306", "latitude": 45.47737905, "longitude": -122.6192527253},
    "3": {"name": "Family Promise of Metro East", "addr": "4837 Northeast Couch Street, Portland",
          "web": "https://www.familypromisemetroeast.org/about-us.html", "phone": "(503) 753-3960",
          "latitude": 45.5241343, "longitude": -122.6132448206},
    "4": {"name": "Good Neighbor Center", "addr": "11130 Southwest Greenburg Road, Tigard",
          "web": "http://gncnw.org/", "phone": "(503) 443-6084", "latitude": 45.43976445,
          "longitude": -122.7727121033},
    "5": {"name": "Transition Projects Laurelwood Center Shelter", "addr": "6130 Southeast Foster Road, Portland",
          "web": "https://www.tprojects.org/contact-us", "phone": "(503) 280-4776", "latitude": 45.4938993,
          "longitude": -122.6052078},
    "6": {"name": "Kenton Women\'s Village (Argyle Village)", "addr": "2250-2344 North Columbia Boulevard, Portland",
          "web": "https://www.catholiccharitiesoregon.org/services/housing-services/kenton-womens-village/",
          "phone": "(503) 231-4866", "latitude": 45.5757174, "longitude": -122.6426704},
    "7": {"name": "Right 2 Dream Too", "addr": "999 North Thunderbird Way, Portland",
          "web": "http://right2dreamtoo.blogspot.com/", "phone": "(503) 382-8838", "latitude": 45.5300756,
          "longitude": -122.668893},
    "8": {"name": "Greater New Hope Family Services", "addr": "11936 Northeast Sandy Boulevard, Portland",
          "web": "http://www.greaternewhopefamilyservices.com/contact-us/", "phone": "(813) 417-4013",
          "latitude": 45.5250561, "longitude": -122.6481242},
    "9": {"name": "Dignity Village", "addr": "9401 Northeast Sunderland Avenue, Portland",
          "web": "https://dignityvillage.org/", "phone": "(503) 281-1604", "latitude": 45.5905967,
          "longitude": -122.6357629},
    "10": {"name": "Rose Haven Day Shelter and Community Center", "addr": "1740 Northwest Glisan Street, Portland",
           "web": "http://www.rosehaven.org/", "phone": "(503) 248-6364", "latitude": 45.52624295,
           "longitude": -122.6890474015}, "11": {"name": "Transition Projects Walnut Park Shelter",
                                                 "addr": "5411 Northeast Martin Luther King Junior Boulevard, Portland",
                                                 "web": "N/A", "phone": "(503) 488-7761", "latitude": 45.55213,
                                                 "longitude": -122.6616242},
    "12": {"name": "Burnside Shelter (Portland Rescue Mission)", "addr": "111 West Burnside Street, Portland",
           "web": "https://portlandrescuemission.org/", "phone": "(503) 906-7690", "latitude": 45.52337975,
           "longitude": -122.671699088},
    "13": {"name": "Community Action Family Shelter", "addr": "210 Southeast 12th Avenue, Hillsboro",
           "web": "https://caowash.org/", "phone": "(503) 640-3263", "latitude": 45.5208577,
           "longitude": -122.969649661},
    "14": {"name": "River District Navigation Center", "addr": "1111 Northwest Naito Parkway, Portland",
           "web": "https://www.tprojects.org/", "phone": "(503) 280-4752", "latitude": 45.5307084,
           "longitude": -122.676937},
    "15": {"name": "Transition Projects Willamette Center Shelter", "addr": "5120 Southeast Milwaukie Avenue, Portland",
           "web": "https://www.tprojects.org/get-assistance/shelters", "phone": "(503) 488-7750",
           "latitude": 45.4857289, "longitude": -122.6493271158},
    "16": {"name": "A Home for Everyone", "addr": "501 Southeast Hawthorne Boulevard #600, Portland", "web": "N/A",
           "phone": "(503) 988-2525", "latitude": 45.5124017, "longitude": -122.5428423},
    "17": {"name": "Family Promise of Tualatin Valley", "addr": "11460 Pacific Highway West, Tigard",
           "web": "https://www.familypromiseoftv.org/", "phone": "(503) 427-2768", "latitude": 45.44146285,
           "longitude": -122.74601155},
    "18": {"name": "Portland Homeless Family Solutions", "addr": "6220 Southeast 92nd Avenue, Portland",
           "web": "http://pdxhfs.org/contact/", "phone": "(503) 915-8306", "latitude": 45.47737905,
           "longitude": -122.6192527253},
    "19": {"name": "Do Good Multnomah", "addr": "7809 Northeast Everett Street, Portland",
           "web": "http://dogoodmultnomah.org/", "phone": "(503) 436-5757", "latitude": 45.5249595,
           "longitude": -122.6708866311}, "20": {"name": "My Father\'s House", "addr": "5003 Powell Boulevard, Gresham",
                                                 "web": "http://www.familyshelter.org/",
                                                 "phone": "(503) 492-3046", "latitude": 45.4927868,
                                                 "longitude": -122.482745725},
    "21": {"name": "Share Orchards Inn", "addr": "5609 Northeast 102nd Avenue, Vancouver",
           "web": "https://sharevancouver.org/programs/share-shelter-system/", "phone": "(360) 604-0907",
           "latitude": 45.66257285, "longitude": -122.56801145},
    "22": {"name": "Open House Ministries Vancouver WA", "addr": "900 West 12th Street, Vancouver",
           "web": "https://www.sheltered.org/", "phone": "(360) 737-0300", "latitude": 45.6305936,
           "longitude": -122.6806633},
    "23": {"name": "Council For the Homeless", "addr": "2306 Northeast Andresen Road, Vancouver",
           "web": "http://www.councilforthehomeless.org/", "phone": "(360) 699-5106", "latitude": 45.6505279,
           "longitude": -122.6019566},
    "24": {"name": "Share Homestead", "addr": "4921 Northeast Hazel Dell Avenue, Vancouver",
           "web": "https://sharevancouver.org/programs/share-shelter-system/", "phone": "(360) 693-8923",
           "latitude": 45.65789975, "longitude": -122.6664860807},
    "25": {"name": "Menlo Park Safe Rest Village", "addr": "12202 East Burnside Street, Portland",
           "web": "https://www.portland.gov/ryan/menlo-park-srv-122nd-and-east-burnside",
           "phone": "(503) 865-6407", "latitude": 45.5226109, "longitude": -122.5665357},
    "26": {"name": "Transition Projects Doreen\'s Place Shelter", "addr": "610 Northwest Broadway, Portland",
           "web": "https://www.tprojects.org/contact-us", "phone": "(503) 280-4664", "latitude": 45.5280781,
           "longitude": -122.6778382}, "27": {"name": "Our Just Future (formerly Human Solutions)",
                                              "addr": "124 Northeast 181st Avenue Suite 109, Portland",
                                              "web": "http://www.humansolutions.org/", "phone": "(503) 405-7875",
                                              "latitude": 45.52329285, "longitude": -122.4767308502},
    "28": {"name": "Blanchet House", "addr": "310 Northwest Glisan Street, Portland",
           "web": "http://blanchethouse.org/", "phone": "(503) 241-4340", "latitude": 45.5263997,
           "longitude": -122.6738412387},
    "29": {"name": "Emergency Shelter Clearing House", "addr": "Vancouver", "web": "N/A", "phone": "(360) 695-9677",
           "latitude": 49.2608724, "longitude": -123.113952},
    "30": {"name": "Share Aspire Program", "addr": "2306 Northeast Andresen Road, Vancouver",
           "web": "http://www.sharevancouver.org/", "phone": "(360) 448-2121", "latitude": 45.6505279,
           "longitude": -122.6019566},
    "31": {"name": "Transition Projects Resource Center", "addr": "650 Northwest Irving Street, Portland",
           "web": "https://www.tprojects.org/resource-center/", "phone": "(503) 280-4700",
           "latitude": 45.5275863, "longitude": -122.6773354},
    "32": {"name": "Reedway Safe Rest Village", "addr": "10550 Southeast Reedway Street, Portland",
           "web": "https://www.portland.gov/safe-rest-villages/locations-safe-rest-villages-and-culturally-specific-villages/reedway-safe-rest",
           "phone": "N/A", "latitude": 45.481045, "longitude": -122.5539968},
    "33": {"name": "Our Just Future", "addr": "10550 Northeast Halsey Street, Portland",
           "web": "http://www.humansolutions.org/", "phone": "(503) 548-0200", "latitude": 45.53321035,
           "longitude": -122.5542951612}}

# Route to handle the search results
@app.route('/results/<search_query>')
def search_results(search_query):
    distances = []
    # finds the 5 closest shelters
    lat = float(portland_coord[search_query][0])
    lon = float(portland_coord[search_query][1])
    for shelter in portland:
        dist = haversine(lat, lon, portland[shelter]["latitude"], portland[shelter]["longitude"])
        distances.append([dist, shelter])
    distances.sort(key=lambda x: x[0])
    return [[f"distance: {round(shelter[0], 2)} km", portland[shelter[1]]] for shelter in distances[:5]]

# route that returns all shelter in portland
@app.route('/pdx', methods=['GET'])
def get_shelters():
    return jsonify(portland)
