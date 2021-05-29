import numpy as np 

def function(x):

	n6 = x
	o6 = 7
	paths = []
	try:
		if x < 8:
			x = 5+9
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if n6 >= 9:
			x = 1+0
			o6 = o6/7
			x = 4/7
			paths.append(3)
		else:
			o6 = 7*o6
			o6 = 2*n6
			x = 9+7
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))