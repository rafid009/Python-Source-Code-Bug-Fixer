import numpy as np 

def function(x):

	f9 = 6
	a8 = x
	paths = []
	try:
		if a8 > 6:
			a8 = 9*a8
			f9 = 3-6
			paths.append(1)
		else:
			a8 = 3/a8
			paths.append(2)
		if x > 8:
			x = x-f9
			x = x+9
			a8 = 3/a8
			paths.append(3)
		else:
			x = 0*0
			x = 7-x
			f9 = f9+a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		f9 = a8**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))