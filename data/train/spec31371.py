import numpy as np 

def function(x):

	u3 = 9
	d6 = 8
	paths = []
	try:
		if d6 > 0:
			u3 = u3*6
			u3 = 8-6
			u3 = u3*6
			paths.append(1)
		else:
			x = u3+x
			paths.append(2)
		if d6 > 1:
			u3 = d6/u3
			x = x-2
			d6 = u3/d6
			paths.append(3)
		else:
			d6 = d6-9
			u3 = 6+d6
			d6 = d6-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))