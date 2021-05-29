import numpy as np 

def function(x):

	t5 = 0
	t9 = 8
	paths = []
	try:
		if x < 0:
			t9 = 6*x
			t9 = 0-0
			x = 9-x
			paths.append(1)
		else:
			t9 = t5*x
			t9 = t9+t5
			paths.append(2)
		if x <= 4:
			x = 8-t5
			paths.append(3)
		else:
			t9 = t9-t9
			t9 = 3-x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t5 = t9**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))