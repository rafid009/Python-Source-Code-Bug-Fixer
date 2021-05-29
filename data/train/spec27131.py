import numpy as np 

def function(x):

	q5 = x
	o1 = 9
	paths = []
	try:
		if x <= 8:
			o1 = o1*9
			paths.append(1)
		else:
			o1 = o1/q5
			paths.append(2)
		if o1 < 1:
			x = x*7
			o1 = 4*9
			paths.append(3)
		else:
			o1 = 0+1
			o1 = x/2
			x = x-0
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