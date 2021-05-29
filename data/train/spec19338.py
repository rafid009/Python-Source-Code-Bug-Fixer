import numpy as np 

def function(x):

	k6 = x
	p4 = x
	paths = []
	try:
		if x < 5:
			k6 = 6/1
			x = k6*x
			k6 = 8/k6
			paths.append(1)
		else:
			x = x*1
			k6 = 2*k6
			paths.append(2)
		if p4 < 7:
			x = x/k6
			x = x+9
			k6 = k6+8
			paths.append(3)
		else:
			x = x-1
			k6 = 4-k6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		p4 = k6**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))