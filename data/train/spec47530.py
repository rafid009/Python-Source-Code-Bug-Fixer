import numpy as np 

def function(x):

	r0 = x
	k6 = 7
	paths = []
	try:
		if r0 > 3:
			x = r0*k6
			x = x-r0
			x = 6-9
			paths.append(1)
		else:
			r0 = r0+7
			paths.append(2)
		if k6 > 7:
			r0 = k6*r0
			paths.append(3)
		else:
			x = r0+x
			k6 = k6/5
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		k6 = r0**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))