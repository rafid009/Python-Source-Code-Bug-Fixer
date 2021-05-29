import numpy as np 

def function(x):

	j3 = x
	h6 = 4
	paths = []
	try:
		if h6 > 7:
			x = x*4
			j3 = j3+0
			h6 = 7+h6
			paths.append(1)
		else:
			x = x*h6
			j3 = j3*x
			j3 = 6-j3
			paths.append(2)
		if x >= 7:
			h6 = 8-h6
			h6 = h6+4
			x = 8/x
			paths.append(3)
		else:
			h6 = x-2
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