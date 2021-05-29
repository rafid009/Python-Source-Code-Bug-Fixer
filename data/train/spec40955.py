import numpy as np 

def function(x):

	r5 = 5
	o3 = 9
	paths = []
	try:
		if x < 9:
			r5 = 7*o3
			x = x*2
			paths.append(1)
		else:
			x = 5-x
			r5 = r5+x
			paths.append(2)
		if r5 >= 5:
			x = x/5
			paths.append(3)
		else:
			x = x*2
			r5 = 0-0
			o3 = x+o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))