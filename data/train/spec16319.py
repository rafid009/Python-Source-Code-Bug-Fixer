import numpy as np 

def function(x):

	b4 = x
	j6 = 3
	paths = []
	try:
		if j6 < 3:
			j6 = j6+8
			j6 = b4+j6
			paths.append(1)
		else:
			j6 = j6-1
			j6 = 5*2
			paths.append(2)
		if j6 < 0:
			j6 = j6+0
			x = 0/x
			paths.append(3)
		else:
			b4 = 9-b4
			j6 = 3+j6
			b4 = b4-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))