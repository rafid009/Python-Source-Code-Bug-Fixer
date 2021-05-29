import numpy as np 

def function(x):

	o3 = x
	p1 = 2
	paths = []
	try:
		if p1 < 0:
			x = x*p1
			x = 0-7
			paths.append(1)
		else:
			x = 5-x
			p1 = 7+9
			paths.append(2)
		if x <= 0:
			p1 = p1-p1
			paths.append(3)
		else:
			p1 = x*1
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