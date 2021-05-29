import numpy as np 

def function(x):

	p9 = 8
	e5 = x
	x = x
	paths = []
	try:
		if x <= 6:
			p9 = x*e5
			p9 = p9-5
			paths.append(1)
		else:
			x = x-5
			x = 6-x
			x = x+3
			paths.append(2)
		if p9 < 4:
			p9 = 9+5
			paths.append(3)
		else:
			x = 2+x
			e5 = e5*e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))