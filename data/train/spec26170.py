import numpy as np 

def function(x):

	j4 = x
	u3 = x
	x = x
	paths = []
	try:
		if x < 4:
			u3 = 0+8
			j4 = 9/j4
			paths.append(1)
		else:
			u3 = j4/u3
			paths.append(2)
		if u3 > 2:
			u3 = j4/u3
			j4 = j4+1
			x = 4+x
			paths.append(3)
		else:
			x = 6-u3
			j4 = j4-8
			x = x-2
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