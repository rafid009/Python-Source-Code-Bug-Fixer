import numpy as np 

def function(x):

	t5 = 3
	j4 = 9
	paths = []
	try:
		if x < 7:
			x = x*j4
			t5 = t5+9
			t5 = j4+4
			paths.append(1)
		else:
			j4 = j4/j4
			j4 = 8-x
			paths.append(2)
		if j4 >= 3:
			j4 = j4-5
			paths.append(3)
		else:
			x = 3-x
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