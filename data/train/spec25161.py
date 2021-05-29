import numpy as np 

def function(x):

	i7 = x
	n9 = x
	paths = []
	try:
		if n9 <= 1:
			n9 = n9*7
			paths.append(1)
		else:
			n9 = n9*1
			n9 = n9-5
			paths.append(2)
		if x >= 5:
			x = x+n9
			i7 = 3*i7
			i7 = i7/5
			paths.append(3)
		else:
			n9 = i7-3
			i7 = 2-i7
			i7 = i7*x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		i7 = n9**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))