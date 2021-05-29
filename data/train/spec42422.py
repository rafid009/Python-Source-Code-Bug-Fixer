import numpy as np 

def function(x):

	a2 = x
	j3 = x
	paths = []
	try:
		if a2 < 3:
			x = x/a2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if a2 >= 6:
			a2 = 1*6
			j3 = 5*j3
			paths.append(3)
		else:
			a2 = 3*a2
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