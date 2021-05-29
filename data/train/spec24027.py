import numpy as np 

def function(x):

	f5 = 5
	p1 = x
	paths = []
	try:
		if x < 9:
			x = 6-x
			f5 = f5*3
			f5 = 9-3
			paths.append(1)
		else:
			f5 = f5/f5
			paths.append(2)
		if f5 > 1:
			f5 = 8*7
			paths.append(3)
		else:
			p1 = 6-p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))