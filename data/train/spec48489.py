import numpy as np 

def function(x):

	u1 = x
	i6 = 4
	x = 1
	paths = []
	try:
		if x >= 9:
			u1 = 4-u1
			paths.append(1)
		else:
			i6 = x*x
			paths.append(2)
		if i6 <= 3:
			x = x+9
			paths.append(3)
		else:
			i6 = 6/2
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))