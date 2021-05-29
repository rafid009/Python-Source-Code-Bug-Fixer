import numpy as np 

def function(x):

	q3 = 4
	f7 = x
	paths = []
	try:
		if q3 >= 2:
			q3 = x+6
			f7 = 4/7
			paths.append(1)
		else:
			q3 = 6/q3
			f7 = 6/f7
			f7 = 3*f7
			paths.append(2)
		if q3 > 5:
			x = q3/x
			paths.append(3)
		else:
			q3 = 6+x
			q3 = f7*1
			q3 = q3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))