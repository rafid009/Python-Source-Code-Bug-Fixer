import numpy as np 

def function(x):

	n2 = 1
	j5 = 7
	paths = []
	try:
		if x < 9:
			x = 8+x
			paths.append(1)
		else:
			x = 6*x
			j5 = j5/5
			paths.append(2)
		if j5 >= 8:
			n2 = n2/9
			j5 = 3+n2
			x = x-1
			paths.append(3)
		else:
			j5 = n2-4
			x = 2+x
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))