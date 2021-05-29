import numpy as np 

def function(x):

	n8 = x
	u3 = 2
	paths = []
	try:
		if n8 < 4:
			u3 = u3/u3
			paths.append(1)
		else:
			u3 = 0-u3
			x = 0+7
			x = x-2
			paths.append(2)
		if u3 < 2:
			u3 = u3*0
			u3 = n8+x
			paths.append(3)
		else:
			x = 8*x
			u3 = 8*x
			u3 = u3*u3
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))