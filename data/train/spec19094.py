import numpy as np 

def function(x):

	t2 = x
	e7 = 8
	paths = []
	try:
		if e7 > 9:
			x = x*8
			t2 = 7*8
			paths.append(1)
		else:
			x = x-6
			x = 4+x
			t2 = 4-x
			paths.append(2)
		if t2 >= 8:
			e7 = e7-8
			t2 = t2-2
			paths.append(3)
		else:
			t2 = t2+8
			e7 = e7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))