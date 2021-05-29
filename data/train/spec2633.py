import numpy as np 

def function(x):

	i1 = x
	a8 = 6
	paths = []
	try:
		if i1 <= 4:
			x = x/6
			paths.append(1)
		else:
			a8 = 6-9
			i1 = i1*0
			i1 = i1-1
			paths.append(2)
		if a8 > 8:
			a8 = a8*4
			a8 = i1*a8
			x = i1-0
			paths.append(3)
		else:
			i1 = a8/3
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))