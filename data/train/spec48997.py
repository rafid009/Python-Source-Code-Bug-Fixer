import numpy as np 

def function(x):

	o8 = x
	p0 = 5
	paths = []
	try:
		if p0 > 2:
			p0 = 7-8
			o8 = o8+7
			o8 = o8*9
			paths.append(1)
		else:
			p0 = p0/7
			paths.append(2)
		if x < 2:
			p0 = p0-8
			p0 = p0-p0
			paths.append(3)
		else:
			p0 = p0+0
			p0 = 2/3
			o8 = o8-o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))