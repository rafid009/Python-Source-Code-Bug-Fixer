import numpy as np 

def function(x):

	e0 = x
	n2 = x
	paths = []
	try:
		if e0 < 2:
			x = 4-x
			n2 = n2/n2
			paths.append(1)
		else:
			n2 = n2-7
			e0 = n2*e0
			n2 = 9-n2
			paths.append(2)
		if n2 <= 4:
			n2 = n2*8
			x = n2+x
			paths.append(3)
		else:
			e0 = n2/3
			x = e0*9
			n2 = x*n2
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		n2 = e0**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))