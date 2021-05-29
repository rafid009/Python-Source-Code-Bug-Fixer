import numpy as np 

def function(x):

	a9 = x
	r9 = x
	paths = []
	try:
		if r9 <= 0:
			r9 = r9/a9
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if x > 8:
			x = 5+x
			a9 = a9+5
			a9 = 0*x
			paths.append(3)
		else:
			a9 = a9*8
			x = 7*8
			r9 = a9-r9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))