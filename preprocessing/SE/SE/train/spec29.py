import numpy as np 

def function(x):

	r6 = 4
	f8 = x
	paths = []
	try:
		if x < 4:
			x = 0/r6
			r6 = r6/4
			paths.append(1)
		else:
			x = 5-7
			r6 = r6+0
			paths.append(2)
		if f8 < 9:
			r6 = r6*3
			r6 = r6*5
			r6 = r6+f8
			paths.append(3)
		else:
			r6 = 6-r6
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