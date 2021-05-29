import numpy as np 

def function(x):

	j9 = 4
	p0 = 2
	paths = []
	try:
		if x < 4:
			j9 = 9-j9
			paths.append(1)
		else:
			p0 = 3-3
			x = 3*0
			paths.append(2)
		if j9 >= 4:
			p0 = x-j9
			paths.append(3)
		else:
			x = 7/x
			x = p0/6
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))