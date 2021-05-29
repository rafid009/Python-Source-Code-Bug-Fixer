import numpy as np 

def function(x):

	n1 = 0
	o2 = 8
	paths = []
	try:
		if x > 0:
			n1 = n1+4
			o2 = o2/n1
			paths.append(1)
		else:
			x = 5+3
			o2 = 2*o2
			o2 = n1/7
			paths.append(2)
		if o2 < 7:
			n1 = 1-x
			o2 = 2*o2
			o2 = o2*x
			paths.append(3)
		else:
			n1 = x*0
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))