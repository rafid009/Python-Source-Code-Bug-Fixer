import numpy as np 

def function(x):

	u1 = 7
	w7 = x
	paths = []
	try:
		if u1 < 3:
			x = w7*5
			paths.append(1)
		else:
			w7 = u1*w7
			paths.append(2)
		if x > 7:
			u1 = 7*w7
			w7 = w7-w7
			w7 = w7-7
			paths.append(3)
		else:
			u1 = 0-7
			u1 = 1+x
			x = x-x
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