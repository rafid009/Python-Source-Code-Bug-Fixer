import numpy as np 

def function(x):

	e9 = 1
	t0 = x
	paths = []
	try:
		if x <= 2:
			t0 = t0-5
			t0 = e9+e9
			e9 = 1-8
			paths.append(1)
		else:
			x = 9*0
			t0 = 4/5
			paths.append(2)
		if e9 >= 8:
			t0 = t0-6
			t0 = 8-4
			t0 = 9/e9
			paths.append(3)
		else:
			x = x+e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))