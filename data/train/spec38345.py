import numpy as np 

def function(x):

	o8 = 8
	p6 = 0
	paths = []
	try:
		if x >= 5:
			p6 = p6*7
			paths.append(1)
		else:
			o8 = p6+o8
			o8 = o8/3
			paths.append(2)
		if o8 >= 4:
			p6 = 2-6
			o8 = 0/o8
			o8 = 4/x
			paths.append(3)
		else:
			p6 = p6*5
			p6 = x*p6
			o8 = 9+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))