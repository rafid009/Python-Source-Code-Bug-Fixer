import numpy as np 

def function(x):

	h9 = x
	j3 = x
	x = 6
	paths = []
	try:
		if j3 >= 3:
			x = 4+0
			j3 = 9/2
			paths.append(1)
		else:
			j3 = j3/3
			paths.append(2)
		if h9 >= 5:
			h9 = 7/x
			paths.append(3)
		else:
			x = 8*x
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		j3 = h9**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))