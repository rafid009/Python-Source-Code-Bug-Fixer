import numpy as np 

def function(x):

	j6 = x
	a5 = 3
	paths = []
	try:
		if j6 < 2:
			a5 = 3-1
			j6 = 4+j6
			a5 = 7*x
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if j6 < 3:
			x = a5-9
			x = 6+3
			a5 = x*a5
			paths.append(3)
		else:
			x = a5*x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		j6 = a5**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))