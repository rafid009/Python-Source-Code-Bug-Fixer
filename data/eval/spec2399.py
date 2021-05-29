import numpy as np 

def function(x):

	j0 = x
	t7 = x
	paths = []
	try:
		if t7 < 2:
			j0 = 8-4
			paths.append(1)
		else:
			j0 = 2-j0
			j0 = j0/1
			t7 = t7+8
			paths.append(2)
		if t7 <= 0:
			t7 = t7*7
			paths.append(3)
		else:
			t7 = t7*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))