import numpy as np 

def function(x):

	p8 = x
	v5 = 7
	paths = []
	try:
		if v5 >= 8:
			v5 = v5/4
			p8 = p8/p8
			paths.append(1)
		else:
			v5 = v5-p8
			paths.append(2)
		if v5 < 6:
			x = x*4
			v5 = p8+3
			p8 = 1+x
			paths.append(3)
		else:
			p8 = p8*7
			p8 = 6/p8
			p8 = 4-p8
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