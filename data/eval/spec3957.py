import numpy as np 

def function(x):

	j2 = 5
	h3 = x
	paths = []
	try:
		if x >= 4:
			j2 = j2-6
			paths.append(1)
		else:
			h3 = h3/1
			x = x-3
			paths.append(2)
		if x > 8:
			x = j2+3
			h3 = 5+6
			paths.append(3)
		else:
			x = 3*j2
			j2 = 7/3
			h3 = x-h3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		j2 = h3**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))