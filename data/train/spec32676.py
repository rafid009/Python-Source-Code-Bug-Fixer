import numpy as np 

def function(x):

	j0 = x
	p3 = x
	paths = []
	try:
		if j0 < 5:
			j0 = j0-j0
			p3 = p3*1
			j0 = 2-j0
			paths.append(1)
		else:
			j0 = j0-j0
			j0 = j0-3
			paths.append(2)
		if p3 > 3:
			j0 = j0*j0
			j0 = j0/2
			j0 = 4*j0
			paths.append(3)
		else:
			x = x*3
			j0 = j0*6
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))