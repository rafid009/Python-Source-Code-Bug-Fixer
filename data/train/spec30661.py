import numpy as np 

def function(x):

	e0 = 8
	t9 = 9
	paths = []
	try:
		if t9 >= 6:
			x = x-6
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x <= 9:
			t9 = t9*x
			t9 = 3-x
			paths.append(3)
		else:
			t9 = 8+9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))