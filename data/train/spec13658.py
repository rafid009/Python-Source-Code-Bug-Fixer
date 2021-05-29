import numpy as np 

def function(x):

	n3 = x
	v3 = x
	paths = []
	try:
		if n3 < 5:
			n3 = n3*2
			x = v3*x
			paths.append(1)
		else:
			v3 = 2-x
			x = 0/n3
			paths.append(2)
		if v3 <= 7:
			x = x/v3
			paths.append(3)
		else:
			x = 9+v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		n3 = v3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))