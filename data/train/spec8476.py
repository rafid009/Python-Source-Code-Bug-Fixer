import numpy as np 

def function(x):

	h0 = x
	j6 = 6
	paths = []
	try:
		if x < 1:
			x = h0*x
			paths.append(1)
		else:
			j6 = j6+7
			j6 = j6*x
			j6 = 4*8
			paths.append(2)
		if x > 9:
			x = x/7
			paths.append(3)
		else:
			h0 = j6*h0
			x = 3/h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		j6 = h0**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))