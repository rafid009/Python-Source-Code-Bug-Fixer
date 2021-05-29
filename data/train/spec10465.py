import numpy as np 

def function(x):

	e7 = 5
	t6 = x
	paths = []
	try:
		if e7 > 8:
			x = x*x
			e7 = 8/2
			x = x-6
			paths.append(1)
		else:
			t6 = t6+e7
			x = x*3
			paths.append(2)
		if t6 < 4:
			t6 = 3+x
			e7 = e7-8
			paths.append(3)
		else:
			x = x-7
			e7 = 7*e7
			e7 = 8+4
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))