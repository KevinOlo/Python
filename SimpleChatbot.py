import re #regular expression regex
import long_res as long #second file w functionality

def msg_prob(user_msg, recog_wds, sgl_res = False, req_wds = []):

    has_req_wds = True
    msg_cert = 0

    # Counts how many words are present in each predefined message

    for word in user_msg:
        if word in recog_wds:
            msg_cert += 1
    
    
     # Calculates the percent of recognised words in a user message

    percent = (float(msg_cert) / float(len(recog_wds))) * 100
    

    # Checks that the required words are in the string

    for words in req_wds:
        if words not in user_msg: # prevents matching incorrect response to msg
            has_req_wds = False
            break

    # Must either have the required words, or be a single response

    if has_req_wds or sgl_res:
        return int(percent)
    else:
        return 0

    
   

def check_all_msg(msg):
    highest_problist ={} #hash / dict

    # Simplifies response creation / adds it to the dict

    def response( bot_resp, list_of_wds, sgl_res = False, req_wds =[]):
        nonlocal highest_problist
        highest_problist[bot_resp] = msg_prob(msg, list_of_wds, sgl_res, req_wds)
    
   #---------------------------------------------- #responses---------------------------------------------------#
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'wassup', 'heyo'], sgl_res = True)
    response('I\'m doing fine, how about you? ',['how', 'are', 'you', 'doing'], req_wds = ['how'])
    response('Thanks G', ['i', 'love', 'you'], req_wds = ['love', 'you'])
    response(long.yo, ['yo', 'my', 'guy'], req_wds = ['yo'])
    response(long.bball , ['basketball', 'athlete', 'players', 'hoop', 'basket', 'nba'],req_wds=['basketball'] )
    response(long.fball, ['football', 'nfl', 'touchdown', 'athlete', 'player' ], req_wds=['football'])
    response(long.libcar,['library', 'card', 'read', 'book', 'books', 'librarian', 'fun', 'hard'], req_wds=['fun'])
    response(long.pyans,['python', 'snakes', 'coding', 'programming', 'language'], req_wds=['snakes'] or ['coding'])


#LONGER RESPONSE__________-------------------------____________--------------------------------------------------

    response(long.r_advice, ['give', 'advice'], req_wds = ['advice'])
    response(long.r_eat, ['what', 'you', 'eat'], req_wds=['you', 'eat'])

    best_match = max(highest_problist, key = highest_problist.get)
    #print(highest_problist)

    return long.unknown() if highest_problist[best_match] < 1 else best_match




def get_res(user_i):
    spltmsg = re.split(r'\s+ | [,.;-?!]| \s*' , user_i.lower()) 
    response = check_all_msg(spltmsg)
    return response

#test get res fun, infin loop to get responses
while True:

    print('Bot: '+ get_res(input('You: ')))
