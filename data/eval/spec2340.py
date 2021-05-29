import numpy as np 

def function(x):

	p7 = 8
	d8 = 1
	x = x
	paths = []
	try:
		if p7 <= 7:
			p7 = 5*p7
			paths.append(1)
		else:
			p7 = 6+9
			paths.append(2)
		if p7 < 9:
			x = x-x
			paths.append(3)
		else:
			p7 = 0*5
			x = x*2
			d8 = 0-d8
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