#Simon Rosner
#3/18/2016
#States Module

stateInfo = [   #list of (state, abbrev, cap)
        ("Alabama",	"AL",	"Montgomery"),
        ("Alaska",	"AK",	"Juneau"),
        ("Arizona",	"AZ",	"Phoenix"),
        ("Arkansas"     "AR",	"Little Rock"),
        ("California",  "CA",	"Sacramento"),
        ("Colorado",    "CO",	"Denver"),
        ("Connecticut", "CT",	"Hartford"),
        ("Delaware",    "DE",	"Dover"),
        ("Florida",	"FL",	"Tallahassee"),
        ("Georgia",	"GA",	"Atlanta"),
        ("Hawaii",	"HI",	"Honolulu"),
        ("Idaho",	"ID",	"Boise"),
        ("Illinois",    "IL",	"Springfield"),
        ("Indiana",	"IN",	"Indianapolis"),
        ("Iowa",	"IA",	"Des Moines"),
        ("Kansas",	"KS",	"Topeka"),
        ("Kentucky",    "KY",	"Frankfort"),
        ("Louisiana",   "LA",	"Baton Rouge"),
        ("Maine",	"ME",	"Augusta"),
        ("Maryland",    "MD",	"Annapolis"),
        ("Massachusetts","MA",	"Boston"),
        ("Michigan",    "MI",	"Lansing"),
        ("Minnesota",   "MN",	"St. Paul"),
        ("Mississippi", "MS",	"Jackson"),
        ("Missouri",    "MO",	"Jefferson City"),
        ("Montana",	"MT",	"Helena"),
        ("Nebraska",    "NE",	"Lincoln"),
        ("Nevada",	"NV",	"Carson City"),
        ("New Hampshire","NH",	"Concord"),
        ("New Jersey",  "NJ",	"Trenton"),
        ("New Mexico",  "NM",	"Santa Fe"),
        ("New York",    "NY",	"Albany"),
        ("North Carolina","NC",	"Raleigh"),
        ("North Dakota","ND",	"Bismarck"),
        ("Ohio",	"OH",	"Columbus"),
        ("Oklahoma",    "OK",	"Oklahoma City"),
        ("Oregon",	"OR",	"Salem"),
        ("Pennsylvania","PA",	"Harrisburg"),
        ("Rhode Island","RI",	"Providence"),
        ("South Carolina","SC",	"Columbia"),
        ("South Dakota","SD",	"Pierre"),
        ("Tennessee",   "TN",	"Nashville"),
        ("Texas",	"TX",	"Austin"),
        ("Utah",	"UT",	"Salt Lake City"),
        ("Vermont",	"VT",	"Montpelier"),
        ("Virginia",    "VA",	"Richmond"),
        ("Washington",  "WA",	"Olympia"),
        ("West Virginia","WV",	"Charleston"),
        ("Wisconsin",   "WI",	"Madison"),
        ("Wyoming",	"WY",	"Cheyenne")]

def getInfo(index,info): #returns 0Name 1Abbrev 2Cap for given state
    tempList = stateInfo[index]
    return tempList[info]

#All methods below implement the above helper method

def nameToAbbrev(name): #takes name, returns abbreviation
    return getInfo(name,1)

def nameToCap(name): #takes name, returns capital
    return getInfo(name,2)

def abbrevToName(abbrev):    #takes abbreviation, returns name
    return getInfo(abbrev,0)

def abbrevToCap(abbrev): #takes abbreviation, returns capital
    return getInfo(abbrev,2)

def capToName(cap):   #takes capital, returns name
    return getInfo(cap,0)

def capToAbbrev(cap): #takes capital, returns abbreviation
    return getInfo(cap,1)


