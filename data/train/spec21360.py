import numpy as np 

def function(x):

	s1 = 1
	o1 = 1
	paths = []
	try:
		if o1 >= 3:
			o1 = o1/o1
			paths.append(1)
		else:
			x = x*x
			x = x*s1
			paths.append(2)
		if x > 0:
			o1 = o1+9
			x = s1-x
			paths.append(3)
		else:
			x = 7/x
			o1 = s1*x
			x = 7*x
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