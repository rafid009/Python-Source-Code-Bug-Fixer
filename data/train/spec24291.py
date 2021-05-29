import numpy as np 

def function(x):

	n7 = 8
	t8 = x
	paths = []
	try:
		if x > 4:
			n7 = 6*n7
			t8 = t8*3
			x = x/2
			paths.append(1)
		else:
			t8 = 0/2
			n7 = 4+3
			paths.append(2)
		if n7 >= 2:
			t8 = t8-4
			t8 = 8-t8
			paths.append(3)
		else:
			n7 = n7/2
			t8 = t8-9
			t8 = t8-1
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