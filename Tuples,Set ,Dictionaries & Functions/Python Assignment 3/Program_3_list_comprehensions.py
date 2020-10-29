'''2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''

#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
lst1 ='ACADGILD'
result_lst1 = [i for i in lst1]
print(result_lst1)

#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
lst2 = ['x','y','z']
result_lst2 = [i*n for i in lst2 for n in range(1,5)]
print(result_lst2)

#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
lst3 = ['x','y','z']
result_lst3 = [i*n for n in range(1,5) for i in lst3 ]
print(result_lst3)

#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
lst4 = [2,3,4]
result_lst4 = [[i+num] for i in lst4 for num in range(0,3)]
print(result_lst4)

#[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
lst5 = [2, 3, 4, 5]
result_lst5 = [[i+num for i in lst5] for num in range(0,4)]
print(result_lst5)

#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
lst6 = [1,2,3]
result_lst6 = [(a,b) for a in lst6 for b in lst6]
print(result_lst6)
