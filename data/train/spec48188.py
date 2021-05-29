import numpy as np 

def function(x):

	p1 = x
	u6 = 8
	x = 6
	paths = []
	try:
		if p1 <= 8:
			x = p1+9
			paths.append(1)
		else:
			u6 = u6*9
			x = 1+x
			paths.append(2)
		if u6 > 1:
			x = x-1
			paths.append(3)
		else:
			p1 = 9/4
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