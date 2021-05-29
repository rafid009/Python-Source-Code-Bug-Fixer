import numpy as np 

def function(x):

	j2 = 2
	i4 = x
	x = x
	paths = []
	try:
		if j2 <= 2:
			x = 4-7
			i4 = i4+i4
			paths.append(1)
		else:
			j2 = 1/i4
			paths.append(2)
		if j2 > 0:
			x = j2+x
			j2 = j2/3
			paths.append(3)
		else:
			j2 = j2/4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))