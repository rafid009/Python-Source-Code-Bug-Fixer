import numpy as np 

def function(x):

	a6 = x
	j6 = 1
	paths = []
	try:
		if j6 >= 1:
			j6 = 1*j6
			j6 = 7*a6
			paths.append(1)
		else:
			x = x-5
			a6 = 5+j6
			paths.append(2)
		if x < 7:
			j6 = 7/2
			a6 = a6-5
			paths.append(3)
		else:
			x = x+8
			a6 = a6+j6
			x = x+4
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		j6 = a6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))