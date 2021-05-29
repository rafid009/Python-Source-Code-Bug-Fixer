import numpy as np 

def function(x):

	l3 = 4
	k7 = x
	paths = []
	try:
		if l3 < 2:
			l3 = x*l3
			l3 = l3-k7
			k7 = k7*x
			paths.append(1)
		else:
			k7 = 2*k7
			l3 = k7+x
			paths.append(2)
		if x < 3:
			k7 = 5+k7
			paths.append(3)
		else:
			k7 = k7/5
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		k7 = l3**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))