"""
game built on selecting capital then selected another capital with condition first letter
equal to last letter in former capital 
"""

#writing all capitals of the world and the countries as dictionary 
capital = {'tirane': 'albania', 'algiers': 'algeria', 'andorra la vella': 'andorra', 'luanda': 'angola',
  'saint johns': 'antigua and barbuda', 'buenos aires': 'argentina', 'yerevan': 'armenia',
  'canberra': 'australia', 'vienna': 'austria', 'baku': 'azerbaijan', 'nassau': 'bahamas',
  'manama': 'bahrain', 'dhaka': 'bangladesh', 'bridgetown': 'barbados', 'minsk': 'belarus',
  'brussels': 'belgium', 'belmopan': 'belize', 'porto novo': 'benin', 'thimphu': 'bhutan',
  'la paz': 'bolivia', 'sarajevo': 'bosnia and herzegovina', 'gaborone': 'botswana',
  'brasilia': 'brazil', 'bandar seri begawan': 'brunei', 'sofia': 'bulgaria',
  'ouagadougou': 'burkina faso', 'gitega': 'burundi', 'phnom penh': 'cambodia', 'yaounde': 'cameroon',
  'ottawa': 'canada', 'praia': 'cape verde', 'bangui': 'central african republic', 'ndjamena': 'chad',
  'santiago': 'chile', 'beijing': 'china', 'bogota': 'colombia', 'moroni': 'comoros',
  'kinshasa': 'congo, democratic republic of the', 'brazzaville': 'congo, republic of the',
  'san jose': 'costa rica', 'yamoussoukro': 'côte d ivoire (ivory coast)', 'zagreb': 'croatia',
  'havana': 'cuba', 'nicosia': 'cyprus', 'prague': 'czech republic (czechia)',
  'copenhagen': 'denmark', 'djibouti': 'djibouti', 'roseau': 'dominica',
  'santo domingo': 'dominican republic', 'dili': 'east timor', 'quito': 'ecuador', 'cairo': 'egypt',
  'san salvador': 'el salvador', 'london': 'england', 'malabo': 'equatorial guinea',
  'asmara': 'eritrea', 'tallinn': 'estonia', 'mbabana': 'eswatini (swaziland)',
  'addis ababa': 'ethiopia', 'palikir': 'federated states of micronesia', 'suva': 'fiji',
  'helsinki': 'finland', 'paris': 'france', 'libreville': 'gabon', 'banjul': 'gambia',
  'tbilisi': 'georgia', 'berlin': 'germany', 'accra': 'ghana', 'athens': 'greece',
  'saint georges': 'grenada', 'guatemala': 'guatemala', 'conakry': 'guinea',
  'bissau': 'guinea-bissau', 'georgetown': 'guyana', 'port au prince': 'haiti',
  'tegucigalpa': 'honduras', 'budapest': 'hungary', 'reykjavik': 'iceland', 'new delhi': 'india',
  'jakarta': 'indonesia', 'tehran': 'iran', 'baghdad': 'iraq', 'dublin': 'ireland',
  'jerusalem': 'palastine', 'rome': 'italy', 'kingston': 'jamaica', 'tokyo': 'japan',
  'amman': 'jordan', 'nur sultan': 'kazakhstan', 'nairobi': 'kenya', 'tarawa atoll': 'kiribati',
  'pristina': 'kosovo', 'kuwait': 'kuwait', 'bishkek': 'kyrgyzstan', 'vientiane': 'laos',
  'riga': 'latvia', 'beirut': 'lebanon', 'maseru': 'lesotho', 'monrovia': 'liberia',
  'tripoli': 'libya', 'vaduz': 'liechtenstein', 'vilnius': 'lithuania', 'luxembourg': 'luxembourg',
  'antananarivo': 'madagascar', 'lilongwe': 'malawi', 'kuala lumpur': 'malaysia', 'male': 'maldives',
  'bamako': 'mali', 'valletta': 'malta', 'majuro': 'marshall islands', 'nouakchott': 'mauritania',
  'port louis': 'mauritius', 'mexico': 'mexico', 'chisinau': 'moldova', 'monaco': 'monaco',
  'ulaanbaatar': 'mongolia', 'podgorica': 'montenegro', 'rabat': 'morocco', 'maputo': 'mozambique',
  'nay pyi taw': 'myanmar (burma)', 'windhoek': 'namibia', 'kathmandu': 'nepal',
  'amsterdam': 'netherlands', 'wellington': 'new zealand', 'managua': 'nicaragua', 'niamey': 'niger',
  'abuja': 'nigeria', 'pyongyang': 'north korea', 'skopje': 'north macedonia (macedonia)',
  'belfast': 'northern ireland', 'oslo': 'norway', 'muscat': 'oman', 'islamabad': 'pakistan',
  'melekeok': 'palau', 'panama': 'panama', 'port moresby': 'papua new guinea', 'asuncion': 'paraguay',
  'lima': 'peru', 'manila': 'philippines', 'warsaw': 'poland', 'lisbon': 'portugal', 'doha': 'qatar',
  'bucharest': 'romania', 'moscow': 'russia', 'kigali': 'rwanda',
  'basseterre': 'saint kitts and nevis', 'castries': 'saint lucia',
  'kingstown': 'saint vincent and the grenadines', 'apia': 'samoa', 'san marino': 'san marino',
  'sao tome': 'sao tome and principe', 'riyadh': 'saudi arabia', 'edinburgh': 'scotland',
  'dakar': 'senegal', 'belgrade': 'serbia', 'victoria': 'seychelles', 'freetown': 'sierra leone',
  'singapore': 'singapore', 'bratislava': 'slovakia', 'ljubljana': 'slovenia',
  'honiara': 'solomon islands', 'mogadishu': 'somalia', 'seoul': 'south korea', 'juba': 'south sudan',
  'madrid': 'spain', 'pretoria': 'south africa', 'sri jayawardenapura kotte': 'sri lanka',
  'khartoum': 'sudan', 'paramaribo': 'suriname', 'stockholm': 'sweden', 'bern': 'switzerland',
  'damascus': 'syria', 'taipei': 'taiwan', 'dushanbe': 'tajikistan', 'dodoma': 'tanzania',
  'bangkok': 'thailand', 'lome': 'togo', 'nukualofa': 'tonga', 'tunis': 'tunisia',
  'ankara': 'türkiye (turkey)', 'ashgabat': 'turkmenistan', 'funafuti': 'tuvalu', 'kampala': 'uganda',
  'kyiv': 'ukraine', 'abu dhabi': 'united arab emirates', 'washington': 'united states',
  'montevideo': 'uruguay', 'tashkent': 'uzbekistan', 'port vila': 'vanuatu',
  'vatican': 'vatican city', 'caracas': 'venezuela', 'hanoi': 'vietnam', 'cardiff': 'wales',
  'sanaa': 'yemen', 'lusaka': 'zambia', 'harare': 'zimbabwe'}

# print welcome sentences 
print("========================\n Capital Cities of the World\n========================")

# define initial variable as int to count score for user 
score= 0

#define bool variable to change condition while loop 
x = False 
while not x:
  #entring any capital
  name = input("Please enter any capital in the world: ").lower()

  #writing alert message if the user entering name not capital
  if not name in capital:
    print(f"{name} is not capital")
  else:

    #print country with capital if name is true 
    while name in capital:
      print(f"Correct, {name} is capital of {capital[name]}")
      name_new = name
      #requastion about another country that first letter matches with last letter from the former capital 
      name = input(f"What is the capital in the World start with '{name[-1]}' letter: ")
      score+=1 #increase score of user by one 

    #create variable to select each capital for every time from dictionary (capital)
    for n in capital:

      #if first letter of any capital equal to last letter of former capital, select it and print in message 
      if n[0] == name_new[-1]:
        print(f"Wrong!, {name} is not correct, you can say '{n}' the capital of '{capital[n]}' ")
        print(f"Your score is {score}")#calculate final score 
        x= True #change condition of while
        break #log out from loop 
      
     






