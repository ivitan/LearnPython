str='''There's a girl but I let her get away
It's all my fault 'cause pride got in the way
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
It's my fault 'cause I said I needed space
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
No home 'cause I'm broken
No room to breathe
And I got no one to blame
No home for me
No home 'cause I'm broken
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
'Cause there's no hope for the broken heart
About that girl
The one I let get away'''

# 将字符串分割成单词列表
strList = str.split()
print(strList)

# 讲列表转成集合,去除重复项
strSet = set(strList)
print(strSet)

# 集合转成列表
strList2 = list(strSet)
print(strList2)

# 建个字典装上统计每个单词出现次数
strDict = {}
"""
for x in range(len(strList2)) :
    strDict[strList2[x]] = 0 # 字典初始值为０
    for y in range(len(strList)):
        if strList2[x]==strList[y]:
            strDict[strList2[x]]+=1
print(strDict)
"""

for key in strList2:
    strDict[key] = strDict.get(key,0)+1
print(strDict)