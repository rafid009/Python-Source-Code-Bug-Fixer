import numpy as np 

def function(x):

	k7 = 7
	l0 = x
	paths = []
	try:
		if l0 >= 8:
			k7 = k7*x
			l0 = l0*0
			paths.append(1)
		else:
			l0 = l0*2
			k7 = l0+1
			paths.append(2)
		if l0 <= 7:
			l0 = l0/6
			l0 = l0/3
			paths.append(3)
		else:
			l0 = 6/l0
			k7 = l0-7
			k7 = k7-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))