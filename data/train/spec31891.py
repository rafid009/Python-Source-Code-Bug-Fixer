import numpy as np 

def function(x):

	a6 = x
	t3 = 3
	x = 7
	paths = []
	try:
		if a6 > 4:
			a6 = 5-x
			paths.append(1)
		else:
			a6 = 7/9
			t3 = t3*a6
			paths.append(2)
		if a6 < 8:
			a6 = a6/x
			paths.append(3)
		else:
			x = 6/x
			t3 = 6*x
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