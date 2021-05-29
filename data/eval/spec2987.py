import numpy as np 

def function(x):

	p3 = 4
	j1 = 1
	paths = []
	try:
		if p3 < 1:
			p3 = p3-p3
			paths.append(1)
		else:
			x = x*j1
			x = j1-p3
			x = 3*x
			paths.append(2)
		if p3 >= 5:
			p3 = p3*p3
			paths.append(3)
		else:
			j1 = x-p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))