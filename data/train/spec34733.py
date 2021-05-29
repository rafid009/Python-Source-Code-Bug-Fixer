import numpy as np 

def function(x):

	a9 = 5
	u1 = 4
	paths = []
	try:
		if u1 > 8:
			u1 = 5*7
			a9 = a9*3
			u1 = x-a9
			paths.append(1)
		else:
			a9 = x+5
			paths.append(2)
		if u1 > 3:
			a9 = a9+a9
			u1 = u1+9
			paths.append(3)
		else:
			a9 = 8*a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		u1 = a9**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))