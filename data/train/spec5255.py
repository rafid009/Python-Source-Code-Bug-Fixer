import numpy as np 

def function(x):

	t1 = x
	e6 = 4
	paths = []
	try:
		if e6 >= 0:
			e6 = e6*x
			e6 = x-e6
			paths.append(1)
		else:
			t1 = t1*5
			t1 = 9+8
			e6 = 7-e6
			paths.append(2)
		if e6 < 8:
			e6 = x+t1
			t1 = t1*2
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))