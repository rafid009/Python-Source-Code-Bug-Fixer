import numpy as np 

def function(x):

	x5 = x
	t4 = 5
	paths = []
	try:
		if t4 > 1:
			x5 = 4+7
			x = x*0
			t4 = 2+6
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if x > 4:
			x = 5+t4
			paths.append(3)
		else:
			x = x5+7
			t4 = 0-x5
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))