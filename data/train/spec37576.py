import numpy as np 

def function(x):

	i0 = x
	t6 = 7
	paths = []
	try:
		if x > 7:
			t6 = 0/t6
			t6 = t6+t6
			paths.append(1)
		else:
			t6 = 4-t6
			x = 1/x
			paths.append(2)
		if x <= 9:
			x = i0+x
			paths.append(3)
		else:
			x = x/2
			i0 = 1/i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))