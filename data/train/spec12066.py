import numpy as np 

def function(x):

	f9 = x
	a1 = x
	paths = []
	try:
		if a1 > 7:
			f9 = f9*4
			paths.append(1)
		else:
			a1 = x*a1
			paths.append(2)
		if f9 >= 8:
			f9 = 6*f9
			f9 = f9*x
			f9 = f9+9
			paths.append(3)
		else:
			a1 = 9-a1
			x = 5+f9
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))