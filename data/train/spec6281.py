import numpy as np 

def function(x):

	e3 = 0
	t0 = x
	paths = []
	try:
		if e3 <= 0:
			x = 6+x
			paths.append(1)
		else:
			x = x*1
			e3 = e3-e3
			paths.append(2)
		if t0 < 8:
			e3 = e3*3
			paths.append(3)
		else:
			t0 = t0-3
			t0 = 7-x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		e3 = t0**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))