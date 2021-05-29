import numpy as np 

def function(x):

	p0 = 9
	q4 = x
	paths = []
	try:
		if x <= 5:
			x = 4+q4
			p0 = 7/2
			p0 = 6+p0
			paths.append(1)
		else:
			p0 = p0+8
			q4 = 2+q4
			p0 = p0/x
			paths.append(2)
		if x <= 3:
			p0 = q4-2
			q4 = 6/q4
			paths.append(3)
		else:
			p0 = p0*8
			q4 = 0-q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))