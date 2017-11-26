from nester import print_lol
import pickle




man = []
new_man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)   
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('man_data.pickle', 'wb') as man_file:
        # print_lol(man, fh=man_file)
        pickle.dump(man, man_file)
    with open('other_data.pickle', 'wb') as other_file:
        # print_lol(other, fh=other_file)
        pickle.dump(other, other_file)
        
except IOError as err:
    print('File error: ' + str(err))
    
except pickle.PickleError as perr:
    print('Pickling error' + str(perr))
    

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
nester.print_lol(new_man)
    
    
# try:
#     data = open('missing.txt')
#     print(data.readline(), end='')
# except IOError as err:
#     print('File error: ' + str(err))
# finally:
#     if 'data' in locals():
#         data.close()


# try:
#     man_file = open('man_data.txt', 'w')
#     other_file = open('other_data.txt', 'w')
#     print(man, file=man_file)
#     print(other, file=other_file)
# except IOError:
#     print('File Error.')
# finally:
#     man_file.close()
#     other_file.close()

# try:
#     data = open('sketch.txt')
#     for line in data:
#         try:
#             (role, line_spoken) = line.split(':', 1)
#             print(role, end='')
#             print(' said: ', end='')
#             print(line_spoken, end='')
#         except ValueError:
#             pass
#     data.close()
# except IOError:
#     print('The file is missing')