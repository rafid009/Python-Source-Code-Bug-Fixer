import numpy as np 

def function(x):

	e9 = 0
	t7 = x
	paths = []
	try:
		if e9 >= 2:
			e9 = x-e9
			t7 = 0-e9
			t7 = 8-6
			paths.append(1)
		else:
			x = e9/t7
			e9 = 1+e9
			paths.append(2)
		if t7 <= 8:
			t7 = 2+t7
			paths.append(3)
		else:
			x = x+0
			e9 = 9-2
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		e9 = t7**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))