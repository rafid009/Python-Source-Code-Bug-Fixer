import numpy as np 

def function(x):

	r0 = 3
	o6 = 2
	paths = []
	try:
		if x < 8:
			o6 = o6+6
			paths.append(1)
		else:
			r0 = r0*1
			r0 = o6+r0
			r0 = r0/9
			paths.append(2)
		if r0 >= 1:
			r0 = r0*o6
			o6 = o6*7
			paths.append(3)
		else:
			r0 = x-o6
			o6 = o6-8
			r0 = 4+5
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		r0 = o6**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))