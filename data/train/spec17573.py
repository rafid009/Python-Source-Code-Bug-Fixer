import numpy as np 

def function(x):

	j9 = 4
	t9 = 8
	paths = []
	try:
		if x <= 9:
			j9 = t9*2
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if j9 >= 8:
			j9 = 4/8
			paths.append(3)
		else:
			x = 7-1
			t9 = t9*x
			j9 = 4/j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))