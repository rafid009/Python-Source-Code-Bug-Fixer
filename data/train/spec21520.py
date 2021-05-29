import numpy as np 

def function(x):

	r3 = 1
	t8 = 3
	paths = []
	try:
		if t8 < 5:
			t8 = 0-t8
			paths.append(1)
		else:
			x = x-1
			r3 = r3-4
			paths.append(2)
		if t8 >= 5:
			x = 8*2
			paths.append(3)
		else:
			r3 = r3*3
			t8 = 2/x
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))