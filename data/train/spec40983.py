import numpy as np 

def function(x):

	t8 = 5
	e5 = 7
	paths = []
	try:
		if e5 > 1:
			e5 = 6+t8
			paths.append(1)
		else:
			e5 = 1+x
			x = 9+x
			paths.append(2)
		if x < 6:
			e5 = t8-e5
			x = 4+x
			e5 = e5/1
			paths.append(3)
		else:
			x = x-3
			t8 = 3/t8
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