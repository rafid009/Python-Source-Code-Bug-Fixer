import numpy as np 

def function(x):

	a7 = 4
	t7 = x
	paths = []
	try:
		if x >= 3:
			a7 = a7*5
			t7 = 8*t7
			paths.append(1)
		else:
			a7 = 5*a7
			a7 = 5*x
			paths.append(2)
		if a7 <= 0:
			t7 = a7+t7
			t7 = t7*5
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))