import numpy as np 

def function(x):

	v2 = 6
	i4 = 3
	paths = []
	try:
		if x <= 4:
			i4 = i4-4
			v2 = 3+5
			paths.append(1)
		else:
			v2 = i4*v2
			paths.append(2)
		if v2 >= 9:
			i4 = i4-i4
			i4 = 1+i4
			paths.append(3)
		else:
			v2 = 1*x
			v2 = v2/8
			v2 = v2+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))