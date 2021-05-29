import numpy as np 

def function(x):

	j5 = x
	u2 = 8
	paths = []
	try:
		if j5 <= 9:
			x = x/x
			paths.append(1)
		else:
			j5 = u2-j5
			j5 = 8-5
			paths.append(2)
		if u2 < 2:
			j5 = u2*j5
			x = 2*x
			paths.append(3)
		else:
			j5 = j5-3
			u2 = 1-5
			u2 = x-1
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		u2 = j5**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))