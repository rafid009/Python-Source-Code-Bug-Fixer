import numpy as np 

def function(x):

	p1 = 7
	j0 = x
	paths = []
	try:
		if p1 <= 0:
			j0 = 4-j0
			j0 = j0*2
			paths.append(1)
		else:
			x = x+j0
			j0 = 8/5
			j0 = 0+j0
			paths.append(2)
		if p1 < 3:
			j0 = 3*j0
			paths.append(3)
		else:
			p1 = 9-p1
			j0 = x*2
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