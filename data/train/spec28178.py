import numpy as np 

def function(x):

	t7 = x
	u1 = 1
	paths = []
	try:
		if t7 <= 5:
			u1 = t7-8
			x = x/4
			paths.append(1)
		else:
			x = x-5
			t7 = x-1
			paths.append(2)
		if x >= 8:
			t7 = u1-6
			u1 = u1-0
			paths.append(3)
		else:
			t7 = t7+8
			t7 = 8*x
			x = 0/x
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