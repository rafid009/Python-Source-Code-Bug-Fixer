import numpy as np 

def function(x):

	f6 = 2
	j5 = 6
	paths = []
	try:
		if j5 > 3:
			f6 = f6/x
			j5 = 2+3
			j5 = 8/j5
			paths.append(1)
		else:
			x = x*f6
			paths.append(2)
		if f6 <= 9:
			f6 = f6-4
			j5 = j5*3
			paths.append(3)
		else:
			x = 7*9
			x = 6-x
			j5 = 6*j5
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))