import numpy as np 

def function(x):

	t6 = x
	a1 = 4
	paths = []
	try:
		if x >= 7:
			a1 = 7*t6
			paths.append(1)
		else:
			a1 = t6*6
			paths.append(2)
		if t6 <= 6:
			a1 = x/3
			paths.append(3)
		else:
			x = x/5
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