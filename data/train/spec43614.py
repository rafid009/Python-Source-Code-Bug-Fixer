import numpy as np 

def function(x):

	j1 = x
	n0 = 6
	x = 6
	paths = []
	try:
		if x <= 1:
			x = j1-n0
			x = x*0
			x = j1*7
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if j1 > 4:
			n0 = j1-5
			paths.append(3)
		else:
			j1 = 3*j1
			n0 = n0/3
			n0 = n0*2
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))