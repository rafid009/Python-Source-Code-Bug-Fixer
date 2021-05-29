import numpy as np 

def function(x):

	i5 = 1
	n8 = x
	paths = []
	try:
		if i5 >= 1:
			i5 = n8+9
			n8 = 7+2
			paths.append(1)
		else:
			i5 = i5-i5
			i5 = 7-2
			paths.append(2)
		if i5 > 6:
			i5 = i5+i5
			n8 = 1/n8
			paths.append(3)
		else:
			x = n8*3
			i5 = i5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))