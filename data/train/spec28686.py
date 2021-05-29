import numpy as np 

def function(x):

	f4 = 5
	q8 = x
	paths = []
	try:
		if x >= 7:
			f4 = 8-3
			q8 = q8*2
			x = x-0
			paths.append(1)
		else:
			f4 = f4*3
			q8 = q8*3
			paths.append(2)
		if f4 < 7:
			f4 = f4*x
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))