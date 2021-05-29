import numpy as np 

def function(x):

	j7 = 4
	i0 = 5
	paths = []
	try:
		if j7 <= 9:
			i0 = i0+8
			paths.append(1)
		else:
			x = j7+j7
			j7 = i0/j7
			paths.append(2)
		if j7 > 3:
			i0 = x*i0
			x = 3+x
			paths.append(3)
		else:
			i0 = 8-7
			i0 = i0-x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		j7 = i0**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))