import numpy as np 

def function(x):

	p8 = x
	u4 = x
	x = 3
	paths = []
	try:
		if p8 >= 3:
			u4 = u4*x
			x = x/u4
			paths.append(1)
		else:
			p8 = p8+0
			x = u4*6
			paths.append(2)
		if p8 <= 5:
			p8 = 4*p8
			x = 5*x
			p8 = 4+p8
			paths.append(3)
		else:
			p8 = p8-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))