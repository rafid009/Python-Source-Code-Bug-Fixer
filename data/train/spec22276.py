import numpy as np 

def function(x):

	n2 = x
	u3 = x
	paths = []
	try:
		if u3 >= 7:
			n2 = u3-u3
			paths.append(1)
		else:
			x = 7/x
			n2 = n2*1
			paths.append(2)
		if x <= 7:
			n2 = u3/4
			paths.append(3)
		else:
			u3 = u3/7
			x = 1-u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		n2 = u3**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))