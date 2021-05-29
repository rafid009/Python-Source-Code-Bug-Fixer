import numpy as np 

def function(x):

	j0 = x
	p3 = x
	paths = []
	try:
		if x > 1:
			j0 = 3+j0
			x = 4-x
			p3 = x-p3
			paths.append(1)
		else:
			p3 = x/1
			x = x-0
			j0 = j0-1
			paths.append(2)
		if p3 < 4:
			x = 1*x
			paths.append(3)
		else:
			x = p3*j0
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))