import numpy as np 

def function(x):

	b4 = x
	d6 = 2
	paths = []
	try:
		if d6 > 1:
			x = x-6
			x = x*7
			paths.append(1)
		else:
			d6 = 0*d6
			b4 = 4/2
			b4 = b4/4
			paths.append(2)
		if b4 > 3:
			b4 = x/4
			paths.append(3)
		else:
			d6 = 3*d6
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))