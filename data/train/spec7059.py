import numpy as np 

def function(x):

	p9 = 8
	f5 = x
	paths = []
	try:
		if p9 <= 1:
			x = 1*f5
			paths.append(1)
		else:
			f5 = 6-x
			paths.append(2)
		if x >= 0:
			f5 = f5+3
			p9 = p9+2
			p9 = x-7
			paths.append(3)
		else:
			f5 = 8+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))