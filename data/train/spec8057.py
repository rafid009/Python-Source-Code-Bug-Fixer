import numpy as np 

def function(x):

	r3 = x
	n9 = x
	paths = []
	try:
		if r3 <= 3:
			n9 = 8-5
			x = 4-8
			n9 = x/n9
			paths.append(1)
		else:
			x = 8+x
			r3 = 0/n9
			paths.append(2)
		if n9 > 2:
			r3 = r3/6
			paths.append(3)
		else:
			n9 = r3-n9
			r3 = 0*n9
			n9 = 5-7
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))