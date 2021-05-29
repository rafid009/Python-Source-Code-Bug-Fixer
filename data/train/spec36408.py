import numpy as np 

def function(x):

	r2 = x
	p2 = 5
	paths = []
	try:
		if r2 <= 6:
			p2 = p2/r2
			r2 = r2+4
			r2 = x-r2
			paths.append(1)
		else:
			p2 = p2*7
			r2 = 2*r2
			paths.append(2)
		if p2 <= 9:
			p2 = r2/7
			p2 = p2/2
			paths.append(3)
		else:
			r2 = x-2
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))