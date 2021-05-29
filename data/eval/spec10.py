import numpy as np 

def function(x):

	t8 = 7
	a8 = x
	paths = []
	try:
		if x >= 7:
			t8 = 4-x
			x = a8*8
			t8 = t8/a8
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if t8 >= 6:
			t8 = t8-2
			paths.append(3)
		else:
			a8 = x+t8
			x = x/x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		t8 = a8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))