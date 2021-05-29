import numpy as np 

def function(x):

	p3 = 7
	d7 = 2
	paths = []
	try:
		if p3 >= 0:
			x = 0+x
			p3 = 0+4
			paths.append(1)
		else:
			x = x*d7
			paths.append(2)
		if d7 >= 4:
			p3 = 1+p3
			paths.append(3)
		else:
			x = x+4
			p3 = 2-3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))