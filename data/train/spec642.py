import numpy as np 

def function(x):

	i0 = 6
	j7 = 6
	paths = []
	try:
		if i0 <= 9:
			i0 = i0+4
			paths.append(1)
		else:
			j7 = 5-j7
			i0 = i0-1
			x = i0/x
			paths.append(2)
		if x < 3:
			i0 = j7-i0
			j7 = j7-8
			j7 = 7*1
			paths.append(3)
		else:
			i0 = 2*1
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))