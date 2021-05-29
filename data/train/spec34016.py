import numpy as np 

def function(x):

	r4 = 6
	j9 = 6
	paths = []
	try:
		if r4 >= 9:
			x = j9*3
			r4 = 9*r4
			paths.append(1)
		else:
			j9 = j9*j9
			j9 = x/6
			j9 = j9+x
			paths.append(2)
		if x > 9:
			j9 = 4-j9
			paths.append(3)
		else:
			r4 = x+r4
			x = 1/x
			j9 = 0-j9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))