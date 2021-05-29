import numpy as np 

def function(x):

	i1 = 1
	o7 = x
	paths = []
	try:
		if i1 <= 0:
			i1 = x-i1
			paths.append(1)
		else:
			i1 = 9-i1
			x = x*1
			paths.append(2)
		if i1 > 7:
			x = x+6
			i1 = 5+i1
			paths.append(3)
		else:
			x = x+8
			i1 = i1-7
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		i1 = o7**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))