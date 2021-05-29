import numpy as np 

def function(x):

	a3 = x
	u3 = x
	paths = []
	try:
		if u3 < 2:
			a3 = a3/1
			x = 9-0
			x = a3/x
			paths.append(1)
		else:
			a3 = u3/6
			paths.append(2)
		if a3 >= 4:
			x = x*u3
			u3 = 0*9
			paths.append(3)
		else:
			x = 3-7
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))