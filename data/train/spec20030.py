import numpy as np 

def function(x):

	n2 = x
	u3 = 7
	paths = []
	try:
		if n2 < 0:
			x = x+8
			x = n2+1
			paths.append(1)
		else:
			x = x*7
			n2 = n2-3
			n2 = 2*7
			paths.append(2)
		if x > 2:
			u3 = u3+9
			paths.append(3)
		else:
			u3 = u3*7
			x = u3*x
			n2 = n2+5
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))