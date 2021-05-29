import numpy as np 

def function(x):

	j6 = x
	b8 = x
	x = x
	paths = []
	try:
		if b8 < 9:
			b8 = 2/b8
			j6 = j6*x
			x = x/3
			paths.append(1)
		else:
			j6 = x*8
			b8 = 0-2
			j6 = 8*j6
			paths.append(2)
		if b8 >= 8:
			x = x-1
			paths.append(3)
		else:
			j6 = j6-x
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