import numpy as np 

def function(x):

	d9 = x
	n2 = x
	paths = []
	try:
		if n2 < 1:
			n2 = n2-5
			paths.append(1)
		else:
			x = 6+9
			paths.append(2)
		if x > 3:
			x = x*x
			x = x*8
			paths.append(3)
		else:
			n2 = 3/n2
			n2 = 5-1
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