import numpy as np 

def function(x):

	i1 = x
	a8 = x
	paths = []
	try:
		if x < 6:
			x = 7*8
			paths.append(1)
		else:
			x = i1/a8
			x = 8+x
			x = a8-x
			paths.append(2)
		if i1 <= 2:
			a8 = 4*7
			x = 2+7
			paths.append(3)
		else:
			a8 = 6-a8
			x = 7/x
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