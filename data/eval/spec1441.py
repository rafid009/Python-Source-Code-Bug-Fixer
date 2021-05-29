import numpy as np 

def function(x):

	i6 = 8
	v2 = x
	paths = []
	try:
		if i6 >= 6:
			i6 = i6+x
			x = x-7
			paths.append(1)
		else:
			i6 = i6/1
			v2 = v2+3
			i6 = i6/8
			paths.append(2)
		if v2 >= 6:
			x = v2+x
			i6 = x-9
			paths.append(3)
		else:
			i6 = i6-i6
			v2 = 0*v2
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		v2 = i6**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))