import numpy as np 

def function(x):

	a4 = 1
	a2 = x
	paths = []
	try:
		if a4 < 4:
			x = 6+9
			x = x-a2
			a2 = a2+a2
			paths.append(1)
		else:
			a4 = a2/x
			paths.append(2)
		if a4 > 4:
			x = 9*a2
			x = 7-x
			paths.append(3)
		else:
			x = a4-a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))