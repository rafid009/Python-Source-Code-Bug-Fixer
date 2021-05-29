import numpy as np 

def function(x):

	v1 = 9
	r2 = x
	paths = []
	try:
		if v1 <= 8:
			x = v1*5
			v1 = 1+3
			r2 = x+x
			paths.append(1)
		else:
			v1 = 0-0
			v1 = r2/x
			r2 = r2*x
			paths.append(2)
		if x < 7:
			r2 = r2*x
			v1 = x/4
			paths.append(3)
		else:
			x = r2+3
			r2 = 4+8
			x = x*1
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		v1 = r2**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))