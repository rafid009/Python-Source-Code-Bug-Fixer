import numpy as np 

def function(x):

	v4 = x
	n8 = 6
	paths = []
	try:
		if v4 > 8:
			v4 = n8+n8
			x = x-1
			paths.append(1)
		else:
			x = v4/7
			n8 = v4+9
			paths.append(2)
		if n8 <= 3:
			x = 5+x
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))