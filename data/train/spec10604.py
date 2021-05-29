import numpy as np 

def function(x):

	a9 = x
	p2 = x
	paths = []
	try:
		if p2 < 4:
			a9 = 1*a9
			x = x*a9
			paths.append(1)
		else:
			x = x-8
			p2 = p2+x
			paths.append(2)
		if p2 <= 8:
			x = x-a9
			paths.append(3)
		else:
			a9 = a9+0
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