import numpy as np 

def function(x):

	a6 = x
	o0 = x
	paths = []
	try:
		if x < 3:
			x = x+x
			o0 = o0+0
			o0 = o0+1
			paths.append(1)
		else:
			o0 = o0-8
			x = a6-x
			o0 = o0/o0
			paths.append(2)
		if o0 < 4:
			o0 = o0+5
			a6 = a6-0
			paths.append(3)
		else:
			x = 3*o0
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))