import numpy as np 

def function(x):

	n4 = 7
	k6 = x
	paths = []
	try:
		if k6 < 8:
			n4 = n4*1
			n4 = n4+4
			x = 9*x
			paths.append(1)
		else:
			n4 = x+x
			paths.append(2)
		if k6 < 4:
			k6 = 3+k6
			x = n4-k6
			k6 = 5*k6
			paths.append(3)
		else:
			k6 = 2*k6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		n4 = k6**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))