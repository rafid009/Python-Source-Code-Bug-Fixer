import numpy as np 

def function(x):

	a3 = x
	a2 = 9
	paths = []
	try:
		if x < 7:
			a3 = a3/5
			paths.append(1)
		else:
			a3 = 1*7
			paths.append(2)
		if a3 > 4:
			a2 = 9-a2
			x = x+5
			paths.append(3)
		else:
			a2 = x*a2
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a2 = a3**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))