str='''There's a girl but I let her get away
It's all my fault cause pride got in the way
And I'd be lying if I said I was ok
About that girl the one I let get away
I keep saying no
This can't be the way we're supposed to be
I keep saying no
There's gotta be a way to get you close to me
Now I know you gotta
Speak up if you want somebody
Can't let him get away, oh no
You don't wanna end up sorry
The way that I'm feeling everyday
No no no no
There's no hope for the broken heart
No no no no
There's no hope for the broken
There's a girl but I let her get away
It's my fault cause I said I needed space
I've been torturing myself night and day
About that girl, the one I let get away
I keep saying no
This can't be the way we're supposed to be
I keep saying no
There's gotta be a way to get you
There's gotta be a way
To get you close to me
You gotta
Speak up if you want somebody
Can't let him get away, oh no
You don't wanna end up sorry
The way that I'm feeling everyday
No no no no
There's no hope for the broken heart
No no no no
There's no hope for the broken
No home for me
No home cause I'm broken
No room to breathe
And I got no one to blame
No home for me
No home cause I'm broken
About that girl
The one I let get away
So you better speak up if you want somebody
Can't let him get away oh no no
You don't wanna end up sorry
The way that I'm feeling everyday
Don't you know
No no no no
There's no hope for the broken heart
Don't you know
No no no no
There's no hope for the broken
You don't wanna lose at love
It's only gonna hurt too much
I'm telling you
You don't wanna lose at love
It's only gonna hurt too much
You don't wanna lose at love
Cause there's no hope for the broken heart
About that girl
The one I let get away'''

''''
str = str.lower() # 将字符串转为小写
str_list = str.split() # 将字符串行切片分割成单词列表
str_set = set(str_list) # 将列表转成集合,去除重复项
str_list2 = list(str_set) # 集合转成列表
str_list2 = list(str_list)
#str_list2.sort()

result_dict = {}
for item in str_list2:
    result_dict[item]=str_list2.count(item)
print(result_dict)
'''
str = str.lower() # 将字符串转为小写
str_list = str.split() # 将字符串行切片分割成单词列表
str_set=set(str_list) # 将列表转成集合,去除重复项
result_dict={}
for item in str_list:
    result_dict[item] = str_list.count(item)
print(result_dict,len(result_dict))