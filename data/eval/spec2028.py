import numpy as np 

def function(x):

	o5 = x
	r8 = 3
	paths = []
	try:
		if r8 >= 6:
			o5 = 1-o5
			o5 = 1/9
			paths.append(1)
		else:
			r8 = r8*o5
			o5 = o5-9
			x = x*7
			paths.append(2)
		if r8 >= 2:
			r8 = r8+x
			r8 = o5*8
			x = 3-x
			paths.append(3)
		else:
			o5 = 9-o5
			o5 = o5-9
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))