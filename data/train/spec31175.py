import numpy as np 

def function(x):

	v6 = x
	o1 = 2
	paths = []
	try:
		if x < 6:
			v6 = v6+4
			v6 = v6+o1
			v6 = v6*x
			paths.append(1)
		else:
			v6 = 9/3
			o1 = o1+2
			paths.append(2)
		if o1 > 3:
			x = x-3
			x = 5-0
			o1 = o1+x
			paths.append(3)
		else:
			x = x/v6
			o1 = o1-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))