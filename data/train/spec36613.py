import numpy as np 

def function(x):

	i1 = 7
	a7 = x
	paths = []
	try:
		if i1 >= 3:
			i1 = a7*i1
			x = x-8
			a7 = i1-3
			paths.append(1)
		else:
			i1 = 6*8
			a7 = 2-8
			paths.append(2)
		if i1 <= 6:
			x = 1/x
			x = a7+7
			a7 = 5+4
			paths.append(3)
		else:
			i1 = i1*6
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))