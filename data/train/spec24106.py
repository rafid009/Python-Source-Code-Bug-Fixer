import numpy as np 

def function(x):

	i6 = x
	t9 = x
	paths = []
	try:
		if t9 >= 8:
			x = x/3
			t9 = 1+t9
			t9 = t9/6
			paths.append(1)
		else:
			x = t9/x
			paths.append(2)
		if x <= 3:
			x = 7-4
			paths.append(3)
		else:
			i6 = i6-i6
			t9 = 2/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))