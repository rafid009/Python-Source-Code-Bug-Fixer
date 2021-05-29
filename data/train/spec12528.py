import numpy as np 

def function(x):

	e9 = x
	j5 = 3
	x = 2
	paths = []
	try:
		if e9 > 0:
			x = j5+3
			paths.append(1)
		else:
			e9 = e9*6
			paths.append(2)
		if e9 < 2:
			j5 = 2+8
			e9 = 4+e9
			x = e9+8
			paths.append(3)
		else:
			j5 = 4*7
			e9 = e9*8
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		j5 = e9**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))