import numpy as np 

def function(x):

	t3 = x
	x8 = 4
	paths = []
	try:
		if x8 >= 2:
			x = t3-8
			paths.append(1)
		else:
			x8 = x8*4
			x = 8-x
			paths.append(2)
		if t3 <= 9:
			t3 = 3-t3
			x = x8*x8
			paths.append(3)
		else:
			x8 = x8/2
			t3 = 2+8
			x8 = x8*t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))