import numpy as np 

def function(x):

	e0 = x
	b9 = 2
	paths = []
	try:
		if e0 <= 5:
			x = e0+5
			x = 7*x
			paths.append(1)
		else:
			b9 = b9*3
			e0 = e0-0
			paths.append(2)
		if x > 1:
			b9 = b9+9
			e0 = e0/8
			b9 = b9/b9
			paths.append(3)
		else:
			x = x*b9
			x = 6-x
			e0 = e0-x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))