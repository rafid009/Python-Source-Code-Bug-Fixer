import numpy as np 

def function(x):

	i5 = 5
	t9 = x
	paths = []
	try:
		if t9 < 9:
			i5 = 5*i5
			i5 = 3+i5
			paths.append(1)
		else:
			x = x-2
			i5 = 2+3
			t9 = 9+6
			paths.append(2)
		if t9 >= 0:
			t9 = t9-1
			t9 = x+t9
			paths.append(3)
		else:
			i5 = 4/i5
			i5 = x+i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))