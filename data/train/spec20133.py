import numpy as np 

def function(x):

	t9 = x
	j4 = x
	paths = []
	try:
		if x < 7:
			j4 = x+j4
			paths.append(1)
		else:
			t9 = t9-9
			paths.append(2)
		if x <= 5:
			j4 = 9*8
			x = x-t9
			paths.append(3)
		else:
			x = 1-4
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))