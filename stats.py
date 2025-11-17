def count_words(contents):
    num_words = contents.split()
    print(f"Found {len(num_words)} total words")
    pass

def count_chars(contents):
    contents = contents.lower()
    my_dict = {}
    alpha = "abcdefghijklmnopqrstuvwxyzôëêâæ"
    for char in contents:
        if char in alpha:
            try:
                if my_dict[char]:
                    my_dict[char] += 1
            except:
                    my_dict[char] = 1
    return my_dict

def sort_on(items):
     return items["num"]

def sorting_function(word_dict):
    # Takes a dictionary returns list of dictionaries
    d1 = {"char":None, "num":None}
    #d1 = {}
    output = []
    for key in word_dict:
        #d1.update({key, word_dict[key]})
        d1["char"] = key
        d1["num"] = word_dict[key]
        #output.append({d1["char"]:d1["num"]})
        output.append({"char":key, "num":word_dict[key]})
    #print(d1)
    output.sort(reverse=True, key=sort_on)
    for item,val in enumerate(output):
        if output[item]["char"] == " ": pass
        else:
            print(f"{output[item]["char"]}: {output[item]["num"]}")

    pass
    

    
    
    
