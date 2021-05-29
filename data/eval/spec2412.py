import numpy as np 

def function(x):

	w0 = x
	p1 = 3
	paths = []
	try:
		if x >= 3:
			p1 = 7+x
			paths.append(1)
		else:
			p1 = 8+2
			p1 = w0/5
			x = 1+x
			paths.append(2)
		if x < 1:
			x = x*4
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))