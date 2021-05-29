import numpy as np 

def function(x):

	a9 = 5
	n1 = x
	paths = []
	try:
		if x >= 2:
			a9 = 6-a9
			a9 = 1+x
			x = n1+7
			paths.append(1)
		else:
			n1 = 8*n1
			a9 = x*1
			n1 = 7+6
			paths.append(2)
		if a9 <= 2:
			a9 = 8+a9
			a9 = a9+2
			paths.append(3)
		else:
			a9 = 8*x
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