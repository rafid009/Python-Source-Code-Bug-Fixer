import numpy as np 

def function(x):

	x4 = 7
	j7 = x
	paths = []
	try:
		if x4 < 5:
			x4 = x4+9
			paths.append(1)
		else:
			x4 = 7*3
			paths.append(2)
		if j7 <= 4:
			x4 = x4+x
			j7 = j7/9
			x = j7+0
			paths.append(3)
		else:
			x = x4+x
			j7 = 7-1
			j7 = j7+j7
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