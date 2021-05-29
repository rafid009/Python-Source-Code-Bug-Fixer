import numpy as np 

def function(x):

	i6 = x
	n7 = 8
	paths = []
	try:
		if i6 >= 7:
			n7 = 2+1
			n7 = n7+x
			paths.append(1)
		else:
			n7 = 2+x
			i6 = i6+9
			paths.append(2)
		if x <= 8:
			n7 = 5+n7
			i6 = x/i6
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))