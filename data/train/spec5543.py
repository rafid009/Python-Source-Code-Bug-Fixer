import numpy as np 

def function(x):

	h5 = x
	j9 = x
	paths = []
	try:
		if x < 0:
			h5 = 1*h5
			x = x-0
			paths.append(1)
		else:
			x = 9*j9
			paths.append(2)
		if x < 3:
			j9 = j9+5
			x = x*0
			paths.append(3)
		else:
			h5 = 5*0
			j9 = j9*x
			h5 = 5*h5
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))