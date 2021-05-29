import numpy as np 

def function(x):

	a9 = 2
	t4 = 4
	paths = []
	try:
		if a9 >= 5:
			a9 = 1-a9
			t4 = 5-t4
			a9 = 2+x
			paths.append(1)
		else:
			a9 = 0+a9
			paths.append(2)
		if x > 4:
			x = x-7
			paths.append(3)
		else:
			x = t4/1
			x = x/x
			a9 = x+x
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