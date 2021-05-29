import numpy as np 

def function(x):

	t9 = 9
	y7 = 3
	paths = []
	try:
		if x >= 9:
			t9 = t9*2
			t9 = y7/t9
			x = x+8
			paths.append(1)
		else:
			y7 = t9*y7
			y7 = y7*t9
			paths.append(2)
		if y7 <= 6:
			x = 3-5
			paths.append(3)
		else:
			x = x/1
			t9 = t9/x
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		y7 = t9**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))