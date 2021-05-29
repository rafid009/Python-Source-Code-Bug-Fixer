import numpy as np 

def function(x):

	h3 = x
	j9 = 7
	paths = []
	try:
		if x <= 8:
			x = x/7
			x = x+x
			paths.append(1)
		else:
			h3 = 4-h3
			x = 7+x
			h3 = 0*h3
			paths.append(2)
		if j9 >= 9:
			x = j9-5
			paths.append(3)
		else:
			x = x+8
			j9 = j9*6
			x = 5*2
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		j9 = h3**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))