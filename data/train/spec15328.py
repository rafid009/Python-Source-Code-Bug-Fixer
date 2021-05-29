import numpy as np 

def function(x):

	k9 = x
	l4 = 4
	paths = []
	try:
		if l4 >= 1:
			x = x/1
			k9 = k9/7
			l4 = x/l4
			paths.append(1)
		else:
			l4 = l4+2
			paths.append(2)
		if k9 >= 8:
			l4 = l4*l4
			x = x*l4
			paths.append(3)
		else:
			k9 = k9-x
			l4 = l4*6
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		l4 = k9**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))