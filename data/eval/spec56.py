import numpy as np 

def function(x):

	q3 = 5
	i0 = 7
	paths = []
	try:
		if x < 9:
			q3 = q3+8
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if i0 > 3:
			x = q3/9
			i0 = x-i0
			paths.append(3)
		else:
			q3 = 3-q3
			i0 = i0+1
			i0 = 3/i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))