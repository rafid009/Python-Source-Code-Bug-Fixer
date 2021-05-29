import numpy as np 

def function(x):

	n5 = x
	j2 = 7
	paths = []
	try:
		if x < 1:
			x = 2+2
			j2 = j2+6
			n5 = n5/n5
			paths.append(1)
		else:
			n5 = x/7
			x = x-2
			x = 6/x
			paths.append(2)
		if n5 >= 8:
			n5 = 2+j2
			paths.append(3)
		else:
			n5 = 3+n5
			x = x*2
			n5 = 4-n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))