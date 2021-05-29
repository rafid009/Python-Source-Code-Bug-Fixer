import numpy as np 

def function(x):

	o0 = 6
	v1 = x
	x = 7
	paths = []
	try:
		if x > 5:
			o0 = 2-8
			paths.append(1)
		else:
			o0 = o0*o0
			o0 = 4+o0
			paths.append(2)
		if x > 4:
			x = x/x
			v1 = v1+5
			x = x+5
			paths.append(3)
		else:
			v1 = v1+o0
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))