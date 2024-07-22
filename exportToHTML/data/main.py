import csv

with open('paydata.csv', mode='w') as csv_file:
    fieldnames = ['Occupation', 'Male Median Salary', 'Female Median Salary', 'Amount More Men Earn', 'Percent More Men Earn']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Occupation": "Cashiers", "Male Median Salary": "$31,460", "Female Median Salary": "$30,160", "Amount More Men Earn": "$1,300", "Percent More Men Earn": "4%"})
    writer.writerow({"Occupation": "Maids and housekeeping cleaners", "Male Median Salary": "$32,136", "Female Median Salary": "$30,472", "Amount More Men Earn": "$1,664", "Percent More Men Earn": "5%"})
    writer.writerow({"Occupation": "Nursing assistants", "Male Median Salary": "$37,024", "Female Median Salary": "$35,100", "Amount More Men Earn": "$1,924", "Percent More Men Earn": "5%"})
    writer.writerow({"Occupation": "Bartenders", "Male Median Salary": "$37,492", "Female Median Salary": "$36,400", "Amount More Men Earn": "$1,092", "Percent More Men Earn": "3%"})
    writer.writerow({"Occupation": "Security guards and gambling surveillance officers", "Male Median Salary": "$38,376", "Female Median Salary": "$78,052", "Amount More Men Earn": "$2,028", "Percent More Men Earn": "6%"})
    writer.writerow({"Occupation": "Office clerks, general", "Male Median Salary": "$41,808", "Female Median Salary": "$36,348", "Amount More Men Earn": "$1,768", "Percent More Men Earn": "4%"})
    writer.writerow({"Occupation": "Social workers, all other", "Male Median Salary": "$61,464", "Female Median Salary": "$40,040", "Amount More Men Earn": "$3,224", "Percent More Men Earn": "6%"})
    writer.writerow({"Occupation": "Special education teachers", "Male Median Salary": "$64,844", "Female Median Salary": "$58,240", "Amount More Men Earn": "$1,976", "Percent More Men Earn": "3%"})
    writer.writerow({"Occupation": "Other life, physical, and social science technicians", "Male Median Salary": "$64,948", "Female Median Salary": "$62,868", "Amount More Men Earn": "$1,144", "Percent More Men Earn": "2%"})
    writer.writerow({"Occupation": "Physical therapists", "Male Median Salary": "$79,664", "Female Median Salary": "$63,804", "Amount More Men Earn": "$1,612", "Percent More Men Earn": "2%"})

with open('largest.csv', mode='w') as csv_file:
    fieldnames = ['Occupation', 'Male Median Salary', 'Female Median Salary', 'Amount More Men Earn', 'Percent More Men Earn']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Occupation": "Real estate brokers and sales agents", "Male Median Salary": "$79,872", "Female Median Salary": "$49,920", "Amount More Men Earn": "$29,952", "Percent More Men Earn": "60%"})
    writer.writerow({"Occupation": "Personal financial advisors", "Male Median Salary": "$103,220", "Female Median Salary": "$65,208", "Amount More Men Earn": "$38,012", "Percent More Men Earn": "58%"})
    writer.writerow({"Occupation": "Insurance sales agents", "Male Median Salary": "$71,604", "Female Median Salary": "$46,332", "Amount More Men Earn": "$25,272", "Percent More Men Earn": "55%"})
    writer.writerow({"Occupation": "Sales managers", "Male Median Salary": "$109,408", "Female Median Salary": "$33,748", "Amount More Men Earn": "$34,840", "Percent More Men Earn": "47%"})
    writer.writerow({"Occupation": "Bus drivers, school", "Male Median Salary": "$49,244", "Female Median Salary": "$40,716", "Amount More Men Earn": "$15,496", "Percent More Men Earn": "46%"})
    writer.writerow({"Occupation": "Sales and related occupations", "Male Median Salary": "$59,228", "Female Median Salary": "$76,336", "Amount More Men Earn": "$18,512", "Percent More Men Earn": "45%"})
    writer.writerow({"Occupation": "Financial managers", "Male Median Salary": "$110,032", "Female Median Salary": "$37,388", "Amount More Men Earn": "$33,696", "Percent More Men Earn": "44%"})
    writer.writerow({"Occupation": "Inspectors, testers, sorters, samplers, and weighers", "Male Median Salary": "$53,716", "Female Median Salary": "$34,424", "Amount More Men Earn": "$16,328", "Percent More Men Earn": "44%"})
    writer.writerow({"Occupation": "Recreation workers", "Male Median Salary": "$48,360", "Female Median Salary": "$39,832", "Amount More Men Earn": "$13,936", "Percent More Men Earn": "40%"})
    writer.writerow({"Occupation": "Insurance claims and policy processing clerks", "Male Median Salary": "$53,872", "Female Median Salary": "$39,832", "Amount More Men Earn": "$14,040", "Percent More Men Earn": "35%"})

with open('industrysmall.csv', mode='w') as csv_file:
    fieldnames = ['Occupation', 'Male Median Salary', 'Female Median Salary', 'Amount More Men Earn',
                  'Percent More Men Earn']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Occupation": "Life, physical, and social science occupations", "Male Median Salary": "$80,028", "Female Median Salary": "$73,268", "Amount More Men Earn": "$6,760",
                     "Percent More Men Earn": "9%"})
    writer.writerow({"Occupation": "Community and social service occupations", "Male Median Salary": "$62,348", "Female Median Salary": "$56,836", "Amount More Men Earn": "$5,512",
                     "Percent More Men Earn": "10%"})
    writer.writerow({"Occupation": "Architecture and engineering occupations", "Male Median Salary": "$91,052", "Female Median Salary": "$82,836", "Amount More Men Earn": "$8,216",
                     "Percent More Men Earn": "10%"})
    writer.writerow({"Occupation": "Food preparation and serving related occupations", "Male Median Salary": "$34,476", "Female Median Salary": "$31,096", "Amount More Men Earn": "$3,380",
                     "Percent More Men Earn": "11%"})
    writer.writerow({"Occupation": "Office and administrative support occupations", "Male Median Salary": "$48,516", "Female Median Salary": "$42,536", "Amount More Men Earn": "$5,980",
                     "Percent More Men Earn": "14%"})


with open('industrylarge.csv', mode='w') as csv_file:
    fieldnames = ['Occupation', 'Male Median Salary', 'Female Median Salary', 'Amount More Men Earn',
                  'Percent More Men Earn']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Occupation": "Legal occupations", "Male Median Salary": "$119,444", "Female Median Salary": "$75,140", "Amount More Men Earn": "$44,304",
                     "Percent More Men Earn": "59%"})
    writer.writerow({"Occupation": "Natural resources, construction, and maintenance occupations", "Male Median Salary": "$50,908", "Female Median Salary": "$36,400", "Amount More Men Earn": "$14,508",
                     "Percent More Men Earn": "40%"})
    writer.writerow({"Occupation": "Management, professional, and related occupations", "Male Median Salary": "$89,752", "Female Median Salary": "$66,768", "Amount More Men Earn": "$22,984",
                     "Percent More Men Earn": "34%"})
    writer.writerow({"Occupation": "Professional and related occupations", "Male Median Salary": "$85,644", "Female Median Salary": "$63,908", "Amount More Men Earn": "$21,736",
                     "Percent More Men Earn": "34%"})
    writer.writerow({"Occupation": "Protective service occupations", "Male Median Salary": "$57,512", "Female Median Salary": "$43,420", "Amount More Men Earn": "$14,092",
                     "Percent More Men Earn": "32%"})


with open('state.csv', mode='w') as csv_file:
    fieldnames = ['State', 'Male Median Annual Earnings', 'Female Median Annual Earnings', 'Difference' ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"State": "Wyoming", "Male Median Annual Earnings": "$59,853", "Female Median Annual Earnings": "$40,976", "Difference": "-$18,877"})
    writer.writerow(
        {"State": "New Hampshire", "Male Median Annual Earnings": "$68,566", "Female Median Annual Earnings": "$51,880", "Difference": "-$16,686"})
    writer.writerow(
        {"State": "Utah", "Male Median Annual Earnings": "$61,269", "Female Median Annual Earnings": "$44,707", "Difference": "-$16,686"})
    writer.writerow(
        {"State": "Washington", "Male Median Annual Earnings": "$74,068", "Female Median Annual Earnings": "$57,567", "Difference": "-$16,501"})
    writer.writerow(
        {"State": "District of Columbia", "Male Median Annual Earnings": "$103,222", "Female Median Annual Earnings": "$87,244", "Difference": "-$15,978"})
    writer.writerow(
        {"State": "Louisiana", "Male Median Annual Earnings": "$55,078", "Female Median Annual Earnings": "$40,136", "Difference": "-$14,942"})
    writer.writerow(
        {"State": "Montana", "Male Median Annual Earnings": "$55,496", "Female Median Annual Earnings": "$41,725", "Difference": "-$13,771"})
    writer.writerow(
        {"State": "New Jersey", "Male Median Annual Earnings": "$75,297", "Female Median Annual Earnings": "$61,802", "Difference": "-$13,495"})
    writer.writerow(
        {"State": "Michigan", "Male Median Annual Earnings": "$60,293", "Female Median Annual Earnings": "$46,914", "Difference": "-$13,379"})
    writer.writerow(
        {"State": "Alabama", "Male Median Annual Earnings": "$52,177", "Female Median Annual Earnings": "$39,338", "Difference": "-$12,839"})
    writer.writerow(
        {"State": "Illinois", "Male Median Annual Earnings": "$63,819", "Female Median Annual Earnings": "$51,131", "Difference": "-$12,688"})
    writer.writerow(
        {"State": "Virginia", "Male Median Annual Earnings": "$66,014", "Female Median Annual Earnings": "$53,414", "Difference": "-$12,600"})
    writer.writerow(
        {"State": "Connecticut", "Male Median Annual Earnings": "$73,022", "Female Median Annual Earnings": "$60,672", "Difference": "-$12,350"})
    writer.writerow(
        {"State": "Nebraska", "Male Median Annual Earnings": "$56,121", "Female Median Annual Earnings": "$44,037", "Difference": "-$12,084"})
    writer.writerow(
        {"State": "West Virginia", "Male Median Annual Earnings": "$51,981", "Female Median Annual Earnings": "$39,897", "Difference": "-$12,084"})





