import numpy as np 

def function(x):

	o7 = x
	j5 = 8
	paths = []
	try:
		if j5 <= 6:
			x = 3*o7
			j5 = 8/o7
			paths.append(1)
		else:
			o7 = 7/o7
			j5 = 9-x
			paths.append(2)
		if o7 < 0:
			x = 9+x
			paths.append(3)
		else:
			j5 = x+j5
			x = 5+2
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		j5 = o7**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))