import numpy as np 

def function(x):

	t9 = 2
	k4 = 1
	paths = []
	try:
		if x > 7:
			x = k4+9
			t9 = 9+t9
			paths.append(1)
		else:
			k4 = k4/k4
			k4 = 5+k4
			paths.append(2)
		if k4 <= 6:
			x = k4-5
			paths.append(3)
		else:
			x = 4+x
			k4 = k4+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))