import numpy as np 

def function(x):

	t9 = x
	j8 = 0
	paths = []
	try:
		if j8 >= 0:
			j8 = 1+j8
			x = x-4
			x = t9/x
			paths.append(1)
		else:
			j8 = j8+5
			j8 = 6-j8
			j8 = j8+9
			paths.append(2)
		if t9 <= 1:
			x = 5+j8
			j8 = j8*j8
			paths.append(3)
		else:
			j8 = j8*x
			t9 = t9*7
			t9 = 4-7
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