import numpy as np 

def function(x):

	u5 = 5
	p8 = x
	x = 0
	paths = []
	try:
		if p8 < 8:
			p8 = 1-3
			paths.append(1)
		else:
			x = p8*x
			x = x-p8
			x = x-4
			paths.append(2)
		if u5 >= 2:
			u5 = 4*p8
			u5 = 9+5
			paths.append(3)
		else:
			x = x+8
			x = 4/2
			x = x/u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))