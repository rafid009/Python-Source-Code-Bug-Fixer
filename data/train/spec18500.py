import numpy as np 

def function(x):

	a3 = x
	u2 = x
	paths = []
	try:
		if u2 >= 7:
			u2 = u2+3
			a3 = 9*a3
			paths.append(1)
		else:
			a3 = 7*x
			u2 = 5/3
			x = x+8
			paths.append(2)
		if x <= 9:
			u2 = u2/x
			paths.append(3)
		else:
			u2 = u2-1
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		u2 = a3**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))