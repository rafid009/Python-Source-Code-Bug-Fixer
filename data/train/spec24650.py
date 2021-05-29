import numpy as np 

def function(x):

	a3 = 4
	t8 = x
	paths = []
	try:
		if a3 > 5:
			x = x-3
			x = x-a3
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if a3 >= 5:
			a3 = 5-a3
			a3 = a3/a3
			a3 = a3/5
			paths.append(3)
		else:
			a3 = 8*a3
			t8 = t8*1
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))