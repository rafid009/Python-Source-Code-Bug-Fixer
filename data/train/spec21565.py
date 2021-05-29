import numpy as np 

def function(x):

	x1 = x
	j5 = 1
	paths = []
	try:
		if x1 <= 1:
			j5 = j5/5
			j5 = x*j5
			j5 = x-j5
			paths.append(1)
		else:
			j5 = 3+2
			x = x1-4
			x1 = 3+x1
			paths.append(2)
		if j5 >= 8:
			x1 = 4*9
			x = 4+4
			paths.append(3)
		else:
			j5 = j5+j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x1 = j5**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))