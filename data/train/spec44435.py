import numpy as np 

def function(x):

	o0 = 8
	j3 = 2
	paths = []
	try:
		if x <= 0:
			o0 = 5+o0
			o0 = o0*o0
			o0 = o0/j3
			paths.append(1)
		else:
			j3 = j3-0
			o0 = o0*x
			j3 = j3/6
			paths.append(2)
		if o0 > 1:
			j3 = j3-5
			j3 = 1+j3
			x = x+2
			paths.append(3)
		else:
			j3 = 2/j3
			o0 = 3-o0
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))