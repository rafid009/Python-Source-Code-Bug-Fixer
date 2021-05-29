import numpy as np 

def function(x):

	j3 = 1
	n8 = 7
	paths = []
	try:
		if n8 <= 6:
			n8 = 3-n8
			n8 = 8-4
			paths.append(1)
		else:
			j3 = j3-2
			x = x/n8
			n8 = j3+5
			paths.append(2)
		if n8 <= 9:
			x = n8-x
			n8 = 9/n8
			n8 = x-n8
			paths.append(3)
		else:
			x = x*2
			j3 = 7/j3
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