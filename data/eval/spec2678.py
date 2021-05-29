import numpy as np 

def function(x):

	u3 = x
	n1 = 2
	paths = []
	try:
		if n1 >= 5:
			x = 0*8
			paths.append(1)
		else:
			x = 5/x
			n1 = n1*5
			paths.append(2)
		if n1 <= 0:
			x = n1/n1
			n1 = n1+7
			paths.append(3)
		else:
			n1 = 7+n1
			n1 = 2*1
			x = x*3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		n1 = u3**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))