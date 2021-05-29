import numpy as np 

def function(x):

	a5 = 4
	o1 = x
	x = 4
	paths = []
	try:
		if x <= 2:
			x = x-9
			paths.append(1)
		else:
			a5 = x*x
			o1 = o1/x
			paths.append(2)
		if a5 > 2:
			x = x/5
			paths.append(3)
		else:
			o1 = 9-o1
			a5 = x-5
			a5 = a5/5
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))