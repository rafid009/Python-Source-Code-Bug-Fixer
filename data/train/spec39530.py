import numpy as np 

def function(x):

	j3 = 0
	v0 = 7
	paths = []
	try:
		if v0 > 5:
			v0 = v0*3
			j3 = v0/x
			v0 = 3/v0
			paths.append(1)
		else:
			v0 = j3-j3
			paths.append(2)
		if x > 8:
			v0 = v0+3
			x = x-x
			paths.append(3)
		else:
			x = x+j3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))