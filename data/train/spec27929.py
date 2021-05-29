import numpy as np 

def function(x):

	a5 = x
	u2 = 5
	paths = []
	try:
		if a5 >= 4:
			x = x*u2
			x = 4+u2
			u2 = u2*u2
			paths.append(1)
		else:
			u2 = u2-3
			a5 = a5/7
			x = x/9
			paths.append(2)
		if x <= 9:
			x = a5/7
			u2 = u2*3
			paths.append(3)
		else:
			x = x*x
			x = 6+x
			u2 = 3-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))