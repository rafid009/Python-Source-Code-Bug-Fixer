import numpy as np 

def function(x):

	p0 = 2
	j6 = 2
	paths = []
	try:
		if x > 0:
			x = 6/x
			paths.append(1)
		else:
			x = x-4
			p0 = p0/2
			p0 = p0/9
			paths.append(2)
		if p0 <= 7:
			j6 = j6/x
			paths.append(3)
		else:
			j6 = j6/5
			j6 = j6/j6
			x = x+p0
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