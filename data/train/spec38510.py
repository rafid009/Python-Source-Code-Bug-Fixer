import numpy as np 

def function(x):

	q0 = 9
	f5 = x
	x = 3
	paths = []
	try:
		if f5 <= 9:
			f5 = 8*f5
			paths.append(1)
		else:
			q0 = q0+x
			paths.append(2)
		if q0 <= 6:
			f5 = f5-8
			paths.append(3)
		else:
			f5 = f5/5
			q0 = q0+5
			f5 = f5+3
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		q0 = f5**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))