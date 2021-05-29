import numpy as np 

def function(x):

	j9 = 4
	r6 = 5
	paths = []
	try:
		if r6 >= 6:
			j9 = 4+j9
			j9 = 7-j9
			paths.append(1)
		else:
			x = x*9
			r6 = 3*r6
			r6 = r6-8
			paths.append(2)
		if x >= 6:
			x = x*8
			r6 = r6/r6
			j9 = 0*x
			paths.append(3)
		else:
			r6 = r6*8
			j9 = j9-9
			r6 = r6+5
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