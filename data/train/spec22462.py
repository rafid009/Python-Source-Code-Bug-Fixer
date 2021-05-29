import numpy as np 

def function(x):

	o0 = x
	j3 = x
	paths = []
	try:
		if o0 < 9:
			o0 = o0-1
			j3 = j3/6
			x = x/9
			paths.append(1)
		else:
			o0 = 9/o0
			o0 = 1*o0
			x = 9+0
			paths.append(2)
		if o0 > 8:
			j3 = 1+j3
			j3 = 7+6
			o0 = x+o0
			paths.append(3)
		else:
			j3 = j3-5
			j3 = 9-j3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))