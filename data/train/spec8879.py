import numpy as np 

def function(x):

	r8 = x
	j8 = x
	paths = []
	try:
		if x > 0:
			j8 = j8+x
			r8 = 9+x
			j8 = x+0
			paths.append(1)
		else:
			j8 = x+j8
			r8 = r8*8
			x = x+8
			paths.append(2)
		if x > 0:
			j8 = 5+j8
			paths.append(3)
		else:
			j8 = x-r8
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))