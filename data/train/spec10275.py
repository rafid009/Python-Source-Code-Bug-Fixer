import numpy as np 

def function(x):

	j6 = 2
	f7 = 4
	paths = []
	try:
		if j6 <= 3:
			j6 = 1+j6
			x = x/f7
			paths.append(1)
		else:
			f7 = 2-j6
			paths.append(2)
		if f7 <= 1:
			x = 1/9
			paths.append(3)
		else:
			j6 = x-j6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))