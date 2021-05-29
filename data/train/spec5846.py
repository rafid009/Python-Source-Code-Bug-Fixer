import numpy as np 

def function(x):

	a6 = x
	paths = []
	try:
		if a6 > 0:
			a6 = a6*9
			paths.append(1)
		else:
			a6 = a6+0
			x = 5-a6
			x = x+5
			paths.append(2)
		if a6 <= 3:
			x = x*a6
			paths.append(3)
		else:
			a6 = a6-x
			a6 = a6-7
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))