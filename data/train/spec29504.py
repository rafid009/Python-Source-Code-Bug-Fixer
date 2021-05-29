import numpy as np 

def function(x):

	p2 = x
	o8 = x
	paths = []
	try:
		if x <= 4:
			x = 5+o8
			paths.append(1)
		else:
			o8 = 0+o8
			paths.append(2)
		if p2 <= 0:
			x = x+7
			p2 = p2-4
			o8 = o8/8
			paths.append(3)
		else:
			o8 = o8/7
			o8 = 4-9
			o8 = 7+o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))