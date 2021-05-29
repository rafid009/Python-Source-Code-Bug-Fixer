import numpy as np 

def function(x):

	q3 = x
	i0 = 6
	paths = []
	try:
		if x <= 3:
			q3 = q3+6
			q3 = 8*3
			x = i0/x
			paths.append(1)
		else:
			x = x-9
			q3 = 4/x
			paths.append(2)
		if q3 >= 7:
			x = x+i0
			paths.append(3)
		else:
			i0 = i0+q3
			q3 = 6+q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		i0 = q3**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))