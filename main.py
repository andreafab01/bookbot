def count_words(file_contents):    
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    words = file_contents.lower()
    letters_dict = {}

    for letter in words:                
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def list_of_dicts(file_contents):                           
    all_letters_dicts = count_letters(file_contents)        
    new_list_dicts = []                                     

    for key, value in all_letters_dicts.items():            
        if key.isalpha():                                   
           new_list_dicts.append({key: value})              
    return new_list_dicts                                  

def sort_on(each_dict):                                 
    for value in each_dict.values():                    
        return value                                    
    
def main():                                     
    with open("books/frankenstein.txt") as f:   
        file_contents = f.read()               
        words = count_words(file_contents)
        
    sorted_list = list_of_dicts(file_contents)                 
    sorted_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()

    for each_dict_key in sorted_list:               
        for i in each_dict_key.keys():              
            letter = i
            amount = each_dict_key[i]                
            print(f"The {letter} character was found {amount} times")

    print("--- End report ---")

main()