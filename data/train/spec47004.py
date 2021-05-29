import numpy as np 

def function(x):

	u3 = x
	n3 = x
	paths = []
	try:
		if x <= 8:
			u3 = u3/u3
			n3 = n3+9
			n3 = n3/8
			paths.append(1)
		else:
			x = x*5
			n3 = n3+5
			paths.append(2)
		if x > 7:
			u3 = u3-u3
			x = x/5
			paths.append(3)
		else:
			n3 = n3*8
			n3 = 7/n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))