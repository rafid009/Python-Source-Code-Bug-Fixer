import numpy as np 

def function(x):

	e0 = 5
	t5 = 7
	x = 9
	paths = []
	try:
		if x >= 9:
			e0 = 1+e0
			e0 = 7*e0
			paths.append(1)
		else:
			e0 = t5+3
			t5 = t5/9
			t5 = 7/t5
			paths.append(2)
		if e0 > 7:
			x = 7-x
			paths.append(3)
		else:
			t5 = t5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))