import numpy as np 

def function(x):

	o0 = x
	j2 = x
	paths = []
	try:
		if o0 >= 0:
			j2 = j2*5
			x = x/2
			j2 = o0-x
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if x < 4:
			x = x+3
			j2 = 4*j2
			j2 = j2+9
			paths.append(3)
		else:
			o0 = o0/x
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))