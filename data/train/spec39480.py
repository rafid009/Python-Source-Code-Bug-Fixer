import numpy as np 

def function(x):

	j8 = x
	o2 = 6
	paths = []
	try:
		if j8 <= 2:
			x = x-9
			x = 8+j8
			paths.append(1)
		else:
			j8 = j8-1
			paths.append(2)
		if x >= 7:
			o2 = 3-o2
			paths.append(3)
		else:
			x = 0-3
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))