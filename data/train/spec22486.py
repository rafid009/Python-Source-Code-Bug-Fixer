import numpy as np 

def function(x):

	f6 = 8
	q4 = x
	paths = []
	try:
		if q4 < 0:
			f6 = f6-2
			f6 = f6/f6
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x <= 6:
			x = 8+q4
			paths.append(3)
		else:
			f6 = 4+f6
			x = x-7
			f6 = 9+5
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))