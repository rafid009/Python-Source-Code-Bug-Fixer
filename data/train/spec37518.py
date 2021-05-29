import numpy as np 

def function(x):

	n6 = 6
	j7 = x
	paths = []
	try:
		if n6 > 9:
			n6 = x*1
			paths.append(1)
		else:
			j7 = j7+2
			n6 = 5-n6
			n6 = n6*5
			paths.append(2)
		if x <= 5:
			x = x+x
			paths.append(3)
		else:
			x = 2-5
			n6 = 9-x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))