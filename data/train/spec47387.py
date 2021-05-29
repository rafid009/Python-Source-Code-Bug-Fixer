import numpy as np 

def function(x):

	p4 = 5
	n5 = x
	paths = []
	try:
		if p4 > 9:
			p4 = 8-8
			paths.append(1)
		else:
			n5 = n5*2
			p4 = 3/x
			paths.append(2)
		if x <= 8:
			n5 = n5-2
			x = x+1
			n5 = 1-7
			paths.append(3)
		else:
			p4 = x/3
			n5 = n5-n5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))