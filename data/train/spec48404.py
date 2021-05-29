import numpy as np 

def function(x):

	i9 = x
	t5 = 6
	x = x
	paths = []
	try:
		if t5 > 9:
			x = t5*t5
			paths.append(1)
		else:
			t5 = t5*t5
			paths.append(2)
		if t5 <= 7:
			x = i9/x
			t5 = i9*t5
			paths.append(3)
		else:
			x = x/9
			t5 = t5/x
			i9 = 9+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))