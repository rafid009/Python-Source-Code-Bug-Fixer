import numpy as np 

def function(x):

	a9 = x
	a2 = x
	paths = []
	try:
		if a9 > 1:
			x = 3-2
			a2 = 5*x
			paths.append(1)
		else:
			a2 = a2-3
			a9 = 5-a9
			a9 = a9*a2
			paths.append(2)
		if a2 < 3:
			a2 = 7/5
			paths.append(3)
		else:
			x = 8*1
			a9 = 1*x
			a2 = a9/8
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))