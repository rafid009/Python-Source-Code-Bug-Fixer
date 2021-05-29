import numpy as np 

def function(x):

	q0 = x
	f3 = x
	paths = []
	try:
		if f3 < 8:
			f3 = 5-x
			q0 = 5/f3
			q0 = 7+q0
			paths.append(1)
		else:
			x = 5/x
			x = f3*x
			x = 0/x
			paths.append(2)
		if q0 < 1:
			f3 = f3+5
			x = 1/x
			f3 = f3-x
			paths.append(3)
		else:
			x = 4-1
			f3 = x-9
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		q0 = f3**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))