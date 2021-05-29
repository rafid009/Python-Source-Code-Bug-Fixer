import numpy as np 

def function(x):

	t8 = x
	i3 = x
	paths = []
	try:
		if x <= 3:
			i3 = i3*3
			i3 = i3/7
			t8 = 8+7
			paths.append(1)
		else:
			t8 = i3-0
			paths.append(2)
		if i3 <= 4:
			x = i3*t8
			paths.append(3)
		else:
			x = x/7
			i3 = t8/x
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