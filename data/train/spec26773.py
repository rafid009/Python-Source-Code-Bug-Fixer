import numpy as np 

def function(x):

	k3 = x
	p2 = 4
	paths = []
	try:
		if x >= 7:
			x = x-k3
			p2 = k3*p2
			paths.append(1)
		else:
			x = 3+k3
			p2 = 0+p2
			paths.append(2)
		if x >= 5:
			k3 = 7/k3
			x = x-3
			paths.append(3)
		else:
			x = x-0
			x = x+2
			p2 = 0+p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))