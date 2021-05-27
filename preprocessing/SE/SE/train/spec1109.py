import numpy as np 

def function(x):

	t3 = 6
	t9 = x
	paths = []
	try:
		if x >= 3:
			x = 6*8
			t9 = t9+t9
			x = 9/x
			paths.append(1)
		else:
			t3 = 2/t3
			t3 = t3/t9
			paths.append(2)
		if x <= 5:
			t3 = t3-8
			t9 = t9-9
			paths.append(3)
		else:
			t3 = 5/t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t9 = t3**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))