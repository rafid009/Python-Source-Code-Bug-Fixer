import numpy as np 

def function(x):

	d8 = 3
	p7 = 8
	x = x
	paths = []
	try:
		if d8 < 7:
			x = x+1
			p7 = 6-8
			paths.append(1)
		else:
			p7 = 7-x
			p7 = 3+p7
			paths.append(2)
		if p7 > 7:
			x = 1-7
			d8 = 5-d8
			x = 8*p7
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))