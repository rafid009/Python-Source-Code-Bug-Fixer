import numpy as np 

def function(x):

	u1 = x
	t4 = 3
	x = 4
	paths = []
	try:
		if u1 < 6:
			x = x+5
			paths.append(1)
		else:
			u1 = t4-u1
			t4 = x/t4
			paths.append(2)
		if x <= 7:
			t4 = 3*t4
			x = 8-x
			paths.append(3)
		else:
			x = 9/4
			u1 = 7+u1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))