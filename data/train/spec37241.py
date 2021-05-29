import numpy as np 

def function(x):

	j4 = x
	n8 = 5
	paths = []
	try:
		if x < 6:
			n8 = 7*4
			paths.append(1)
		else:
			x = x-4
			j4 = j4+j4
			paths.append(2)
		if j4 > 3:
			j4 = 0+5
			paths.append(3)
		else:
			x = 9+x
			n8 = n8+x
			x = x+7
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		n8 = j4**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))