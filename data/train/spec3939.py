import numpy as np 

def function(x):

	u3 = x
	n2 = x
	paths = []
	try:
		if u3 >= 4:
			x = 3+x
			paths.append(1)
		else:
			n2 = n2*9
			paths.append(2)
		if n2 < 5:
			x = x+n2
			paths.append(3)
		else:
			x = u3*x
			u3 = u3/3
			x = x/7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))