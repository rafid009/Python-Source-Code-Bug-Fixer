import numpy as np 

def function(x):

	e3 = x
	t9 = x
	paths = []
	try:
		if e3 < 7:
			t9 = x*t9
			paths.append(1)
		else:
			e3 = e3*8
			t9 = 6-4
			e3 = e3/5
			paths.append(2)
		if x <= 8:
			t9 = t9*4
			x = x*t9
			paths.append(3)
		else:
			x = 5+x
			x = 9+0
			x = 8/e3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))