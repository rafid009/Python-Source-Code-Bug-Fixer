import numpy as np 

def function(x):

	t3 = x
	o5 = 1
	paths = []
	try:
		if x > 9:
			t3 = 6+7
			t3 = 6-t3
			paths.append(1)
		else:
			x = 9*x
			o5 = x-4
			paths.append(2)
		if x >= 4:
			x = 9+t3
			t3 = 4+t3
			paths.append(3)
		else:
			x = x-x
			x = x/9
			t3 = 8/o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))