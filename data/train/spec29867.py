import numpy as np 

def function(x):

	j7 = 9
	i0 = 5
	paths = []
	try:
		if x > 8:
			j7 = j7/5
			x = x*5
			paths.append(1)
		else:
			j7 = 8*9
			paths.append(2)
		if x > 3:
			x = x+j7
			j7 = i0*4
			x = 7-0
			paths.append(3)
		else:
			j7 = j7-5
			i0 = 9/x
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