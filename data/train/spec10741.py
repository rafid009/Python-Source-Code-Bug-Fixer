import numpy as np 

def function(x):

	p0 = 1
	o1 = 2
	paths = []
	try:
		if o1 <= 4:
			o1 = 3-o1
			o1 = o1*x
			paths.append(1)
		else:
			o1 = 9-p0
			o1 = o1-8
			o1 = o1*1
			paths.append(2)
		if x <= 5:
			p0 = 5+p0
			paths.append(3)
		else:
			p0 = 7*5
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