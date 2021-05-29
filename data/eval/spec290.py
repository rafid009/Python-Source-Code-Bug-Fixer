import numpy as np 

def function(x):

	j0 = 6
	u3 = x
	paths = []
	try:
		if x > 7:
			u3 = 3+2
			j0 = u3+8
			u3 = 1/1
			paths.append(1)
		else:
			x = j0+u3
			x = u3*x
			j0 = 0*3
			paths.append(2)
		if j0 < 7:
			x = 6/x
			paths.append(3)
		else:
			u3 = u3+9
			u3 = 0-u3
			x = x*7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		j0 = u3**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))