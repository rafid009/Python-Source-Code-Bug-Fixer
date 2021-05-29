import numpy as np 

def function(x):

	n0 = 5
	j3 = x
	paths = []
	try:
		if n0 > 5:
			x = 7/n0
			n0 = j3*j3
			x = x/x
			paths.append(1)
		else:
			j3 = 1-5
			j3 = j3/3
			paths.append(2)
		if n0 > 9:
			j3 = j3*6
			n0 = 1-x
			j3 = j3+5
			paths.append(3)
		else:
			n0 = x+2
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