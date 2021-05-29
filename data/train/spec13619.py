import numpy as np 

def function(x):

	t8 = 6
	a5 = x
	paths = []
	try:
		if a5 > 5:
			a5 = t8/6
			paths.append(1)
		else:
			a5 = 2/x
			t8 = a5/2
			paths.append(2)
		if x <= 9:
			x = x+1
			paths.append(3)
		else:
			t8 = t8-6
			x = x-3
			t8 = 4*4
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))