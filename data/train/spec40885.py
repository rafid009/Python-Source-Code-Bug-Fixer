import numpy as np 

def function(x):

	v1 = 6
	i6 = x
	paths = []
	try:
		if i6 > 9:
			v1 = v1*4
			v1 = v1+4
			v1 = i6+v1
			paths.append(1)
		else:
			x = 1-4
			paths.append(2)
		if x <= 2:
			x = x+5
			paths.append(3)
		else:
			v1 = v1/x
			v1 = v1/3
			i6 = 7+i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))