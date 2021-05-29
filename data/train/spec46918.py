import numpy as np 

def function(x):

	d4 = x
	r6 = 2
	paths = []
	try:
		if r6 <= 2:
			r6 = r6+7
			x = 1+d4
			paths.append(1)
		else:
			r6 = r6*d4
			paths.append(2)
		if x <= 6:
			r6 = 6*r6
			r6 = d4+r6
			paths.append(3)
		else:
			r6 = r6+d4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))