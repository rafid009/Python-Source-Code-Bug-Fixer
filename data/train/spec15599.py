import numpy as np 

def function(x):

	i0 = x
	t5 = 6
	paths = []
	try:
		if i0 <= 4:
			x = x*3
			paths.append(1)
		else:
			x = x+i0
			paths.append(2)
		if x <= 9:
			t5 = 7+t5
			paths.append(3)
		else:
			t5 = 2/t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))