import numpy as np 

def function(x):

	a1 = x
	v7 = 1
	x = 7
	paths = []
	try:
		if x > 4:
			v7 = 4*v7
			paths.append(1)
		else:
			a1 = 3+1
			a1 = 6*a1
			paths.append(2)
		if a1 <= 0:
			v7 = 5/6
			paths.append(3)
		else:
			a1 = a1/2
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))