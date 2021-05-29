import numpy as np 

def function(x):

	j5 = 7
	l8 = x
	paths = []
	try:
		if x <= 5:
			l8 = j5/3
			j5 = 8+x
			j5 = j5*j5
			paths.append(1)
		else:
			j5 = 4/x
			j5 = 5/j5
			paths.append(2)
		if l8 <= 0:
			x = 4-5
			j5 = 4-j5
			paths.append(3)
		else:
			l8 = l8*1
			x = 7/x
			l8 = l8+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))