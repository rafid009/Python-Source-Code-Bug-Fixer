import numpy as np 

def function(x):

	k7 = x
	l2 = x
	paths = []
	try:
		if l2 > 2:
			x = l2+x
			x = 2*2
			k7 = 9-2
			paths.append(1)
		else:
			k7 = 8/k7
			x = l2+x
			x = x+9
			paths.append(2)
		if l2 < 6:
			k7 = 7+1
			x = k7*l2
			paths.append(3)
		else:
			l2 = l2+k7
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))