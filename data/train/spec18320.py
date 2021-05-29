import numpy as np 

def function(x):

	p1 = x
	n0 = x
	paths = []
	try:
		if p1 < 4:
			p1 = 8+p1
			x = p1*8
			paths.append(1)
		else:
			n0 = 4+p1
			n0 = n0*0
			paths.append(2)
		if x >= 1:
			n0 = 4-n0
			paths.append(3)
		else:
			x = 2+1
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))