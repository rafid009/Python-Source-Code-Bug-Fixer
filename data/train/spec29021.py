import numpy as np 

def function(x):

	o6 = x
	y4 = x
	paths = []
	try:
		if o6 < 7:
			x = y4*6
			o6 = y4+o6
			x = 2+x
			paths.append(1)
		else:
			x = 0*x
			y4 = y4/y4
			paths.append(2)
		if o6 <= 5:
			o6 = 3+9
			o6 = o6*1
			paths.append(3)
		else:
			y4 = y4+9
			x = 0*2
			x = 8+o6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))