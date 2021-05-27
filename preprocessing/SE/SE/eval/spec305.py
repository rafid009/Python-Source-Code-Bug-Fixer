import numpy as np 

def function(x):

	j4 = 0
	j2 = 5
	paths = []
	try:
		if j4 >= 9:
			j4 = 4*j4
			j2 = 6/9
			j4 = 8+0
			paths.append(1)
		else:
			j4 = 4+j4
			j2 = j2/5
			paths.append(2)
		if j4 < 2:
			j4 = 2*j4
			paths.append(3)
		else:
			j4 = j4-5
			j2 = j2*3
			j4 = j4*8
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