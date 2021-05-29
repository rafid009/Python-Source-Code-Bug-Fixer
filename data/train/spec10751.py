import numpy as np 

def function(x):

	o0 = 7
	j9 = 7
	paths = []
	try:
		if x < 0:
			j9 = j9/4
			o0 = j9-o0
			x = 7/x
			paths.append(1)
		else:
			x = 7+j9
			j9 = x-x
			paths.append(2)
		if o0 < 0:
			x = x*4
			j9 = x+j9
			paths.append(3)
		else:
			x = 6*3
			o0 = o0*1
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))