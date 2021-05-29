import numpy as np 

def function(x):

	n2 = x
	v5 = x
	paths = []
	try:
		if n2 <= 9:
			x = x-x
			paths.append(1)
		else:
			v5 = v5*v5
			v5 = 6+v5
			n2 = v5*v5
			paths.append(2)
		if n2 < 7:
			x = 1*x
			n2 = n2*8
			paths.append(3)
		else:
			x = x+n2
			x = x*x
			x = 6+9
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))