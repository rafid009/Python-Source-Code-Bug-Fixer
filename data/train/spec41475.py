import numpy as np 

def function(x):

	u3 = x
	o1 = 6
	paths = []
	try:
		if u3 >= 3:
			o1 = 8/x
			paths.append(1)
		else:
			o1 = o1/u3
			x = u3-1
			u3 = u3+0
			paths.append(2)
		if o1 > 2:
			o1 = o1-u3
			paths.append(3)
		else:
			u3 = u3-9
			u3 = 7+6
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