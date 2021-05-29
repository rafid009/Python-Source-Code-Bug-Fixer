import numpy as np 

def function(x):

	v4 = 2
	t7 = x
	paths = []
	try:
		if v4 > 7:
			v4 = v4-x
			x = x/x
			t7 = 3/v4
			paths.append(1)
		else:
			v4 = v4*7
			v4 = v4/t7
			x = t7+x
			paths.append(2)
		if v4 > 2:
			t7 = 6-t7
			paths.append(3)
		else:
			t7 = 3*9
			x = x/5
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))