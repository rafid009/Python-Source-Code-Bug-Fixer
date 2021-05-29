import numpy as np 

def function(x):

	r3 = x
	p0 = 3
	paths = []
	try:
		if r3 < 5:
			p0 = r3/3
			p0 = x/p0
			paths.append(1)
		else:
			p0 = 0-2
			p0 = p0+p0
			paths.append(2)
		if r3 <= 3:
			r3 = p0-r3
			paths.append(3)
		else:
			r3 = r3+9
			p0 = 2+p0
			x = x-x
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