import numpy as np 

def function(x):

	j3 = 4
	n8 = 7
	paths = []
	try:
		if x >= 0:
			j3 = 1+j3
			j3 = j3-6
			paths.append(1)
		else:
			j3 = n8*x
			paths.append(2)
		if n8 < 1:
			x = x/n8
			x = j3+4
			x = x-8
			paths.append(3)
		else:
			n8 = n8-9
			n8 = x-3
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		j3 = n8**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))