import numpy as np 

def function(x):

	f4 = 6
	q1 = 5
	paths = []
	try:
		if q1 <= 9:
			q1 = x/9
			paths.append(1)
		else:
			q1 = 3/q1
			paths.append(2)
		if f4 >= 9:
			x = x-1
			f4 = f4-2
			f4 = f4-6
			paths.append(3)
		else:
			q1 = 2+q1
			f4 = 4/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))