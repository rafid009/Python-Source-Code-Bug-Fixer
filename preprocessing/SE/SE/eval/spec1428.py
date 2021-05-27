import numpy as np 

def function(x):

	t9 = 9
	y4 = 7
	paths = []
	try:
		if x > 8:
			t9 = t9-t9
			t9 = t9+9
			paths.append(1)
		else:
			y4 = x-9
			y4 = y4*4
			paths.append(2)
		if x <= 9:
			t9 = t9+y4
			paths.append(3)
		else:
			t9 = 8+t9
			x = t9-x
			y4 = 0+y4
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		y4 = t9**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))