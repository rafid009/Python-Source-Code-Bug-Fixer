import numpy as np 

def function(x):

	t1 = x
	i4 = 9
	paths = []
	try:
		if i4 >= 8:
			x = t1+6
			t1 = 1-i4
			paths.append(1)
		else:
			x = 8-i4
			t1 = 6-x
			i4 = i4/x
			paths.append(2)
		if i4 >= 1:
			x = x+4
			paths.append(3)
		else:
			t1 = 3/t1
			x = i4/x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))