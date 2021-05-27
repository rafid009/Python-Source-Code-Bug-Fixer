import numpy as np 

def function(x):

	i0 = 0
	j2 = x
	paths = []
	try:
		if x <= 3:
			x = i0+1
			x = i0-7
			paths.append(1)
		else:
			j2 = 1+j2
			i0 = x-8
			x = x-i0
			paths.append(2)
		if x >= 6:
			j2 = j2*2
			paths.append(3)
		else:
			j2 = j2-x
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