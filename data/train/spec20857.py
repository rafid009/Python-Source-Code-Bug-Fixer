import numpy as np 

def function(x):

	o0 = x
	j4 = 8
	paths = []
	try:
		if x < 6:
			x = x-7
			paths.append(1)
		else:
			o0 = 1-9
			x = 9-0
			paths.append(2)
		if j4 >= 9:
			x = 8*0
			o0 = 9*0
			paths.append(3)
		else:
			j4 = j4/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))