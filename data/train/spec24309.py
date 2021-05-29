import numpy as np 

def function(x):

	e5 = x
	r7 = 7
	paths = []
	try:
		if e5 < 5:
			e5 = e5+x
			r7 = 6/e5
			e5 = 3-e5
			paths.append(1)
		else:
			x = x*x
			r7 = 8/e5
			paths.append(2)
		if e5 <= 9:
			r7 = r7+e5
			r7 = x-e5
			paths.append(3)
		else:
			e5 = 1*e5
			r7 = x*x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))