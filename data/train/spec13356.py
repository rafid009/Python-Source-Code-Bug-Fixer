import numpy as np 

def function(x):

	i0 = 3
	j7 = x
	paths = []
	try:
		if j7 < 9:
			x = x+6
			j7 = i0*j7
			i0 = i0/i0
			paths.append(1)
		else:
			i0 = 0/i0
			j7 = j7-0
			paths.append(2)
		if x > 7:
			j7 = i0*1
			paths.append(3)
		else:
			x = i0-0
			i0 = i0+9
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		i0 = j7**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))