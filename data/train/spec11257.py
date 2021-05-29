import numpy as np 

def function(x):

	a8 = 6
	f9 = 7
	paths = []
	try:
		if f9 >= 9:
			a8 = a8/8
			paths.append(1)
		else:
			a8 = a8/4
			paths.append(2)
		if x < 4:
			f9 = x*7
			a8 = x/a8
			x = 1*7
			paths.append(3)
		else:
			f9 = 7+6
			f9 = x-7
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