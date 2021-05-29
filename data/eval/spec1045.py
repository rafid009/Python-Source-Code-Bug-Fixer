import numpy as np 

def function(x):

	i8 = x
	j3 = 3
	paths = []
	try:
		if j3 > 4:
			x = 6+x
			paths.append(1)
		else:
			x = x/4
			j3 = j3*9
			paths.append(2)
		if x < 0:
			i8 = 3-7
			paths.append(3)
		else:
			x = 7-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))