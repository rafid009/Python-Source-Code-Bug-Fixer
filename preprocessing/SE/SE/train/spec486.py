import numpy as np 

def function(x):

	a8 = 4
	u2 = 3
	paths = []
	try:
		if u2 < 1:
			u2 = 9/u2
			u2 = u2*u2
			u2 = 1*u2
			paths.append(1)
		else:
			a8 = x/9
			a8 = 9*a8
			paths.append(2)
		if x > 5:
			x = 5+x
			paths.append(3)
		else:
			a8 = x/9
			u2 = 0+u2
			x = 8/3
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))