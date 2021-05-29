import numpy as np 

def function(x):

	n7 = x
	b0 = x
	paths = []
	try:
		if n7 > 4:
			b0 = b0*n7
			n7 = 2+5
			paths.append(1)
		else:
			x = n7/1
			paths.append(2)
		if x <= 9:
			x = x*x
			x = x+5
			paths.append(3)
		else:
			x = x-3
			n7 = n7/7
			b0 = b0*7
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))