import numpy as np 

def function(x):

	j2 = 7
	t5 = 1
	paths = []
	try:
		if x >= 2:
			j2 = 6*j2
			paths.append(1)
		else:
			t5 = t5*j2
			paths.append(2)
		if t5 < 7:
			j2 = 2/9
			paths.append(3)
		else:
			t5 = 9+9
			j2 = 8-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))