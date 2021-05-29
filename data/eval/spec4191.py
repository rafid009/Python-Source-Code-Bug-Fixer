import numpy as np 

def function(x):

	q9 = 4
	t8 = x
	paths = []
	try:
		if t8 <= 6:
			x = x-x
			paths.append(1)
		else:
			q9 = 4-7
			x = q9-1
			paths.append(2)
		if t8 < 3:
			q9 = q9+8
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))