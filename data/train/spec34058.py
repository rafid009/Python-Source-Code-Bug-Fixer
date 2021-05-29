import numpy as np 

def function(x):

	y5 = 6
	t3 = x
	paths = []
	try:
		if y5 < 9:
			t3 = t3+7
			paths.append(1)
		else:
			x = x+2
			t3 = x/7
			paths.append(2)
		if t3 < 0:
			x = x+x
			y5 = y5/y5
			x = x+y5
			paths.append(3)
		else:
			t3 = 1-3
			y5 = y5-y5
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		y5 = t3**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))