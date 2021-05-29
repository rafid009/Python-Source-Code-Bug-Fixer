import numpy as np 

def function(x):

	v8 = x
	i1 = 4
	x = x
	paths = []
	try:
		if i1 >= 9:
			x = 8-x
			x = x+8
			paths.append(1)
		else:
			x = x/7
			v8 = v8-i1
			x = x+1
			paths.append(2)
		if i1 >= 5:
			v8 = v8+v8
			v8 = 6-4
			paths.append(3)
		else:
			i1 = i1-8
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		v8 = i1**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))