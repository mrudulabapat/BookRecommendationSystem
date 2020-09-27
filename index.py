import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from BUI1 import retrieve_input
from tkinter import *

goodbooks = pd.read_csv("D:\\desktop\\BookRecSystem_Project\\books.csv")
#print(goodbooks.head())

goodbooks.drop(['isbn13','language_code','work_ratings_count','work_text_reviews_count','ratings_1','ratings_2','ratings_3','ratings_4','ratings_5'], inplace=True,axis=1)
missvals = ['isbn','original_publication_year','original_title']
for i in missvals:
    goodbooks[i] = goodbooks[i].fillna('')

popularity_threshold = 40000
popular_book = goodbooks.query('ratings_count >= @popularity_threshold')
#print(popular_book.head())

popular_book_pivot = popular_book.pivot(index='title', columns= 'book_id', values='average_rating').fillna(0)
#print(popular_book_pivot.head())

popular_book_matrix = csr_matrix(popular_book_pivot.values)

model_knn = NearestNeighbors(metric='cosine',algorithm='brute')
model_knn.fit(popular_book_matrix)

#query_index = np.random.choice(popular_book_pivot.shape[0])
#print(query_index)

book_user_likes = retrieve_input()

query_index = popular_book_pivot.index.tolist().index(book_user_likes)
print(query_index)

distances,indices = model_knn.kneighbors(popular_book_pivot.iloc[query_index,:].values.reshape(1,-1), n_neighbors=11)

root = Tk()
root.geometry("650x650")
root.configure(background="#a1dbcd")
root.title("Recommendations")

#label = Label(root, text="Recommendations for "+retrieve_input()+" are:",font="Arial 12 bold", fg="blue", width=30, height=2 )
#label.place(x=250, y=10, anchor="center")

label = Label(root, text="Recommendations for "+retrieve_input()+" are:", bd=1, relief="solid", bg="yellow", font="Arial 14 bold", width=70, height=2)
label.place(x=325, y=40, anchor="center")

book_list = []
book_range=[]

for i in range(0, len(distances.flatten())):
    if i == 0:
        print('Recommendations for {0}:\n'.format(popular_book_pivot.index[query_index]))
    else:
        book_list.append(popular_book_pivot.index[indices.flatten()[i]])
        book_range.append(distances.flatten()[i])
        print('{0}: {1}, with distance of {2}:'.format(i, popular_book_pivot.index[indices.flatten()[i]], distances.flatten()[i]))

list1=Listbox(root, height=20, width=50, font="Arial 12 bold", fg="red", relief="solid")
list1.insert(0, book_list[1:2])
list1.insert(1, book_list[2:3])
list1.insert(2, book_list[3:4])
list1.insert(3, book_list[4:5])
list1.insert(4, book_list[5:6])
list1.insert(5, book_list[6:7])
list1.insert(6, book_list[7:8])
list1.insert(7, book_list[8:9])
list1.insert(8, book_list[9:10])
list1.insert(9, book_list[0:1])

list1.place(x=250, y=300, anchor="center")

list2=Listbox(root, height=20, width=20, font="Arial 12 bold", fg="red", relief="solid")
list2.insert(0, book_range[0:1])
list2.insert(1, book_range[1:2])
list2.insert(2, book_range[2:3])
list2.insert(3, book_range[3:4])
list2.insert(4, book_range[4:5])
list2.insert(5, book_range[5:6])
list2.insert(6, book_range[6:7])
list2.insert(7, book_range[7:8])
list2.insert(8, book_range[8:9])
list2.insert(9, book_range[9:10])

list2.place(x=550, y=300, anchor="center")

button2 = Button(root, text="Cancel", fg="white", command=root.quit, height=3, width=15, bg="red", font="Times 10 bold")

button2.place(x=325, y=575, anchor="center")

root.mainloop()
