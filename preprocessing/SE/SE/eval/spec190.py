import numpy as np 

def function(x):

	u4 = 1
	t6 = x
	x = 8
	paths = []
	try:
		if t6 < 0:
			x = 1/x
			paths.append(1)
		else:
			u4 = u4+9
			u4 = u4+t6
			paths.append(2)
		if u4 >= 5:
			u4 = x-u4
			u4 = 6-3
			t6 = 5-t6
			paths.append(3)
		else:
			t6 = 8*t6
			x = t6-x
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))