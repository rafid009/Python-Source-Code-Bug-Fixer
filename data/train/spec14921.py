import numpy as np 

def function(x):

	v2 = 5
	u1 = x
	paths = []
	try:
		if x > 8:
			u1 = u1/9
			x = x-v2
			paths.append(1)
		else:
			v2 = v2*x
			paths.append(2)
		if v2 < 2:
			x = x+v2
			u1 = 9*u1
			paths.append(3)
		else:
			v2 = v2*3
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