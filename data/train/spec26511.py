import numpy as np 

def function(x):

	b7 = 9
	d8 = x
	paths = []
	try:
		if x <= 6:
			x = x*8
			d8 = b7/x
			d8 = 3+d8
			paths.append(1)
		else:
			x = x*x
			x = x+b7
			paths.append(2)
		if x > 7:
			b7 = x*9
			paths.append(3)
		else:
			d8 = d8+0
			d8 = d8+b7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))