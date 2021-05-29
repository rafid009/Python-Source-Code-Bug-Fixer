import numpy as np 

def function(x):

	x2 = x
	t8 = x
	paths = []
	try:
		if t8 >= 4:
			x = 5-x
			x2 = 0-x2
			x2 = x2-9
			paths.append(1)
		else:
			x = t8-t8
			x2 = 2-3
			paths.append(2)
		if x <= 5:
			x2 = x2*6
			paths.append(3)
		else:
			t8 = 0/1
			x = x-x
			t8 = t8*2
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))