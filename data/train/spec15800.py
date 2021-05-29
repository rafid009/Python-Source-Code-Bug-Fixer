import numpy as np 

def function(x):

	y3 = x
	t7 = 9
	x = 4
	paths = []
	try:
		if t7 >= 9:
			x = x-1
			t7 = t7*0
			paths.append(1)
		else:
			x = x/y3
			paths.append(2)
		if x < 3:
			x = x-9
			y3 = y3+4
			paths.append(3)
		else:
			t7 = 8-t7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))