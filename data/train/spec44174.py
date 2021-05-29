import numpy as np 

def function(x):

	f8 = 5
	a5 = 1
	paths = []
	try:
		if f8 >= 7:
			f8 = x/a5
			a5 = a5+2
			paths.append(1)
		else:
			a5 = 5*x
			paths.append(2)
		if a5 < 5:
			f8 = f8+0
			a5 = a5-3
			x = x*2
			paths.append(3)
		else:
			f8 = 0*f8
			a5 = 9-a5
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