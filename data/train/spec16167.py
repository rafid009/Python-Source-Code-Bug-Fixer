import numpy as np 

def function(x):

	v4 = 7
	r7 = 7
	paths = []
	try:
		if v4 >= 1:
			v4 = x*4
			x = 1-v4
			paths.append(1)
		else:
			r7 = r7*x
			r7 = r7+4
			v4 = 5+r7
			paths.append(2)
		if v4 < 6:
			v4 = 7/v4
			x = x*8
			r7 = r7*0
			paths.append(3)
		else:
			r7 = r7*r7
			x = 0-x
			r7 = 3*6
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		r7 = v4**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))