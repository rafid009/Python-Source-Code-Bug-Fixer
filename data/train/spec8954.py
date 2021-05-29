import numpy as np 

def function(x):

	o7 = x
	p7 = x
	paths = []
	try:
		if o7 <= 4:
			x = x+p7
			paths.append(1)
		else:
			o7 = o7-0
			paths.append(2)
		if p7 < 4:
			x = 1*x
			p7 = 7-p7
			paths.append(3)
		else:
			o7 = o7*3
			x = 1*7
			o7 = 9*4
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o7 = o7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))