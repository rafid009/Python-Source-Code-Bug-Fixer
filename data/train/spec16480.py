import numpy as np 

def function(x):

	u1 = x
	o5 = x
	paths = []
	try:
		if x >= 5:
			x = 9-o5
			paths.append(1)
		else:
			u1 = u1-5
			x = x/u1
			u1 = u1-8
			paths.append(2)
		if x <= 2:
			x = 9+x
			paths.append(3)
		else:
			o5 = o5-2
			o5 = o5*o5
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))