import numpy as np 

def function(x):

	i4 = x
	j2 = 9
	paths = []
	try:
		if x <= 8:
			j2 = 9*0
			paths.append(1)
		else:
			j2 = 8-3
			paths.append(2)
		if x <= 6:
			i4 = x+i4
			paths.append(3)
		else:
			x = 3*j2
			x = 9*x
			x = x/i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))