import numpy as np 

def function(x):

	j4 = 9
	f9 = x
	paths = []
	try:
		if j4 >= 5:
			x = 1/f9
			f9 = 2-f9
			paths.append(1)
		else:
			j4 = f9+j4
			paths.append(2)
		if x < 9:
			x = 4+f9
			f9 = f9+6
			paths.append(3)
		else:
			j4 = 2*j4
			f9 = 4-f9
			f9 = f9*x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		j4 = f9**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))