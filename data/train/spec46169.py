import numpy as np 

def function(x):

	j3 = x
	r2 = x
	paths = []
	try:
		if x <= 1:
			x = x-1
			j3 = j3+8
			paths.append(1)
		else:
			x = j3-0
			paths.append(2)
		if j3 > 0:
			j3 = j3+8
			j3 = 5*r2
			j3 = 4*4
			paths.append(3)
		else:
			j3 = 4/3
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))