import numpy as np 

def function(x):

	b5 = x
	d4 = x
	x = x
	paths = []
	try:
		if d4 <= 8:
			x = x/4
			paths.append(1)
		else:
			b5 = 6+3
			b5 = 5-b5
			d4 = x+2
			paths.append(2)
		if b5 > 1:
			b5 = b5-x
			d4 = 1+9
			b5 = b5*x
			paths.append(3)
		else:
			b5 = b5*6
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))