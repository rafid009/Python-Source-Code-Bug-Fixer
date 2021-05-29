import numpy as np 

def function(x):

	r6 = 0
	v9 = x
	paths = []
	try:
		if r6 >= 9:
			r6 = 0+r6
			x = x*4
			paths.append(1)
		else:
			r6 = x*4
			paths.append(2)
		if x <= 7:
			v9 = v9-8
			v9 = v9-6
			paths.append(3)
		else:
			v9 = r6*6
			x = x+x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))