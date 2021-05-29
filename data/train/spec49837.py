import numpy as np 

def function(x):

	y6 = x
	t8 = x
	x = 7
	paths = []
	try:
		if y6 >= 9:
			x = x-x
			paths.append(1)
		else:
			y6 = y6*5
			paths.append(2)
		if y6 <= 7:
			t8 = y6/2
			paths.append(3)
		else:
			x = x+x
			x = 7+x
			y6 = y6-7
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		y6 = t8**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))