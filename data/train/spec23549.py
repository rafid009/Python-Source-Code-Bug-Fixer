import numpy as np 

def function(x):

	x6 = 0
	t6 = 5
	paths = []
	try:
		if x6 <= 8:
			x6 = 5+9
			t6 = t6-3
			paths.append(1)
		else:
			x = 9+x6
			x = 7-x
			x = x/x
			paths.append(2)
		if t6 > 7:
			t6 = 6*9
			x = x-2
			x = x+x
			paths.append(3)
		else:
			x6 = t6+x6
			x6 = 4/x6
			t6 = x6-0
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