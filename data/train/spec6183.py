import numpy as np 

def function(x):

	o5 = x
	k1 = 9
	paths = []
	try:
		if k1 <= 1:
			o5 = x-1
			o5 = 3+k1
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x < 6:
			k1 = k1*x
			k1 = 6+k1
			paths.append(3)
		else:
			k1 = k1+o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))