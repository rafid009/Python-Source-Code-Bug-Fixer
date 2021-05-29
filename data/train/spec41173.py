import numpy as np 

def function(x):

	k9 = x
	l6 = 0
	paths = []
	try:
		if l6 <= 5:
			l6 = 0*l6
			paths.append(1)
		else:
			k9 = k9-0
			paths.append(2)
		if x >= 9:
			l6 = 5/1
			l6 = l6-1
			paths.append(3)
		else:
			x = x*x
			x = x*8
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))