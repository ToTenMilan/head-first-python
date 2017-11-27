# import file_processor
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def open_results(athlete_name):
    try:
        with open(athlete_name + '.txt') as file:
            data = file.readline()
        return(data.strip().split(','))
    except IOError as err:
        print('File is missing: ' + str(err))
        return(None)
        
def show_results(results):
    print(sorted(set([sanitize(t) for t in results]))[0:3])
    
show_results(open_results('james'))
show_results(open_results('julie'))
show_results(open_results('mikey'))
show_results(open_results('sarah'))


# with open('julie.txt') as juf:
#     data = juf.readline()
# julie = data.strip().split(',')
# with open('mikey.txt') as mif:
#     data = mif.readline()
# mikey = data.strip().split(',')
# with open('sarah.txt') as saf:
#     data = saf.readline()
# sarah = data.strip().split(',')

# # jas = []
# # for item in james:
# #     # item = sanitize(item)
# #     jas.append(sanitize(item))

# jas = [sanitize(item) for item in james]

# # ```Ruby james.each(&:sanitize)
    
# # jus = []
# # for item in julie:
# #     # item = sanitize(item)
# #     jus.append(sanitize(item))

# jus = [sanitize(item) for item in julie]
    
# # mis = []
# # for item in mikey:
# #     # item = sanitize(item)
# #     mis.append(sanitize(item))
    
# mis = [sanitize(item) for item in mikey]
    
# # sas = []
# # for item in sarah:
# #     # item = sanitize(item)
# #     sas.append(sanitize(item))
    
# sas = [sanitize(item) for item in sarah]
    
# # james = sorted([sanitize(t) for t in james])
# # unique_james = []
# # for item in james:
# #     if item not in unique_james:
# #         unique_james.append(item)
# # print(unique_james[0:3])
# print(sorted(set([sanitize(t) for t in james]))[0:3])

# # julie = sorted([sanitize(t) for t in julie])
# # unique_julie = []
# # for item in julie:
# #     if item not in unique_julie:
# #         unique_julie.append(item)
# # print(unique_julie[0:3])
# print(sorted(set([sanitize(t) for t in julie]))[0:3])

# # mikey = sorted([sanitize(t) for t in mikey])
# # unique_mikey = []
# # for item in mikey:
# #     if item not in unique_mikey:
# #         unique_mikey.append(item)
# # print(unique_mikey[0:3])
# print(sorted(set([sanitize(t) for t in mikey]))[0:3])

# # sarah = sorted(set([sanitize(t) for t in sarah]))
# # unique_sarah = []
# # for item in sarah:
# #     if item not in unique_sarah:
# #         unique_sarah.append(item)
# # print(unique_sarah[0:3])
# print(sorted(set([sanitize(t) for t in sarah]))[0:3])


        
    
# print(sorted(jas[0:3]))
# print(sorted(jus[0:3]))
# print(sorted(mis[0:3]))
# print(sorted(sas[0:3]))
    






# julia = []
# mikey = []
# sarah = []

# # try:
# #     james_data = open('james.txt')
# #     julia_data = open('julia.txt')
# #     mikey_data = open('mikey.txt')
# #     sarah_data = open('sarah.txt')
# # except:
# #     pass

# file_processor.process_file('james.txt')
# file_processor.process_file('julia.txt')
# file_processor.process_file('mikey.txt')
# file_processor.process_file('sarah.txt')