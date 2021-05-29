import numpy as np 

def function(x):

	r5 = 7
	v2 = x
	paths = []
	try:
		if x <= 6:
			r5 = 2-r5
			x = x+5
			x = x*x
			paths.append(1)
		else:
			r5 = 9/7
			paths.append(2)
		if r5 < 3:
			x = x+2
			r5 = v2-x
			r5 = x+5
			paths.append(3)
		else:
			v2 = 8/x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))