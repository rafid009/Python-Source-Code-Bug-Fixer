import numpy as np 

def function(x):

	f0 = 0
	p2 = x
	paths = []
	try:
		if f0 > 6:
			x = x-9
			p2 = 4-9
			paths.append(1)
		else:
			f0 = 5-f0
			p2 = 3-4
			paths.append(2)
		if x <= 6:
			f0 = f0*6
			p2 = 6+4
			paths.append(3)
		else:
			p2 = p2-x
			f0 = 2+p2
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