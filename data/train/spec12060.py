import numpy as np 

def function(x):

	t6 = x
	j8 = 4
	x = 5
	paths = []
	try:
		if t6 <= 6:
			t6 = j8+t6
			j8 = 9-j8
			paths.append(1)
		else:
			x = x-9
			t6 = t6+6
			paths.append(2)
		if x > 6:
			j8 = j8/7
			paths.append(3)
		else:
			x = t6/1
			t6 = 1-t6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))