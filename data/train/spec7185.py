import numpy as np 

def function(x):

	x3 = 9
	t7 = 3
	paths = []
	try:
		if t7 < 8:
			x = 8+x
			paths.append(1)
		else:
			x3 = x/t7
			x = x+x
			t7 = 5/3
			paths.append(2)
		if t7 >= 6:
			x3 = 3-1
			x3 = x3/4
			paths.append(3)
		else:
			x3 = x3-4
			t7 = t7*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))