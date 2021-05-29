import numpy as np 

def function(x):

	k6 = x
	r6 = 8
	paths = []
	try:
		if r6 <= 6:
			x = 1*x
			paths.append(1)
		else:
			x = x*x
			k6 = k6+3
			r6 = r6+5
			paths.append(2)
		if k6 <= 3:
			r6 = 2*r6
			r6 = 2-r6
			paths.append(3)
		else:
			k6 = 4/3
			r6 = r6-r6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		k6 = r6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))