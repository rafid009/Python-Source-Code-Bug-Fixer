import numpy as np 

def function(x):

	p6 = 0
	f2 = 1
	paths = []
	try:
		if x >= 0:
			p6 = x+p6
			x = 6-x
			f2 = 9-8
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if f2 > 4:
			x = 5/1
			f2 = 6/f2
			f2 = f2/8
			paths.append(3)
		else:
			f2 = p6/f2
			p6 = p6*2
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