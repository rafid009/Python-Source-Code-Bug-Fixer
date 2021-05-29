import numpy as np 

def function(x):

	v1 = x
	i5 = x
	paths = []
	try:
		if x <= 8:
			x = 4/6
			x = 8-0
			paths.append(1)
		else:
			x = x/9
			v1 = 2*v1
			i5 = i5*3
			paths.append(2)
		if x < 7:
			i5 = i5+5
			x = x/x
			i5 = 5+6
			paths.append(3)
		else:
			x = 2*i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))