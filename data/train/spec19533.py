import numpy as np 

def function(x):

	t3 = 1
	p0 = x
	paths = []
	try:
		if t3 >= 7:
			x = x-x
			paths.append(1)
		else:
			p0 = p0-6
			paths.append(2)
		if x > 3:
			t3 = t3-t3
			x = 5-x
			paths.append(3)
		else:
			p0 = 5-p0
			x = t3*x
			p0 = 0+7
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