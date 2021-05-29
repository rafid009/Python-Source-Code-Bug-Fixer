import numpy as np 

def function(x):

	b9 = x
	t6 = x
	x = 1
	paths = []
	try:
		if t6 < 7:
			x = 1/x
			paths.append(1)
		else:
			b9 = b9*6
			b9 = 9+4
			t6 = 6-t6
			paths.append(2)
		if t6 <= 3:
			b9 = b9-3
			paths.append(3)
		else:
			t6 = 8/t6
			b9 = b9-2
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))