import numpy as np 

def function(x):

	i1 = 2
	i3 = 3
	paths = []
	try:
		if i3 > 5:
			x = 5-0
			paths.append(1)
		else:
			x = 2/x
			i1 = i1*8
			paths.append(2)
		if x <= 6:
			i1 = 7-2
			x = 6/x
			i3 = 9+i3
			paths.append(3)
		else:
			x = x-4
			i1 = x/4
			i1 = i1+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))