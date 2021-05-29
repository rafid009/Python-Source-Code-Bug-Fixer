import numpy as np 

def function(x):

	l9 = 5
	k3 = 6
	paths = []
	try:
		if l9 <= 8:
			k3 = k3-9
			l9 = k3/6
			x = x*x
			paths.append(1)
		else:
			l9 = 1+l9
			l9 = l9/4
			k3 = k3-6
			paths.append(2)
		if k3 >= 6:
			l9 = k3*l9
			l9 = l9*x
			paths.append(3)
		else:
			x = 7+x
			l9 = x-2
			l9 = 2+l9
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		l9 = k3**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))