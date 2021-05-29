import numpy as np 

def function(x):

	t6 = x
	e6 = 8
	paths = []
	try:
		if t6 <= 7:
			e6 = x/7
			paths.append(1)
		else:
			t6 = t6+6
			t6 = 2-6
			paths.append(2)
		if x > 6:
			x = 8-1
			x = 6-7
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))