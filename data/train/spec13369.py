import numpy as np 

def function(x):

	j5 = x
	o6 = 0
	paths = []
	try:
		if x > 6:
			j5 = 2+j5
			paths.append(1)
		else:
			o6 = o6/2
			o6 = 0+o6
			paths.append(2)
		if j5 > 5:
			x = x-6
			o6 = o6*2
			o6 = o6+x
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))