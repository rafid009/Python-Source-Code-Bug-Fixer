import numpy as np 

def function(x):

	a1 = 8
	i1 = 3
	paths = []
	try:
		if x <= 7:
			x = 6-8
			a1 = a1/a1
			x = 0-3
			paths.append(1)
		else:
			a1 = 0-9
			paths.append(2)
		if i1 <= 6:
			i1 = i1-0
			a1 = a1-6
			paths.append(3)
		else:
			x = x-1
			i1 = x-x
			x = x-a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))