import numpy as np 

def function(x):

	t8 = 2
	x5 = x
	paths = []
	try:
		if t8 > 9:
			x = t8/x
			t8 = t8-0
			paths.append(1)
		else:
			x = x+x
			t8 = t8+7
			paths.append(2)
		if x5 > 7:
			t8 = t8+x
			x5 = 5+x5
			t8 = t8*1
			paths.append(3)
		else:
			x5 = 9*x5
			x = t8-x
			x5 = 1*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))