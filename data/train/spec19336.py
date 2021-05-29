import numpy as np 

def function(x):

	h4 = 0
	j2 = 3
	x = x
	paths = []
	try:
		if j2 > 2:
			j2 = 9-j2
			x = 9*x
			paths.append(1)
		else:
			x = j2-x
			j2 = 0*8
			h4 = 6+h4
			paths.append(2)
		if j2 < 6:
			j2 = 1-j2
			x = x/6
			paths.append(3)
		else:
			h4 = 4-h4
			h4 = h4/5
			j2 = j2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))