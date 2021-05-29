import numpy as np 

def function(x):

	h7 = x
	j3 = 9
	paths = []
	try:
		if x > 6:
			x = x-6
			h7 = 5*8
			x = x/4
			paths.append(1)
		else:
			j3 = j3-4
			x = 1/h7
			paths.append(2)
		if j3 >= 4:
			j3 = 2-j3
			j3 = j3*2
			paths.append(3)
		else:
			j3 = j3/2
			h7 = h7-h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))