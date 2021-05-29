import numpy as np 

def function(x):

	i0 = 1
	j3 = x
	x = x
	paths = []
	try:
		if j3 < 8:
			x = 6/6
			paths.append(1)
		else:
			j3 = x*3
			paths.append(2)
		if i0 >= 2:
			x = x/7
			j3 = j3+3
			paths.append(3)
		else:
			x = 4-2
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))