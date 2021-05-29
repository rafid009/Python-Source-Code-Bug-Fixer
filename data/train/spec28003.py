import numpy as np 

def function(x):

	i4 = 4
	j2 = x
	paths = []
	try:
		if x < 9:
			i4 = i4/6
			j2 = j2-j2
			paths.append(1)
		else:
			j2 = 9-j2
			paths.append(2)
		if j2 <= 7:
			x = 0*4
			paths.append(3)
		else:
			i4 = 5+i4
			i4 = 1/7
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))