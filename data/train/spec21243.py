import numpy as np 

def function(x):

	v9 = 2
	u1 = x
	paths = []
	try:
		if x > 1:
			u1 = u1+x
			paths.append(1)
		else:
			v9 = 5-1
			v9 = v9-5
			u1 = u1*7
			paths.append(2)
		if v9 >= 5:
			v9 = v9*u1
			paths.append(3)
		else:
			x = v9+0
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		u1 = v9**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))