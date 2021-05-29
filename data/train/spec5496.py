import numpy as np 

def function(x):

	t6 = 3
	a3 = x
	x = 1
	paths = []
	try:
		if x < 8:
			a3 = t6-9
			t6 = t6*5
			paths.append(1)
		else:
			a3 = a3-9
			paths.append(2)
		if x < 6:
			x = x-8
			x = 3*x
			t6 = a3/5
			paths.append(3)
		else:
			a3 = a3+7
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		a3 = t6**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))