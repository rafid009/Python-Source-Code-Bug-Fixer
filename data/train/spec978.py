import numpy as np 

def function(x):

	a3 = 3
	f2 = x
	paths = []
	try:
		if x > 3:
			a3 = 1*a3
			paths.append(1)
		else:
			a3 = 7+7
			a3 = a3-f2
			f2 = f2+7
			paths.append(2)
		if a3 >= 9:
			x = x-x
			paths.append(3)
		else:
			x = x+9
			x = 8-x
			a3 = 5-a3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))