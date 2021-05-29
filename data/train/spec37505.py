import numpy as np 

def function(x):

	u3 = x
	j6 = 1
	paths = []
	try:
		if j6 <= 8:
			j6 = 0+3
			paths.append(1)
		else:
			u3 = 8*u3
			x = x+6
			paths.append(2)
		if x >= 0:
			j6 = 2/x
			j6 = u3+j6
			paths.append(3)
		else:
			u3 = j6+9
			u3 = 9-u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		j6 = u3**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))