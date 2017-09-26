import movie
import fresh_tomatoes

movie1 = movie.Movie("Горе-творец", "Сюжет основывается на реальной истории создания фильма «Комната», а также биографии его создателя — Томми Вайсо, которая была освещена в одноимённой книге.", "https://upload.wikimedia.org/wikipedia/ru/thumb/a/a6/The_Disaster_Artist.jpg/405px-The_Disaster_Artist.jpg", "https://www.youtube.com/watch?v=Mo2472JRhqw")
movie2 = movie.Movie("Банды Нью-Йорка", "В 1846 году в Нижнем Манхэттене в районе Пяти Улиц происходит столкновение между бандами «коренных» американцев и иммигрантов, осевших в Нью-Йорке не так давно. В ходе этой драки от рук главаря «коренных» Билла «Мясника» Каттинга погибает предводитель иммигрантов «Священник» Валлон, ирландец по происхождению. Малолетний сын Валлона, Амстердам, попадает в исправительное учреждение, откуда выходит только спустя 16 лет. Он возвращается в свой район, движимый желанием отомстить за смерть своего отца. Но очень быстро он понимает, что сделать это в одиночку у него не выйдет — подобраться к Каттингу не так-то просто. Случайно Амстердам сталкивается со знакомым из далёкого детства — Джонни Сирокко, который помогает ему втереться в доверие к «Мяснику». Так он получает возможность хладнокровно убить своего врага, но вместо этого решает совершить свою месть на глазах у всех в момент празднования очередной годовщины победы «коренных». Но его предают, и план мести проваливается. Каттинг неожиданно не убивает Амстердама, только жестоко избивает его, оставляя шрам на лице раскалённым ножом. После этого едва оставшийся в живых Амстердам решает собрать старые ирландские банды вместе и бросить вызов Каттингу.", "https://upload.wikimedia.org/wikipedia/ru/d/d4/Gangs_NY.jpg", "https://www.youtube.com/watch?v=s0cxVgNfTxY")

list_of_movies = [movie1, movie2]

fresh_tomatoes.open_movies_page(list_of_movies)