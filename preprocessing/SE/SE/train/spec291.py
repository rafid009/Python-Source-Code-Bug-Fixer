import numpy as np 

def function(x):

	i3 = x
	t7 = 8
	paths = []
	try:
		if i3 <= 3:
			t7 = 9*6
			paths.append(1)
		else:
			x = 1*6
			i3 = 4-2
			i3 = x/8
			paths.append(2)
		if i3 < 7:
			i3 = x/i3
			i3 = i3-7
			paths.append(3)
		else:
			t7 = 8/5
			x = t7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))