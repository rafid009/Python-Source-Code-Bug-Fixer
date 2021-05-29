import numpy as np 

def function(x):

	i4 = 8
	t4 = x
	paths = []
	try:
		if i4 <= 2:
			i4 = 7-i4
			t4 = t4+3
			paths.append(1)
		else:
			i4 = i4/t4
			paths.append(2)
		if t4 >= 3:
			t4 = t4/8
			x = x+t4
			paths.append(3)
		else:
			x = x*6
			t4 = 6+t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))