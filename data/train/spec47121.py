import numpy as np 

def function(x):

	x5 = 9
	a6 = 5
	paths = []
	try:
		if a6 <= 2:
			a6 = a6/a6
			a6 = x*1
			paths.append(1)
		else:
			x5 = 4+x
			paths.append(2)
		if x5 <= 6:
			x = 9/x
			x = 2+5
			a6 = a6+1
			paths.append(3)
		else:
			x5 = x5*3
			x = x-5
			x = a6/x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))