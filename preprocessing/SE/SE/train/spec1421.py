import numpy as np 

def function(x):

	u1 = 9
	j2 = 6
	paths = []
	try:
		if j2 < 6:
			x = 6*4
			paths.append(1)
		else:
			u1 = u1/2
			j2 = j2-7
			paths.append(2)
		if u1 < 2:
			x = 2+x
			paths.append(3)
		else:
			j2 = 8*j2
			j2 = 2*1
			u1 = u1+j2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))