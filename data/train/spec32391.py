import numpy as np 

def function(x):

	s4 = x
	n2 = 3
	x = x
	paths = []
	try:
		if n2 >= 8:
			n2 = n2+s4
			x = x+s4
			x = 3*2
			paths.append(1)
		else:
			n2 = s4*8
			s4 = n2/s4
			s4 = x-8
			paths.append(2)
		if n2 < 4:
			n2 = n2/n2
			paths.append(3)
		else:
			n2 = 3-n2
			x = x/1
			n2 = n2+s4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))