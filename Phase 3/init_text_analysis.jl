#= I have decided for the time being to not use
Julia for text analysis. An ecosystem still needs
to be built for optimization before I will use the language.
Python was a lot quicker in loading the data and it used a lot less
RAM and CPU=#
using DataFrames
using JSON


data = JSON.parsefile("/Users/Joel/Desktop/Tweets/final_poke_tweets.json")
df = DataFrames()


for x in data
  println(x)
end

#=function dict_to_df(x::Dict)
  s = "Dataframe("
    for k in keys(x)=#

#println(df)
