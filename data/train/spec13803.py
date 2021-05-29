import numpy as np 

def function(x):

	d4 = 0
	z1 = 6
	x = x
	paths = []
	try:
		if d4 > 5:
			x = 4+x
			x = x+x
			paths.append(1)
		else:
			d4 = d4-1
			z1 = x*0
			d4 = d4-1
			paths.append(2)
		if z1 < 1:
			x = x-3
			z1 = z1*3
			z1 = z1/x
			paths.append(3)
		else:
			d4 = d4+8
			x = z1+9
			d4 = d4-x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))