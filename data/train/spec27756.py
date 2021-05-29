import numpy as np 

def function(x):

	p0 = x
	i1 = 3
	paths = []
	try:
		if i1 >= 6:
			p0 = 0-p0
			x = x*x
			paths.append(1)
		else:
			i1 = p0*7
			paths.append(2)
		if i1 < 5:
			i1 = p0-1
			x = 2-x
			paths.append(3)
		else:
			p0 = 1+p0
			p0 = 8-p0
			p0 = p0+p0
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))