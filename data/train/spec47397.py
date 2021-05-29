import numpy as np 

def function(x):

	k4 = x
	t3 = 3
	paths = []
	try:
		if t3 > 3:
			k4 = 7/t3
			paths.append(1)
		else:
			t3 = t3/3
			x = 6-7
			t3 = t3/t3
			paths.append(2)
		if t3 >= 1:
			k4 = k4+5
			paths.append(3)
		else:
			t3 = 3*t3
			k4 = 0/k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))