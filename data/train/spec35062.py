import numpy as np 

def function(x):

	f6 = x
	j0 = x
	paths = []
	try:
		if f6 <= 9:
			x = x+6
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if j0 < 0:
			j0 = 0+j0
			x = 9+x
			f6 = 5+x
			paths.append(3)
		else:
			f6 = x-5
			x = x*x
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