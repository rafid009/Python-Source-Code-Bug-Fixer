import numpy as np 

def function(x):

	t7 = x
	u0 = 6
	paths = []
	try:
		if t7 < 3:
			u0 = u0/4
			paths.append(1)
		else:
			u0 = u0-3
			paths.append(2)
		if t7 >= 7:
			x = u0+x
			t7 = 5/t7
			t7 = t7+x
			paths.append(3)
		else:
			x = 5/6
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		u0 = t7**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))