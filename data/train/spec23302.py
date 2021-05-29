import numpy as np 

def function(x):

	i0 = 8
	a5 = 7
	paths = []
	try:
		if x >= 8:
			x = 6+x
			a5 = x+2
			paths.append(1)
		else:
			a5 = x-5
			i0 = i0-0
			x = 8-x
			paths.append(2)
		if a5 < 2:
			x = x*6
			a5 = a5*9
			paths.append(3)
		else:
			x = x/4
			i0 = 2-x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		i0 = a5**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))