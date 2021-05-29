import numpy as np 

def function(x):

	j2 = 0
	h4 = 6
	paths = []
	try:
		if j2 > 9:
			h4 = x-h4
			h4 = j2/h4
			j2 = j2+0
			paths.append(1)
		else:
			j2 = j2/7
			j2 = j2+6
			h4 = x/2
			paths.append(2)
		if x < 7:
			h4 = h4*9
			x = 1-2
			paths.append(3)
		else:
			j2 = h4+8
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		j2 = h4**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))