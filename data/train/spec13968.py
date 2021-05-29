import numpy as np 

def function(x):

	t6 = 7
	t1 = 6
	paths = []
	try:
		if x <= 5:
			t6 = t6+5
			x = x-5
			x = x*3
			paths.append(1)
		else:
			t6 = t6/t6
			paths.append(2)
		if x >= 4:
			t6 = 9-t6
			t6 = t6+6
			t6 = 3-t6
			paths.append(3)
		else:
			t6 = t6-1
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))