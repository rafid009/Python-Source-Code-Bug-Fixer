import numpy as np 

def function(x):

	u4 = x
	p5 = 7
	paths = []
	try:
		if p5 >= 3:
			x = x*4
			u4 = 1*u4
			u4 = 1/x
			paths.append(1)
		else:
			u4 = 1*u4
			paths.append(2)
		if p5 >= 8:
			x = 1-5
			u4 = 6+8
			x = x-x
			paths.append(3)
		else:
			x = x*p5
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