import numpy as np 

def function(x):

	a5 = x
	f9 = 6
	paths = []
	try:
		if f9 <= 0:
			x = a5-x
			f9 = f9+6
			f9 = 7/2
			paths.append(1)
		else:
			a5 = a5/6
			f9 = x/2
			f9 = f9-a5
			paths.append(2)
		if a5 >= 7:
			x = 1+x
			x = 2-f9
			x = a5*7
			paths.append(3)
		else:
			x = x*f9
			x = 0/8
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))