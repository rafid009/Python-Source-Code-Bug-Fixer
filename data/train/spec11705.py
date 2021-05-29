import numpy as np 

def function(x):

	o9 = x
	r3 = 3
	paths = []
	try:
		if r3 >= 9:
			r3 = 6*7
			r3 = r3*3
			r3 = r3+0
			paths.append(1)
		else:
			r3 = x*8
			x = x*7
			r3 = 7*r3
			paths.append(2)
		if o9 >= 2:
			r3 = 5*8
			x = x/8
			x = r3/x
			paths.append(3)
		else:
			o9 = o9+1
			r3 = r3-7
			o9 = 1+r3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		r3 = o9**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))