import numpy as np 

def function(x):

	v7 = 3
	r8 = x
	paths = []
	try:
		if v7 >= 5:
			x = v7-0
			x = x/7
			x = x+x
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if v7 >= 6:
			r8 = x-r8
			paths.append(3)
		else:
			r8 = r8-x
			v7 = 0*5
			v7 = v7-8
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		r8 = v7**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))