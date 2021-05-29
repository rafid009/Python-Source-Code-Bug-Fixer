import numpy as np 

def function(x):

	d5 = 0
	r2 = x
	paths = []
	try:
		if x > 4:
			x = 6+x
			paths.append(1)
		else:
			r2 = r2*5
			x = r2*x
			r2 = 1*2
			paths.append(2)
		if x < 5:
			d5 = 9+3
			x = r2-7
			paths.append(3)
		else:
			x = 1/x
			r2 = 4-r2
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))