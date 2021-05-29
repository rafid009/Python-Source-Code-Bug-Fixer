import numpy as np 

def function(x):

	v8 = x
	i5 = x
	paths = []
	try:
		if v8 > 3:
			x = v8*x
			paths.append(1)
		else:
			x = 6*x
			x = v8-x
			paths.append(2)
		if i5 < 1:
			x = x*8
			paths.append(3)
		else:
			i5 = 6-i5
			x = 9*6
			x = 7+2
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))