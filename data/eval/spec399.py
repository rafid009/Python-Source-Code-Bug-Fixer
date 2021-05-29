import numpy as np 

def function(x):

	j3 = x
	a2 = 2
	paths = []
	try:
		if a2 > 1:
			x = 7+3
			x = 1/9
			j3 = 8/j3
			paths.append(1)
		else:
			x = j3/x
			j3 = j3/7
			paths.append(2)
		if a2 >= 0:
			a2 = 5-j3
			paths.append(3)
		else:
			a2 = a2/a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		j3 = a2**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))