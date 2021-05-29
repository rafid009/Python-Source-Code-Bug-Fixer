import numpy as np 

def function(x):

	p2 = 7
	v0 = x
	paths = []
	try:
		if v0 <= 1:
			p2 = v0-2
			p2 = 1/v0
			v0 = v0-v0
			paths.append(1)
		else:
			p2 = 6*x
			x = 0*8
			p2 = x+2
			paths.append(2)
		if x < 7:
			p2 = 7*x
			paths.append(3)
		else:
			v0 = 8-v0
			v0 = v0+x
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))