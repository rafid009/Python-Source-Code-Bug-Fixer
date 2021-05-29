import numpy as np 

def function(x):

	a6 = 5
	t8 = x
	x = 0
	paths = []
	try:
		if a6 >= 6:
			x = 5/x
			paths.append(1)
		else:
			t8 = 7*t8
			x = 2*x
			t8 = 3+x
			paths.append(2)
		if x < 1:
			a6 = a6+2
			x = 0*x
			a6 = 5-a6
			paths.append(3)
		else:
			a6 = a6/4
			t8 = 8-t8
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