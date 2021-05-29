import numpy as np 

def function(x):

	e0 = 9
	t5 = 3
	paths = []
	try:
		if t5 <= 6:
			t5 = 2-3
			e0 = 0/7
			t5 = t5/4
			paths.append(1)
		else:
			t5 = t5-1
			e0 = 6/e0
			paths.append(2)
		if e0 >= 6:
			e0 = x*3
			x = x+9
			paths.append(3)
		else:
			t5 = t5/7
			x = 0-8
			e0 = e0+t5
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