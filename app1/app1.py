from flask import Flask, render_template, json, request
from amazonproduct import API
import os
import pandas as pd
import numpy as np
from recommender import cossimilarity, most_similar_users, recommend

app = Flask(__name__)

############recommender###################
movies_list = pd.read_csv("./static/csv/movies_filtered.csv")
movies_list = list(movies_list['product_productid']) # Read in a list of movies in the data
users = pd.read_csv("./static/csv/users_filtered.csv") # Read in the user table
users = users.fillna("") # Change NaN to ""
users_colnames = list(users) # Get column names


# Create a dictionary with indices as keys and user IDs as values
userids = {}
for i in range(len(users)):
    userids[i] = users['review_userid'][i]


# Create a dictionary:
#     keys are user IDs
#     values are themselves dictionaries
#         for each value-dictionary, keys are movie IDs, values are review scores
# eg. {'A123456789': {'B00000000': 5, 'B000099999': 3}, 'A987654321': {'B00000000': 4}} 
# Access a particular user's dictionary via users_data[userids][0] or users_data['A123456789']

users_data = {}
for user in range(len(users)):
    users_data[userids[user]] = {}    
    star = 1
    for col in range(14, 19):        
        for movie in users[users_colnames[col]][user].split():
            users_data[userids[user]][movie] = star
        star += 1
#print(users_data['A100JCBNALJFAW'])

@app.route("/")
def main():
    return render_template('index.html')

# @app.route('/showNewUser')
# def showNewUser():
#     return render_template('NewUser.html')

@app.route('/Recommend', methods=['POST'])
def Recommend():
    _movie1 = str(request.form['movie1'])
    _movie2 = str(request.form['movie2'])
    _movie3 = str(request.form['movie3'])
    _movie4 = str(request.form['movie4'])
    _movie5 = str(request.form['movie5'])
    _rate1 = int(request.form['rate1'])
    _rate2 = int(request.form['rate2'])
    _rate3 = int(request.form['rate3'])
    _rate3 = int(request.form['rate4'])
    _rate3 = int(request.form['rate5'])

    # keywords to ASIN
    # api = API("AKIAJGEEABW2F4H7ZB4Q", "6+ShIy2suLuPzWOdhEbzA8y4Cd3QDdfzokAbILB1","us","yueyingteng-20")
   
    api = API("AKIAIKFQCWRMAQBAIGDQ","V3URxyjcNbnRgak1CnWSoNqze2OFo2xkzxhYgYbg","us","chenlji-20")


    # print(1)

    ASIN = {}
    print("1.1")
    keywords = [_movie1, _movie2, _movie3, _movie4, _movie5]
    print("1.2")
    for keyword in keywords:
        ASIN[str(keyword)] = []
        results = api.item_search('DVD', Title = str(keyword))
        print("1.3")
        for item in results:
            item =  item.ASIN
            ASIN[str(keyword)].append(str(item))
    
    print(2)

    # ASIN = {}
    # keywords = ['little miss sunshine']
    # ASIN['little miss sunshine'] = ['B000K7VHQE', 'B000MR1V22', 'B001JNNDDI', 'B000JU9OJ4']
    

    # from recommender import create_new_user_data
    # def create_new_user_data(username, keywords, ratings):
    #     print(a)
    #     empty_dict = {}
    #     print(b)
    #     for i in range(len(keywords)):
    #         print(c)
    #     # if there are no ASINs in common between the Amazon API results and our data, do not create an entry
    #         if len(set(ASIN[keywords[i]]) & set(movies_list)) == 0:
    #             print(d)
    #             continue
    #         else:
    #             print(e)
    #         # get the first entry from the intersection of the Amazon API results and the ASINs in our data
    #             empty_dict[list(set(ASIN[keywords[i]]) & set(movies_list))[0]] = ratings[i]
    #     users_data[username] = empty_dict

    print(keywords[0])
    print(ASIN[keywords[0]])
    print(list(ASIN[keywords[0]]))
    print(set(ASIN[str(keywords[0])]))
    print(set(list(ASIN[keywords[0]])))
    #print(set(list(movies_list)))
    #a = [filter(lambda x: x in ASIN[keywords[0]], sublist) for sublist in movies_list]
    #print(a)
    
    def create_new_user_data(username, keywords, ratings, ASIN):
        userids[len(userids)] = 'newuser1'
        print("a")
        empty_dict = {}
        print("b")
        for i in range(len(keywords)):
            print("c")
            a = set(list(ASIN[keywords[i]]))
            print(a)
            b = set(list(movies_list))
            print(b)
            c = list(a & b)
            print(c)
            if len(list(c)) == 0:
                print("d")
                continue
            else:
                #empty_dict[list(c)] = ratings[i]
                empty_dict[c[0]] = ratings[i]
                print("e")
        users_data[username] = empty_dict


    print(3)
    

    create_new_user_data('newuser1', keywords, [_rate1, _rate2, _rate3, _rate2, _rate1], ASIN)
    print(users_data['newuser1'])

    

    testrun = recommend('newuser1', userids, users_data)

    print(testrun)

    movies = {}
    for movie in testrun:
        movies[movie] = []
        #result = api.item_lookup(str(movie))
        for item in api.item_lookup(str(movie)).Items.Item:
            title = item.ItemAttributes.Title 
            URL = item.ItemLinks.ItemLink.URL
            movies[movie].append(str(title))
            movies[movie].append(str(URL))
        #result2 = api.item_lookup(str(movie), ResponseGroup='Images')
        for items in api.item_lookup(str(movie), ResponseGroup='Images').Items.Item:
            imageURL = items.ImageSets.ImageSet.LargeImage.URL
            movies[movie].append(str(imageURL))


    
    # # movies2 = {'B004L9GLKE': ['Departed', 'http://www.amazon.com/Departed-Leonardo-DiCaprio/dp/tech-data/B004L9GLKE%3FSubscriptionId%3DAKIAJGEEABW2F4H7ZB4Q%26tag%3Dyueyingteng-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D386001%26creativeASIN%3DB004L9GLKE', 'http://ecx.images-amazon.com/images/I/51CN2a6OGvL.jpg'], 'B000S0DDG0': ['Dreamgirls', 'http://www.amazon.com/Dreamgirls-Jamie-Foxx/dp/tech-data/B000S0DDG0%3FSubscriptionId%3DAKIAJGEEABW2F4H7ZB4Q%26tag%3Dyueyingteng-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D386001%26creativeASIN%3DB000S0DDG0', 'http://ecx.images-amazon.com/images/I/51NsSmJiUxL.jpg'], '6300267881': ['The Exorcist [VHS]', 'http://www.amazon.com/The-Exorcist-VHS-Ellen-Burstyn/dp/tech-data/6300267881%3FSubscriptionId%3DAKIAJGEEABW2F4H7ZB4Q%26tag%3Dyueyingteng-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D386001%26creativeASIN%3D6300267881', 'http://ecx.images-amazon.com/images/I/21HWKZ0WSNL.jpg']}
    print(movies[testrun[0]][0])
    print(movies[testrun[0]][1])
    print(movies[testrun[0]][2])
    # print(movies2[testrun[0]][0])
    # print(movies2[testrun[0]][1])
    # print(movies2[testrun[0]][2])


    data = [{"title1" : movies[testrun[0]][0], "url1" : movies[testrun[0]][1], "imgUrl1" : movies[testrun[0]][2],
    "title2" : movies[testrun[1]][0], "url2" : movies[testrun[1]][1], "imgUrl2" : movies[testrun[1]][2],
    "title3" : movies[testrun[2]][0], "url3" : movies[testrun[2]][1], "imgUrl3" : movies[testrun[2]][2]}]
    # Writing JSON data
    
    #data = [{'title1': 'The Exorcist [VHS]', 'title2': 'Departed', 'title3': 'Dreamgirls', 'url1': 'http://www.amazon.com/The-Exorcist-VHS-Ellen-Burstyn/dp/tech-data/6300267881%3FSubscriptionId%3DAKIAJGEEABW2F4H7ZB4Q%26tag%3Dyueyingteng-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D386001%26creativeASIN%3D6300267881', 'url3': 'http://www.amazon.com/Dreamgirls-Jamie-Foxx/dp/tech-data/B000S0DDG0%3FSubscriptionId%3DAKIAJGEEABW2F4H7ZB4Q%26tag%3Dyueyingteng-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D386001%26creativeASIN%3DB000S0DDG0', 'url2': 'http://www.amazon.com/Departed-Leonardo-DiCaprio/dp/tech-data/B004L9GLKE%3FSubscriptionId%3DAKIAJGEEABW2F4H7ZB4Q%26tag%3Dyueyingteng-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D386001%26creativeASIN%3DB004L9GLKE', 'imgUrl3': 'http://ecx.images-amazon.com/images/I/51NsSmJiUxL.jpg', 'imgUrl2': 'http://ecx.images-amazon.com/images/I/51CN2a6OGvL.jpg', 'imgUrl1': 'http://ecx.images-amazon.com/images/I/21HWKZ0WSNL.jpg'}]

    print(data)
    with open('static/js/data.json', 'w') as f:
      json.dump(data,f, ensure_ascii = False, encoding = 'utf-8')

    return render_template('index.html')
    #return json.dumps({'status':'OK','user':_movie1,'pass':_rate1})
    #return redirect('NewUser.html')

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5009))
    app.run(host='0.0.0.0', port=port)

