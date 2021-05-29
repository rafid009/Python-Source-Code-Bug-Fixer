import numpy as np 

def function(x):

	o7 = x
	i1 = x
	paths = []
	try:
		if o7 > 3:
			o7 = 5/o7
			paths.append(1)
		else:
			x = 5*1
			o7 = o7-5
			x = o7/x
			paths.append(2)
		if o7 < 0:
			x = 1+x
			o7 = 3/o7
			o7 = 7*o7
			paths.append(3)
		else:
			o7 = 7*7
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