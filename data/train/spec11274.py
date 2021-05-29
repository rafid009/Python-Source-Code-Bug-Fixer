import numpy as np 

def function(x):

	i1 = x
	a1 = x
	paths = []
	try:
		if i1 <= 3:
			a1 = a1-9
			a1 = a1-6
			i1 = i1-x
			paths.append(1)
		else:
			a1 = 8/a1
			i1 = 2-i1
			paths.append(2)
		if x >= 2:
			x = 6+x
			paths.append(3)
		else:
			a1 = 8-9
			i1 = 8*i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		a1 = i1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))