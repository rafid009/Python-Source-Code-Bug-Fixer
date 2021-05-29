import numpy as np 

def function(x):

	j5 = x
	w6 = 8
	paths = []
	try:
		if j5 >= 6:
			w6 = w6*9
			paths.append(1)
		else:
			w6 = 8+j5
			paths.append(2)
		if j5 < 8:
			x = x*6
			w6 = 5*w6
			paths.append(3)
		else:
			w6 = w6*8
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		j5 = w6**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))