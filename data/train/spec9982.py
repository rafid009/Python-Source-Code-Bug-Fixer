import numpy as np 

def function(x):

	f1 = 7
	q0 = 2
	paths = []
	try:
		if x < 8:
			f1 = 6+0
			q0 = q0-1
			f1 = 4-f1
			paths.append(1)
		else:
			f1 = 0+f1
			x = q0+5
			x = x-q0
			paths.append(2)
		if q0 >= 6:
			x = x*8
			f1 = f1-7
			x = 6/3
			paths.append(3)
		else:
			q0 = x*8
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))