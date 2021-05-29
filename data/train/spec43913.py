import numpy as np 

def function(x):

	o1 = 2
	j0 = 3
	paths = []
	try:
		if j0 <= 4:
			j0 = 1*o1
			paths.append(1)
		else:
			x = j0-o1
			o1 = o1*x
			paths.append(2)
		if x < 3:
			o1 = 5/x
			x = x-0
			j0 = j0+5
			paths.append(3)
		else:
			j0 = x*o1
			x = x/9
			j0 = o1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))