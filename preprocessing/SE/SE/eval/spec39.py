import numpy as np 

def function(x):

	i1 = 1
	i8 = x
	paths = []
	try:
		if i1 <= 8:
			i8 = 7*i8
			i1 = i1*3
			paths.append(1)
		else:
			i1 = x+i1
			paths.append(2)
		if x > 7:
			x = 3-i1
			i8 = x+1
			paths.append(3)
		else:
			x = 7/x
			x = x+0
			i1 = i1*x
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i8 = i1**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))