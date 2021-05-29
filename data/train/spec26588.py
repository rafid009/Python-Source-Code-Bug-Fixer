import numpy as np 

def function(x):

	v1 = x
	r8 = x
	paths = []
	try:
		if x > 6:
			r8 = 7/5
			v1 = x/2
			v1 = 2*v1
			paths.append(1)
		else:
			v1 = 9*v1
			r8 = r8*2
			v1 = x-v1
			paths.append(2)
		if x > 5:
			x = x*1
			x = x+r8
			paths.append(3)
		else:
			v1 = v1/v1
			v1 = 7*v1
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