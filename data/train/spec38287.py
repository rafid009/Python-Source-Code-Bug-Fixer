import numpy as np 

def function(x):

	t4 = 0
	j8 = 9
	paths = []
	try:
		if t4 > 5:
			t4 = 9*t4
			paths.append(1)
		else:
			j8 = j8+j8
			t4 = j8+x
			paths.append(2)
		if t4 > 4:
			j8 = j8*4
			t4 = t4/6
			paths.append(3)
		else:
			x = x-5
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