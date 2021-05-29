import numpy as np 

def function(x):

	t9 = x
	t6 = 3
	paths = []
	try:
		if x <= 1:
			x = t6*5
			paths.append(1)
		else:
			t6 = t9/t6
			paths.append(2)
		if t9 <= 5:
			x = x+8
			t9 = 6/t9
			paths.append(3)
		else:
			x = 7+x
			t9 = t9+2
			t9 = t9/6
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