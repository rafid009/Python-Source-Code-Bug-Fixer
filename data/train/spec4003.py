import numpy as np 

def function(x):

	i7 = x
	r7 = x
	paths = []
	try:
		if i7 > 7:
			r7 = 6/r7
			i7 = i7*1
			paths.append(1)
		else:
			r7 = i7+r7
			r7 = 9+r7
			paths.append(2)
		if r7 > 3:
			r7 = r7/r7
			i7 = 3*i7
			paths.append(3)
		else:
			x = 2+x
			r7 = r7*9
			r7 = r7/r7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))