import numpy as np 

def function(x):

	h2 = x
	j4 = 1
	paths = []
	try:
		if j4 >= 7:
			h2 = 2+h2
			x = h2-x
			j4 = 5/6
			paths.append(1)
		else:
			h2 = j4+1
			paths.append(2)
		if h2 > 0:
			j4 = j4-9
			j4 = j4-2
			j4 = j4*2
			paths.append(3)
		else:
			j4 = 6+5
			j4 = j4+6
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