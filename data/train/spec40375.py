import numpy as np 

def function(x):

	n6 = 1
	j9 = x
	x = 8
	paths = []
	try:
		if n6 >= 9:
			j9 = 8-9
			n6 = n6-6
			j9 = 7*j9
			paths.append(1)
		else:
			n6 = n6-n6
			x = 1-1
			paths.append(2)
		if j9 < 4:
			j9 = j9+6
			x = x+6
			paths.append(3)
		else:
			n6 = 7/7
			j9 = j9*0
			x = 6/1
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